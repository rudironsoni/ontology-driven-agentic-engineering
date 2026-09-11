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
boundary.

ODAE is a Design Science Research design artifact. Its definitions describe the
proposed mechanism; they do not establish that the mechanism improves outcomes.
Semantic continuity is a provisional quality objective: engineering meaning,
rationale, constraints, authority, and realization relationships should remain
recoverable and internally consistent across artifacts and change.

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

## Current maturity

This initial revision contains conceptual framework definitions and a manual
conformance checklist. It does not yet supply a machine-readable schema, executable
validator, validated serialization, automated validation workflow, or completed
adoption example. It must not be described as a validated implementation.

The intended initial representation is Markdown with typed metadata. Serialization
and executable validation remain open design questions. Consequential framework
changes should proceed from an open proposal to an actual decision, specification,
implementation, and executed framework evidence. No accepted decision history is
reconstructed retroactively.

Framework evidence concerns the framework implementation itself. A successful schema
or validator check would not establish improved software-engineering outcomes.
