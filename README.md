# Ontology-Driven Agentic Engineering

Ontology-Driven Agentic Engineering (ODAE) is a proposed software-engineering
framework for relating domain semantics, deliberation, architectural decisions,
realization contracts, implementation, and verification evidence.

The framework addresses an engineering problem: when these artifacts disagree or
lose their connections, a reader must reconstruct what a statement means, whether
it remains current, and which claim it governs. ODAE defines explicit relationship,
authority, and lifecycle semantics to make those questions inspectable by people
and software agents. Its empirical effectiveness has not been established.

## Artifact roles

| Role | Responsibility |
|---|---|
| Ontology | Defines domain vocabulary, identity, types, relationships, and constraints. |
| RFC | Records a proposed change and its deliberation. It is not an accepted decision. |
| ADR | Records a consequential decision, its rationale, and its status. |
| Specification | Defines realization obligations, either for a bounded change or a durable normative contract. |
| Implementation | Represents the realized technical state at an identified revision. |
| Evidence | Records observations supporting or challenging a specified claim about that state. |

An ontology defines semantics; a knowledge graph instantiates them. A specification
does not replace architectural rationale. Source code does not by itself establish
why a decision was made. A test definition is not an executed test result.

## Framework definition

Start with the [metamodel](framework/metamodel.md), then read the
[semantic](framework/semantic-model.md), [artifact](framework/artifact-model.md),
[authority](framework/authority-model.md), [relationship](framework/relationship-model.md),
[lifecycle](framework/lifecycle-model.md), and [conformance](framework/conformance.md)
models. [Applicability](framework/applicability.md) defines the intended adoption
boundary. The [record format](framework/record-format.md) defines the executable JSON
representation.

ODAE is a Design Science Research design artifact. Its definitions describe the
proposed mechanism; they do not establish that the mechanism improves outcomes.
The framework aims to keep meaning, rationale, constraints, authority, and realization
links recoverable as the system changes.

## Initial adoption

Identify one consequential change and the durable concepts it affects. Locate its
existing proposal, decision, specification, implementation revision, and executed
evidence. Assign explicit identities and links where the roles apply. Record missing
information as missing rather than reconstructing undocumented decisions as fact.

Use the authority and lifecycle models to distinguish a proposal from an accepted
constraint and current guidance from superseded history. Review links and claim
scope using the conformance checklist. Extend the vocabulary only when a concrete
domain need requires it, documenting the meaning and permitted endpoints of each
new relationship.

Validate an ODAE document with Python 3.11 or newer:

```sh
python3 validator/validate.py examples/minimal/odae.json
```

The example is fictional. Its evidence record demonstrates the format and does not
report a real payment-system result.

## Current maturity

ODAE v1 contains the conceptual framework, a JSON record format, a standard-library
validator, and one fictional complete example. The validator checks structure,
references, relation endpoints, lifecycle values, supersession, and evidence revision.
It does not judge whether prose is true or whether adopting ODAE improves engineering.

The reference implementation is intentionally small. It has no graph database,
service, custom agent protocol, generated site, or automated validation workflow.

Framework evidence concerns the framework implementation itself. A successful format
or validator check would not establish improved software-engineering outcomes.
