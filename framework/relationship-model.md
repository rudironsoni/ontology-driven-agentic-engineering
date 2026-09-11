# Relationship model

Relationships state how identified artifacts and semantic objects are connected.
Each relationship needs a direction, meaning, and permitted endpoint roles. A generic
hyperlink alone does not establish whether one artifact governs, realizes, or verifies
another.

Candidate relationships include targeting a semantic object, recording a decision
about a proposal, constraining a specification, realizing a specification, and
providing verification evidence for a claim. Dependency, derivation, and supersession
are different relationships and must not be used interchangeably.

A verification link identifies the claim and evaluated revision. A supersession link
identifies what is replaced and within which scope. Preserve historical traversal
when a successor changes the current interpretation.

The concrete relation vocabulary, cardinalities, and encoding remain open. Extensions
must document their semantics before being used as conformance obligations.
