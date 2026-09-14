#!/usr/bin/env python3

import json
import sys
from pathlib import Path


ROLE_STATES = {
    "semantic": {"proposed", "current", "deprecated", "superseded"},
    "proposal": {"draft", "proposed", "accepted", "rejected", "withdrawn"},
    "decision": {"proposed", "accepted", "superseded"},
    "specification": {"draft", "active", "fulfilled", "deprecated", "superseded"},
    "implementation": {"current", "historical"},
    "evidence": {"recorded", "superseded"},
}

ROLE_FIELDS = {
    "semantic": {"definition"},
    "proposal": {"summary"},
    "decision": {"decision", "rationale"},
    "specification": {"obligation", "specification_kind"},
    "implementation": {"path"},
    "evidence": {"claim", "procedure", "result", "evaluated_revision"},
}

RELATION_ROLES = {
    "targets": ({"proposal", "decision", "specification"}, {"semantic"}),
    "decides": ({"decision"}, {"proposal"}),
    "constrains": ({"decision"}, {"specification"}),
    "realizes": ({"implementation"}, {"specification"}),
    "verifies": ({"evidence"}, {"implementation"}),
    "derived_from": (set(ROLE_STATES), set(ROLE_STATES)),
}

COMMON_RECORD_FIELDS = {
    "id",
    "role",
    "title",
    "scope",
    "location",
    "revision",
    "lifecycle",
}

GAP_FIELDS = {"id", "missing_role", "scope", "needed_by", "status", "reason"}


def _is_text(value):
    return isinstance(value, str) and bool(value.strip())


def validate_document(document):
    errors = []
    if not isinstance(document, dict):
        return ["document: expected object"]
    unknown_document_fields = sorted(set(document) - {"format", "project", "records", "relations", "gaps"})
    if unknown_document_fields:
        errors.append(f"document: unknown fields {', '.join(unknown_document_fields)}")
    if document.get("format") != "odae/v1":
        errors.append("format: expected odae/v1")
    if not _is_text(document.get("project")):
        errors.append("project: expected non-empty string")

    records = document.get("records")
    relations = document.get("relations")
    gaps = document.get("gaps", [])
    if not isinstance(records, list) or not records:
        errors.append("records: expected non-empty array")
        records = []
    if not isinstance(relations, list):
        errors.append("relations: expected array")
        relations = []
    if not isinstance(gaps, list):
        errors.append("gaps: expected array")
        gaps = []

    record_by_id = {}
    for index, record in enumerate(records):
        prefix = f"records[{index}]"
        if not isinstance(record, dict):
            errors.append(f"{prefix}: expected object")
            continue
        record_id = record.get("id")
        role = record.get("role")
        if not _is_text(record_id):
            errors.append(f"{prefix}.id: expected non-empty string")
        elif record_id in record_by_id:
            errors.append(f"{prefix}.id: duplicate {record_id}")
        else:
            record_by_id[record_id] = record
        if not _is_text(role) or role not in ROLE_STATES:
            errors.append(f"{prefix}.role: unknown role {role!r}")
            continue

        allowed = COMMON_RECORD_FIELDS | ROLE_FIELDS[role]
        unknown = sorted(set(record) - allowed)
        if unknown:
            errors.append(f"{prefix}: unknown fields {', '.join(unknown)}")
        for field in sorted(COMMON_RECORD_FIELDS - {"scope"}):
            if field == "lifecycle":
                continue
            if not _is_text(record.get(field)):
                errors.append(f"{prefix}.{field}: expected non-empty string")
        for field in sorted(ROLE_FIELDS[role]):
            value = record.get(field)
            if field == "result":
                if not _is_text(value) or value not in {"pass", "fail", "inconclusive"}:
                    errors.append(f"{prefix}.result: expected pass, fail, or inconclusive")
            elif field == "specification_kind":
                if not _is_text(value) or value not in {"change", "normative"}:
                    errors.append(f"{prefix}.specification_kind: expected change or normative")
            elif not _is_text(value):
                errors.append(f"{prefix}.{field}: expected non-empty string")

        scope = record.get("scope")
        if not isinstance(scope, list) or any(not _is_text(item) for item in scope):
            errors.append(f"{prefix}.scope: expected string array")

        lifecycle = record.get("lifecycle")
        if not isinstance(lifecycle, dict):
            errors.append(f"{prefix}.lifecycle: expected object")
            continue
        if set(lifecycle) != {"state", "basis", "transition_owner"}:
            errors.append(f"{prefix}.lifecycle: expected state, basis, and transition_owner")
            continue
        state = lifecycle["state"]
        basis = lifecycle["basis"]
        valid_bases = {"explicit", "inferred", "missing", "unresolved", "defaulted"}
        if not _is_text(basis) or basis not in valid_bases:
            errors.append(f"{prefix}.lifecycle.basis: unknown basis {basis!r}")
        if _is_text(basis) and basis in {"missing", "unresolved"}:
            if state is not None:
                errors.append(f"{prefix}.lifecycle.state: expected null for {basis} basis")
        elif not _is_text(state) or state not in ROLE_STATES[role]:
            errors.append(f"{prefix}.lifecycle.state: invalid {role} state {state!r}")
        if not _is_text(lifecycle["transition_owner"]):
            errors.append(f"{prefix}.lifecycle.transition_owner: expected non-empty string")

    relation_ids = set()
    outbound = {}
    inbound = {}
    for index, relation in enumerate(relations):
        prefix = f"relations[{index}]"
        if not isinstance(relation, dict):
            errors.append(f"{prefix}: expected object")
            continue
        if set(relation) != {"id", "type", "from", "to"}:
            errors.append(f"{prefix}: expected id, type, from, and to")
            continue
        relation_id = relation["id"]
        relation_type = relation["type"]
        source_id = relation["from"]
        target_id = relation["to"]
        if not _is_text(relation_id):
            errors.append(f"{prefix}.id: expected non-empty string")
        elif relation_id in relation_ids:
            errors.append(f"{prefix}.id: duplicate {relation_id}")
        else:
            relation_ids.add(relation_id)
        source = record_by_id.get(source_id) if _is_text(source_id) else None
        target = record_by_id.get(target_id) if _is_text(target_id) else None
        if source is None:
            errors.append(f"{prefix}.from: unresolved {source_id}")
        if target is None:
            errors.append(f"{prefix}.to: unresolved {target_id}")
        if source_id == target_id:
            errors.append(f"{prefix}: self relation is not allowed")
        if relation_type == "supersedes":
            if source and target and source["role"] != target["role"]:
                errors.append(f"{prefix}: supersedes requires matching roles")
        elif not _is_text(relation_type) or relation_type not in RELATION_ROLES:
            errors.append(f"{prefix}.type: unknown relation {relation_type!r}")
        elif source and target:
            source_roles, target_roles = RELATION_ROLES[relation_type]
            if source["role"] not in source_roles or target["role"] not in target_roles:
                errors.append(f"{prefix}: invalid roles for {relation_type}")
        if _is_text(source_id) and _is_text(relation_type):
            outbound.setdefault(source_id, set()).add(relation_type)
        if _is_text(target_id) and _is_text(relation_type):
            inbound.setdefault(target_id, set()).add(relation_type)

    for record_id, record in record_by_id.items():
        scope = record.get("scope", [])
        if not isinstance(scope, list):
            scope = []
        for scope_id in scope:
            if not _is_text(scope_id):
                continue
            target = record_by_id.get(scope_id)
            if target is None:
                errors.append(f"{record_id}.scope: unresolved {scope_id}")
            elif target["role"] != "semantic":
                errors.append(f"{record_id}.scope: {scope_id} is not semantic")
        lifecycle = record.get("lifecycle")
        if isinstance(lifecycle, dict) and lifecycle.get("state") == "superseded":
            if "supersedes" not in inbound.get(record_id, set()):
                errors.append(f"{record_id}: superseded record needs supersedes relation")
        if record.get("role") == "evidence" and "verifies" not in outbound.get(record_id, set()):
            errors.append(f"{record_id}: evidence needs verifies relation")

    gap_ids = set()
    for index, gap in enumerate(gaps):
        prefix = f"gaps[{index}]"
        if not isinstance(gap, dict):
            errors.append(f"{prefix}: expected object")
            continue
        if set(gap) != GAP_FIELDS:
            errors.append(f"{prefix}: expected id, missing_role, scope, needed_by, status, and reason")
            continue
        gap_id = gap["id"]
        if not _is_text(gap_id):
            errors.append(f"{prefix}.id: expected non-empty string")
        elif gap_id in gap_ids or gap_id in record_by_id:
            errors.append(f"{prefix}.id: duplicate {gap_id}")
        else:
            gap_ids.add(gap_id)
        missing_role = gap["missing_role"]
        if not _is_text(missing_role) or missing_role not in ROLE_STATES:
            errors.append(f"{prefix}.missing_role: unknown role {missing_role!r}")
        status = gap["status"]
        if not _is_text(status) or status not in {"missing", "not_observable"}:
            errors.append(f"{prefix}.status: expected missing or not_observable")
        if not _is_text(gap["reason"]):
            errors.append(f"{prefix}.reason: expected non-empty string")
        needed_by = gap["needed_by"]
        if not _is_text(needed_by) or needed_by not in record_by_id:
            errors.append(f"{prefix}.needed_by: unresolved {needed_by}")
        scope = gap["scope"]
        if not isinstance(scope, list) or any(not _is_text(item) for item in scope):
            errors.append(f"{prefix}.scope: expected string array")
            continue
        for scope_id in scope:
            target = record_by_id.get(scope_id)
            if target is None:
                errors.append(f"{prefix}.scope: unresolved {scope_id}")
            elif target["role"] != "semantic":
                errors.append(f"{prefix}.scope: {scope_id} is not semantic")

    for relation in relations:
        if not isinstance(relation, dict) or relation.get("type") != "verifies":
            continue
        source_id = relation.get("from")
        target_id = relation.get("to")
        source = record_by_id.get(source_id) if _is_text(source_id) else None
        target = record_by_id.get(target_id) if _is_text(target_id) else None
        if source and target and source.get("evaluated_revision") != target.get("revision"):
            errors.append(f"{relation['id']}: evidence revision does not match implementation")

    return sorted(set(errors))


def load_document(path):
    if path.is_symlink() or not path.is_file():
        raise ValueError("input must be a regular file")
    if path.stat().st_size > 1_048_576:
        raise ValueError("input exceeds 1 MiB")
    return json.loads(path.read_text(encoding="utf-8"))


def main(argv):
    if len(argv) != 2:
        print("usage: validate.py <odae.json>", file=sys.stderr)
        return 2
    path = Path(argv[1])
    try:
        document = load_document(path)
    except (OSError, ValueError, json.JSONDecodeError) as error:
        print(f"INVALID {path}: {error}", file=sys.stderr)
        return 1
    errors = validate_document(document)
    if errors:
        for error in errors:
            print(f"ERROR {error}", file=sys.stderr)
        print(f"INVALID {path}: {len(errors)} error(s)", file=sys.stderr)
        return 1
    record_count = len(document["records"])
    relation_count = len(document["relations"])
    gap_count = len(document.get("gaps", []))
    print(f"VALID {path}: {record_count} records, {relation_count} relations, {gap_count} gaps")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
