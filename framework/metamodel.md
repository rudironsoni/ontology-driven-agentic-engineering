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
and revision. An authoritative requirement can conflict with implemented behavior;
that conflict is information to examine, not permission to overwrite either record.

This is a conceptual definition. Concrete fields, cardinalities, serialization, and
validation rules require a separately specified implementation contract.
