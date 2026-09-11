# Authority model

Authority is scoped to a kind of claim, not assigned as a universal ranking of files.

| Record | Authority within its declared scope |
|---|---|
| Ontology | Meaning, identity, classification, and domain relationships. |
| RFC | What was proposed and deliberated. |
| Accepted ADR | What was decided and why. |
| Active specification | What behavior or realization is required. |
| Implementation revision | What technical state exists at that revision. |
| Evidence record | What was observed by the recorded verification activity. |

Interpret each record with its scope, revision, and lifecycle status. A rejected RFC
may explain historical deliberation without constraining current implementation.
An accepted ADR remains a decision record when implementation does not conform to it.

Resolve competing claims explicitly. A recent file timestamp is not sufficient to
establish precedence. Supersession must identify the affected authority and scope;
it does not erase the earlier rationale. These are framework interpretation rules,
not evidence of their empirical benefit.
