# Lifecycle model

Lifecycle status determines how a record should be interpreted over time. An RFC may
be under deliberation, accepted, rejected, or withdrawn. An ADR may be proposed,
accepted, or superseded. These illustrative states do not yet define an executable
transition system.

Change specifications and normative specifications have different completion
semantics. Fulfilling a bounded change does not retire a durable contract. Record
the distinction instead of treating every specification as temporary.

Preserve consequential decision history. When current guidance changes, identify the
successor and its scope rather than silently rewriting the earlier rationale. Record
unresolved status explicitly; do not infer acceptance from implementation alone.

A snapshot can show current status and links. Establishing that a transition was
permitted requires transition records or history. Legal transitions and their
preconditions remain an implementation design question.
