# CyberAlchemy Lab assets for Agentic Research Network

Status: **read-only adoption inventory**. Authority effect: **none**. The Definition source snapshot is now copied; the remaining stages are recommendations. This inventory does not admit definitions, activate Lab governance in ARN, or claim a working ontology service.

## What was inspected

The source cut is the public Lab commit [`19d860e719d6d65c05bff74b1c7547b3d48defcc`](https://github.com/cyberAlchemyAI/CyberAlchemy-lab/tree/19d860e719d6d65c05bff74b1c7547b3d48defcc). The [machine manifest](source-manifest.json) records all 22 top-level areas (138,855 tracked paths), all 183 current admitted Definition identities with exact source hashes, the 36-record initial reuse shortlist, nine selected Relation Kind records, and the 17 Lab schema snapshots already in ARN. The [complete current Definition catalog](CURRENT-DEFINITIONS.md) lists every current identity. Rebuild both with [the inventory script](../../../scripts/build_lab_asset_inventory.py) against that exact source commit.

This is a repository-wide **area inventory with a selected-file audit**, not a claim that every one of the 138,855 files was read. The source cut avoids uncommitted Lab changes and distinguishes admitted contracts, candidate implementations, historical evidence, and generated projections. The path list and exact digests in the machine manifest are the adoption bill of materials.

To check the manifest against a local Lab checkout with the pinned commit available:

```sh
python3 scripts/build_lab_asset_inventory.py \
  --lab-root /path/to/CyberAlchemy-lab \
  --ref 19d860e719d6d65c05bff74b1c7547b3d48defcc \
  --check
```

## Recommended starting set

| Priority | Lab asset | Use in ARN | Condition before adoption |
| --- | --- | --- | --- |
| 0 | Definition registry and complete 183-record catalog; 36 initial priorities | A read-only semantic baseline for Project, Product, Goal, research work, evidence, authority, ontology and provenance | **Copied:** all 189 admitted versions in the [Lab reference snapshot](../../../references/cyberalchemy-lab/definitions/README.md). Map each ARN concept to reuse, specialization, or new definition; do not replace ARN definitions by matching names. |
| 0 | Definition v1/v2 schemas and candidate lifecycle profile | Shape and review vocabulary for ARN Definition records | Keep the profile's `candidate-unadmitted` status. Define an ARN owner and admission route before using it as policy. |
| 1 | Artifact Type, Relation Kind, Typed Relation and ontology schemas | Graph contracts for research objects and their links | Check exact endpoint types, qualifiers, schema versions, and referential closure. |
| 1 | Nine admitted Relation Kinds | Initial link vocabulary for contributions, derivation, evidence, evaluation and governance | Existing Lab endpoint pairs do not automatically cover ARN types; extend by an ARN-owned candidate rather than asserting Lab admission. |
| 2 | Project State, decision, policy, role, principal, provenance and context patterns | A record and review trail for research and product decisions | Model ARN-specific actors, rights and transitions; preserve Lab evidence and authority boundaries. |
| 3 | Ontology lifecycle witness and governed-node proposal | Experimental event replay and context projection design | Treat as a candidate. Import only with its DomainSpec compiler/source closure, tests, and an ARN conformance target. |
| 4 | Define workflow and Lab runtime | Optional authoring and local inspection adapters | Decide whether ARN needs them after the record model is stable. Do not import the 1,023-file Define package or the Lab runtime wholesale. |

### Definitions: start here

The Lab [registry](https://github.com/cyberAlchemyAI/CyberAlchemy-lab/blob/19d860e719d6d65c05bff74b1c7547b3d48defcc/authority/definitions/registry.json) contains **189 admitted exact versions: 183 current identities and six historical/noncurrent versions**. The prior 36 count was an initial relevance shortlist, not the number admitted. The [full current catalog](CURRENT-DEFINITIONS.md) preserves the 183 identities, terms, versions and source paths. Its 183 identities have 180 distinct display terms, so a term alone is not a safe lookup key. The initial 36 priorities are:

| Group | Selected terms |
| --- | --- |
| Work and research | Agent, Goal, Product, Product Capability, Project, Research Inquiry, Experiment Design, Research Run, Finding, Evidence Set, Source, Work |
| Meaning and records | Artifact Type, Artifact Type Registry, Definition, Context, Ontology, Ontology Node, Ontology Edge, Ontology Manifest, Ontology Cut, Ontology View |
| Links and provenance | Relation Kind, Typed Relation, Provenance, Semantic Event History, Governance Event History |
| Review and authority | Admission Transaction, Authority, Authority Boundary, Decision, Policy, Principal, Project State, Review, Role |

The other 147 current identities are available for review. Likely next-pass concepts include Artifact, Hypothesis, Experiment Run, Observation, Measurement Method, Measurement Result, Evaluation, Evidence, Validation Receipt, Challenge Contract, Ledger, Workflow and Traceability. Their meanings and version compatibility still need an ARN use-case review.

Some current Definition files live under `evidence/migrations/...`; their directory name does not negate their registry status. Conversely, registry admission is scoped to Lab. Copying a file into ARN does not admit its meaning in ARN. ARN currently has [41 task-local candidate definitions](../../proposals/agentic-research-network/2026-10-29/model-v1/definitions.json), with **no exact term matches to any of the 183 current Lab terms**. A bridge should record each ARN term's Lab source, intended specialization, owner, unresolved differences and exact version. In particular, research novelty, reward, sponsor, W-token and engineer marketplace terms remain ARN-owned proposals. The Lab already has a substantial admitted vocabulary; admitting more Lab definitions solely to increase the count is unnecessary.

Copy the [Definition schemas](https://github.com/cyberAlchemyAI/CyberAlchemy-lab/tree/19d860e719d6d65c05bff74b1c7547b3d48defcc/authority/artifact-types/definition), [registry index](https://github.com/cyberAlchemyAI/CyberAlchemy-lab/blob/19d860e719d6d65c05bff74b1c7547b3d48defcc/authority/definitions/DEFINITIONS-INDEX.md) and [drift audit](https://github.com/cyberAlchemyAI/CyberAlchemy-lab/blob/19d860e719d6d65c05bff74b1c7547b3d48defcc/authority/definitions/drift-audit.json) only as supporting source evidence. The [Definition lifecycle profile](https://github.com/cyberAlchemyAI/CyberAlchemy-lab/blob/19d860e719d6d65c05bff74b1c7547b3d48defcc/authority/profiles/definition/v1/lifecycle.json) is **candidate-unadmitted**. Its sequence is candidate-authored → validated-candidate → owner-reviewed → admitted, with superseded/withdrawn routes. A validation PASS and an owner review are separate from admission.

### Relations and ontology: build the dependency closure

[Lab Decision 0070](https://github.com/cyberAlchemyAI/CyberAlchemy-lab/blob/19d860e719d6d65c05bff74b1c7547b3d48defcc/docs/decisions/0070-definition-complete-lab-model-admission/DECISION.md) admits 93 Artifact Type contracts, 40 Relation Kinds, and one Governed Model instance. It admits **zero Typed Relations and zero runtime activations**. The useful initial nine are `contributes-to`, `declares-effect-on`, `derives-from`, `engages-inquiry`, `evaluates`, `evidence-bears-on`, `governed-by`, `member-of`, and `realizes`. Their exact instance files and endpoint-pair counts are in the manifest; the [postimage registry](https://github.com/cyberAlchemyAI/CyberAlchemy-lab/blob/19d860e719d6d65c05bff74b1c7547b3d48defcc/docs/decisions/0070-definition-complete-lab-model-admission/proposal/relation-kind-registry-postimage.json) covers all 40. The nine may be a starting vocabulary, but ARN needs its own typed edges for contribution claims, novelty comparisons, experiment results, product value and reward attribution.

Relevant source schemas include `ontology-node/v2`, `ontology-edge/v1`, `ontology-package/v1`, `ontology-manifest/v1`, `ontology-cut/v1`, `ontology-view/v1`, `semantic-event-history/v1`, `governance-event-history/v1`, `context-request/v1` and `context-view/v1` under [Lab Artifact Types](https://github.com/cyberAlchemyAI/CyberAlchemy-lab/tree/19d860e719d6d65c05bff74b1c7547b3d48defcc/authority/artifact-types). ARN's [17 existing schema snapshots](../../../authority/README.md) are byte-identical to this Lab cut; they do not need to be recopied.

The [ontology lifecycle witness](https://github.com/cyberAlchemyAI/CyberAlchemy-lab/blob/19d860e719d6d65c05bff74b1c7547b3d48defcc/ontology-lifecycle/README.md) is a **candidate implementation with automated verification and pending human selections**. It reconstructs a graph at an exact cursor from semantic events, keeps governance events separate, and treats snapshots and views as rebuildable projections. Its Rust reducer covers a thin node/relation model; the richer [governed-node architecture](https://github.com/cyberAlchemyAI/CyberAlchemy-lab/blob/19d860e719d6d65c05bff74b1c7547b3d48defcc/docs/proposals/0004-governed-ontology-node-architecture/proposal.json) is an unselected successor proposal. A portable import would need the Rust package, payload schemas, DomainSpec event-sourcing compiler inputs and outputs, fixtures, tests, and verification script. Importing just `runtime/src/lib.rs` would not establish that closure.

### Governance, authoring and runtime

The Lab [Project State lookup](https://github.com/cyberAlchemyAI/CyberAlchemy-lab/blob/19d860e719d6d65c05bff74b1c7547b3d48defcc/authority/project-state-transitions/current.json) and decision/policy/role/principal schemas are useful patterns for an ARN state machine. The [Lab runtime admission note](https://github.com/cyberAlchemyAI/CyberAlchemy-lab/blob/19d860e719d6d65c05bff74b1c7547b3d48defcc/implementation/lab-runtime/ADMISSION.md) limits admitted v1 to a local D74 source profile; the current Project State is D75 and a v2 profile is only a candidate. No external service is activated. ARN should define its own state, actor, and transaction effects.

[Define](https://github.com/cyberAlchemyAI/CyberAlchemy-lab/blob/19d860e719d6d65c05bff74b1c7547b3d48defcc/define/README.md) has a useful authoring flow: goal + intent + context → concepts and sources → reuse/specialize/propose/open → review → a Definition Pack for a named consumer. Its source is an imported private candidate package and the Lab CLI is separately candidate. The [architecture dependency rules](https://github.com/cyberAlchemyAI/CyberAlchemy-lab/blob/19d860e719d6d65c05bff74b1c7547b3d48defcc/architecture/pattern-library/DEPENDENCY-RULES.md) are useful review guidance: exact source and digest, separate candidate from authority, and distinguish local ontology mappings from globally admitted Typed Relations.

## Whole-repository disposition

Counts are tracked files at the pinned public Lab commit. “Reference” means consult exact source while designing ARN; it is not an import instruction.

| Area | Files | Disposition for ARN |
| --- | ---: | --- |
| `authority` | 3,159 | **Selectively snapshot** current definitions, type schemas and relation kinds with exact provenance; never transfer Lab authority by directory copy. |
| `ontology-lifecycle` | 823 | **Experimental later**: import a tested runtime/compiler closure only if ARN selects event sourcing. |
| `architecture` | 32 | **Reference** dependency and testing rules; adapt to ARN's smaller scope. |
| `contexts` | 34 | **Reference** context selection and projection patterns; create ARN consumer contexts. |
| `coordination` | 10 | **Reference** handoff and owner patterns; define ARN roles independently. |
| `define` | 1,645 | **Reference** the Definition Pack method; consider an adapter after semantic bridge work. |
| `implementation` | 5,209 | **Selectively evaluate** Define CLI, Lab runtime and other implementation bindings; no blanket copy. |
| `tooling` | 35 | **Reference** inventory and validation tooling; port only a specific tool with its dependencies. |
| `tests` | 78 | **Reference** source qualification; write ARN tests for ARN contracts and imported adapters. |
| `docs` | 65,125 | **Selectively reference** decisions, guides, proposals and audits by exact path. Much is history or generated output. |
| `evidence` | 3,421 | **Reference** exact admission/migration evidence; copy only the records needed to verify an adopted source. |
| `craft` | 14,762 | **Defer** broad language and formalization experiments until ARN has a concrete compilation need. |
| `product` | 32,019 | **Exclude from foundation import**; product histories and generated runs are not reusable core semantics. Product 001 already has its own bounded EA example. |
| `output` | 11,267 | **Exclude** generated projections and run output; regenerate from selected canonical input when needed. |
| `website` | 1,208 | **Defer** UI and presentation assets until there is an ARN product surface. |
| `.arcanum` | 19 | **Defer** Lab-local workflow configuration. |
| `claude` | 4 | **Defer** tool-specific local guidance. |
| `.github` | 1 | **Reference** only if adapting repository workflow. |
| `.gitattributes`, `.gitignore` | 1 each | **Compare** configuration against this repository; preserve its own rules. |
| `README.md` | 1 | **Reference** the Lab entry point. |
| `CyberAlchemy-From-Intent-to-Bounded-Evidence.pdf` | 1 | **Reference** presentation material; no model dependency. |

## Import sequence and acceptance checks

1. **Semantic bridge.** The read-only source slice now contains all 183 current identities and six historical versions, retaining original IDs, versions, status and digest. Review the full catalog; add an ARN mapping for each local definition: reuse, specialize, new, or unresolved. Check for collisions and owner assignment. Keep the copied Lab registry as evidence, not ARN's current lookup.
2. **Typed graph.** Reuse the 17 existing schemas, add only required type/ontology schemas and the selected relation records, and build an ARN type/edge registry. Validate exact endpoint pairs, qualifiers, referenced definitions, versioned type IDs and cycles. Record which relations are genuinely new ARN proposals.
3. **Decision trail.** Define ARN review, Project State, appeal and contribution decisions using the Lab provenance/context patterns. Separate semantic state, authority state, validation evidence and publication state.
4. **Ontology prototype.** If the graph needs event replay, import the whole candidate closure into an experimental module. Prove replay determinism, cut consistency, governance joins and projection regeneration against ARN fixtures before making it a core dependency.
5. **Authoring/runtime.** Try a small Define Pack for Product 001 and one new research inquiry. Add CLI/runtime adapters only after the record and ownership model is stable.

For every import: pin the Lab commit; copy only selected paths; record SHA-256 and any path translation; verify all referenced schemas and records resolve; run ARN validation and focused tests; keep `authority_effect: none` until a separate ARN owner decision exists. Avoid copying generated output, historical run data, participant information, local stores, keys or broad Lab packages as a shortcut. A source snapshot is evidence of the Lab bytes at the pinned cut, not an ARN admission or live product behavior.
