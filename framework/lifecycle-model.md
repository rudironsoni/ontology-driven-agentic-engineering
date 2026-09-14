# Lifecycle model

Lifecycle status determines how a record should be interpreted over time. An RFC may
be under deliberation, accepted, rejected, or withdrawn. An ADR may be proposed,
accepted, or superseded. ODAE v1 validates the state vocabulary for each role but does
not validate transitions between revisions.

Change specifications and normative specifications have different completion
semantics. Fulfilling a bounded change does not retire a durable contract. Record
the distinction instead of treating every specification as temporary.

Preserve consequential decision history. When current guidance changes, identify the
successor and its scope rather than silently rewriting the earlier rationale. Record
unresolved status explicitly; do not infer acceptance from implementation alone.

Record how the state is known. The basis is explicit, inferred, missing, unresolved,
or defaulted. Missing and unresolved states have no state value. Name the person,
group, or mechanism that owns the transition.

A snapshot can show current status and links. Establishing that a transition was
permitted requires transition records or history. Legal transition sequences and
their preconditions remain outside ODAE v1.
