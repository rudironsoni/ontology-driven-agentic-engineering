# Relationship model

Relationships state how identified artifacts and semantic objects are connected.
Each relationship needs a direction, meaning, and permitted endpoint roles. A generic
hyperlink alone does not establish whether one artifact governs, realizes, or verifies
another.

ODAE v1 defines `targets`, `decides`, `constrains`, `realizes`, `verifies`,
`supersedes`, and `derived_from`. Their permitted endpoint roles are part of the
[record format](record-format.md). Derivation and supersession are different
relationships and must not be used interchangeably.

A verification link identifies the claim and evaluated revision. A supersession link
identifies what is replaced and within which scope. Preserve historical traversal
when a successor changes the current interpretation.

Extensions must document their direction, meaning, and permitted endpoint roles before
they become conformance obligations. ODAE v1 rejects unknown relation types.
