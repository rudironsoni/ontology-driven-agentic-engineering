# Conformance

Conformance concerns agreement with stated framework rules and project obligations.
Structural validity and software correctness are distinct: a resolved link can point
to a claim that the available evidence does not support.

For a review of a bounded engineering change, examine:

1. Whether identities and references resolve without ambiguous interpretation.
2. Whether artifact roles, claim scopes, and lifecycle states are explicit.
3. Whether governing decisions and realization obligations can be located.
4. Whether superseded guidance identifies its successor where one exists.
5. Whether evidence names the claim, evaluated revision, procedure, result, and limits.
6. Whether missing or conflicting information is recorded rather than silently filled.

Record the reviewed revision and the scope of the check. Run the ODAE v1 structural
validator with:

```sh
python3 validator/validate.py <odae.json>
```

The validator checks required fields, role-specific states, reference resolution,
relation endpoints, supersession links, and evidence revision. It does not decide
whether claims are true or whether two prose statements conflict.

New deterministic checks need a stated rule and an executed test before their behavior
is claimed. Framework evidence records those checks. It does not establish that
adopting ODAE improves engineering outcomes.
