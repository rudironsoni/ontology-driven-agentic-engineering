# Metamodel

ODAE distinguishes semantic objects from the artifacts that propose, decide,
specify, implement, or verify changes concerning them. An artifact has an identity,
a role, a scope, and a lifecycle state. Relationships connect identified objects and
artifacts; their meaning must be explicit.

The ontology supplies domain semantics. The knowledge graph contains concrete
objects, artifacts, and links interpreted using those semantics. Files and directory
names are storage choices, not the metamodel.

The framework separates semantic, artifact, authority, relationship, lifecycle,
conformance, and applicability concerns. A claim must be interpreted with its scope
and revision. Its lifecycle basis distinguishes an explicit state from one that was
inferred, defaulted, missing, or unresolved. An authoritative requirement can conflict
with implemented behavior; that conflict is information to examine, not permission to
overwrite either record.

The [record format](record-format.md) defines the ODAE v1 fields, serialization, and
deterministic validation boundary.
