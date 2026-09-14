# Applicability

ODAE is intended for engineering work in which domain meaning, consequential
decisions, durable constraints, and evolving implementation must remain connected.
Its suitability and costs require evaluation in the intended setting.

Candidate settings include long-lived systems and changes whose rationale cannot be
reliably recovered from source code alone. This is an applicability hypothesis, not
an established advantage. A short-lived script may not justify the recording and
maintenance effort.

Begin with one consequential change. Reuse available artifacts, identify their
roles, and make relevant relationships explicit. Do not require an RFC or ADR for
every edit. The significance of a decision and the expected lifetime of its knowledge
should determine the recording effort.

Agent consumption applies only when a project permits agents to participate. Plain
files or an existing export command are sufficient when the agent can recover the
required records and links.

Extensions should address an identified domain need, preserve existing meanings,
and state any new conformance obligations. Organizational authority and review
responsibilities remain project decisions; ODAE does not assign them automatically.
