# Record format

ODAE v1 uses one JSON document. The document contains identified records and typed
relations. JSON is the reference encoding, not the framework itself.

## Document

| Field | Meaning |
|---|---|
| `format` | Exact value `odae/v1`. |
| `project` | Project identifier. |
| `records` | Semantic and engineering records. |
| `relations` | Directed links between records. |

## Records

Every record has `id`, `role`, `title`, `scope`, `location`, `revision`, and
`lifecycle`. Scope entries point to semantic records. Location identifies the owning
source. Revision identifies the state in which the record applies.

Lifecycle has three fields:

- `state` is the domain state or `null` when it is missing or unresolved.
- `basis` is `explicit`, `inferred`, `missing`, `unresolved`, or `defaulted`.
- `transition_owner` names the person, group, or mechanism that changes the state.

This keeps an unknown state separate from a valid state supplied by a parser default.

Each role adds its own content:

| Role | Required fields |
|---|---|
| `semantic` | `definition` |
| `proposal` | `summary` |
| `decision` | `decision`, `rationale` |
| `specification` | `obligation`, `specification_kind` |
| `implementation` | `path` |
| `evidence` | `claim`, `procedure`, `result`, `evaluated_revision` |

Specification kind is `change` or `normative`. Evidence result is `pass`, `fail`, or
`inconclusive`.

## Relations

Every relation has `id`, `type`, `from`, and `to`.

| Type | Source | Target |
|---|---|---|
| `targets` | Proposal, decision, or specification | Semantic record |
| `decides` | Decision | Proposal |
| `constrains` | Decision | Specification |
| `realizes` | Implementation | Specification |
| `verifies` | Evidence | Implementation |
| `supersedes` | Any record | Earlier record with the same role |
| `derived_from` | Any record | Any record |

A `verifies` relation is valid only when the evidence `evaluated_revision` matches
the implementation revision. A record with state `superseded` must be the target of a
`supersedes` relation.

## Limits

The validator checks document shape, role-specific fields, references, endpoint roles,
lifecycle values, supersession, and evidence revision. It does not decide whether a
claim is true, whether a decision is good, or whether two prose statements conflict.

The [minimal example](../examples/minimal/odae.json) is fictional. Its evidence record
demonstrates the format and does not report a real payment-system result.
