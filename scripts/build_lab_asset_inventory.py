"""Build a read-only, source-pinned Lab asset inventory for ARN adoption review."""

from __future__ import annotations

import argparse
import hashlib
import json
import subprocess
from collections import Counter
from pathlib import Path


ARN_ROOT = Path(__file__).resolve().parents[1]
DEFAULT_OUT = ARN_ROOT / "docs/lab-asset-adoption/2026-11-01/source-manifest.json"
DEFAULT_CATALOG_OUT = ARN_ROOT / "docs/lab-asset-adoption/2026-11-01/CURRENT-DEFINITIONS.md"

CORE_TERMS = {
    "Admission Transaction", "Agent", "Artifact Type", "Artifact Type Registry",
    "Authority", "Authority Boundary", "Context", "Decision", "Definition",
    "Evidence Set", "Experiment Design", "Finding", "Goal",
    "Governance Event History", "Ontology", "Ontology Cut", "Ontology Edge",
    "Ontology Manifest", "Ontology Node", "Ontology View", "Policy",
    "Principal", "Product", "Product Capability", "Project", "Project State",
    "Provenance", "Relation Kind", "Research Inquiry", "Research Run",
    "Review", "Role", "Semantic Event History", "Source", "Typed Relation",
    "Work",
}

RELATION_IDS = {
    "relation.contributes-to", "relation.declares-effect-on",
    "relation.derives-from", "relation.engages-inquiry", "relation.evaluates",
    "relation.evidence-bears-on", "relation.governed-by",
    "relation.member-of", "relation.realizes",
}

GROUP_PATHS = {
    "definition-contract": [
        "authority/definitions/registry.json",
        "authority/definitions/DEFINITIONS-INDEX.md",
        "authority/definitions/drift-audit.json",
        "authority/artifact-types/definition/v1/schema.json",
        "authority/artifact-types/definition/v2/schema.json",
        "authority/profiles/definition/v1/lifecycle.json",
        "authority/profiles/definition/v1/LIFECYCLE.md",
        "docs/lab/how-to/prepare-definition.md",
    ],
    "relation-and-artifact-contract": [
        "docs/decisions/0070-definition-complete-lab-model-admission/DECISION.md",
        "docs/decisions/0070-definition-complete-lab-model-admission/proposal/artifact-type-admission-manifest.json",
        "docs/decisions/0070-definition-complete-lab-model-admission/proposal/relation-kind-registry-postimage.json",
        "authority/artifact-types/artifact-type-registry/v1/schema.json",
        "authority/artifact-types/relation-kind/v2/schema.json",
        "authority/artifact-types/typed-relation/v2/schema.json",
    ],
    "ontology-contract": [
        "authority/artifact-types/ontology-node/v2/schema.json",
        "authority/artifact-types/ontology-edge/v1/schema.json",
        "authority/artifact-types/ontology-package/v1/schema.json",
        "authority/artifact-types/ontology-manifest/v1/schema.json",
        "authority/artifact-types/ontology-cut/v1/schema.json",
        "authority/artifact-types/ontology-view/v1/schema.json",
        "authority/artifact-types/semantic-event-history/v1/schema.json",
        "authority/artifact-types/governance-event-history/v1/schema.json",
        "authority/artifact-types/context-request/v1/schema.json",
        "authority/artifact-types/context-view/v1/schema.json",
    ],
    "ontology-lifecycle-witness": [
        "ontology-lifecycle/README.md",
        "ontology-lifecycle/candidate-selections.json",
        "ontology-lifecycle/business-ontology.json",
        "ontology-lifecycle/product-capability.json",
        "ontology-lifecycle/domainspec/event-sourcing/source.json",
        "ontology-lifecycle/runtime/Cargo.toml",
        "ontology-lifecycle/runtime/src/lib.rs",
        "ontology-lifecycle/scripts/verify.py",
        "docs/proposals/0004-governed-ontology-node-architecture/proposal.json",
        "authority/ontology-integration/candidates/0003-definition-complete-runtime-integration/MODEL.md",
    ],
    "governance-and-state": [
        "authority/project-state-transitions/current.json",
        "authority/artifact-types/project-state/v1/schema.json",
        "authority/artifact-types/decision/v1/schema.json",
        "authority/artifact-types/policy/v1/schema.json",
        "authority/artifact-types/role/v1/schema.json",
        "authority/artifact-types/principal/v1/schema.json",
        "implementation/lab-runtime/ADMISSION.md",
        "docs/lab/guide/authority.md",
        "docs/lab/guide/lifecycle.md",
        "docs/lab/guide/provenance.md",
    ],
    "define-context-and-architecture": [
        "define/README.md",
        "implementation/define-cli/v1/README.md",
        "docs/lab/guide/records-and-connections.md",
        "architecture/ARCHITECTURE.md",
        "architecture/pattern-library/DEPENDENCY-RULES.md",
        "architecture/pattern-library/TESTING-ALIGNMENT.md",
        "tooling/inventory/build_inventory.py",
    ],
}


def git(lab: Path, *args: str) -> bytes:
    return subprocess.run(["git", *args], cwd=lab, check=True, capture_output=True).stdout


def source_bytes(lab: Path, commit: str, path: str) -> bytes:
    return git(lab, "show", f"{commit}:{path}")


def file_entry(lab: Path, commit: str, path: str) -> dict:
    raw = source_bytes(lab, commit, path)
    return {"path": path, "sha256": hashlib.sha256(raw).hexdigest(), "bytes": len(raw)}


def build(lab: Path, ref: str) -> dict:
    commit = git(lab, "rev-parse", ref).decode().strip()
    paths = [p for p in git(lab, "ls-tree", "-r", "--name-only", commit).decode().splitlines() if p]
    areas = Counter(path.split("/", 1)[0] for path in paths)
    registry = json.loads(source_bytes(lab, commit, "authority/definitions/registry.json"))
    current_refs = set(registry["current_lookup"].values())
    current = [entry for entry in registry["entries"]
               if f"{entry['definition_id']}@{entry['version']}" in current_refs]
    if len(current) != len(current_refs):
        raise ValueError("current Definition lookup does not resolve one-to-one")
    current_rows = [{**file_entry(lab, commit, entry["path"]),
                     "definition_id": entry["definition_id"],
                     "version": entry["version"],
                     "term": entry["term"],
                     "lifecycle_state": entry["lifecycle_state"]}
                    for entry in sorted(current, key=lambda e: (e["term"].casefold(), e["definition_id"]))]
    historical = [entry for entry in registry["entries"]
                  if f"{entry['definition_id']}@{entry['version']}" not in current_refs]
    historical_rows = [{"definition_id": entry["definition_id"],
                        "version": entry["version"],
                        "term": entry["term"],
                        "path": entry["path"],
                        "lifecycle_state": entry["lifecycle_state"]}
                       for entry in sorted(historical, key=lambda e: (e["term"].casefold(), e["definition_id"]))]
    core = [entry for entry in registry["entries"]
            if entry["term"] in CORE_TERMS and
            f"{entry['definition_id']}@{entry['version']}" in current_refs]
    if {entry["term"] for entry in core} != CORE_TERMS:
        raise ValueError("core Definition selection is incomplete or ambiguous")
    core_rows = [{**file_entry(lab, commit, entry["path"]),
                  "definition_id": entry["definition_id"],
                  "version": entry["version"],
                  "term": entry["term"],
                  "lifecycle_state": entry["lifecycle_state"]}
                 for entry in sorted(core, key=lambda e: e["term"])]
    relation_registry = json.loads(source_bytes(
        lab, commit,
        "docs/decisions/0070-definition-complete-lab-model-admission/proposal/relation-kind-registry-postimage.json"))
    relations = [entry for entry in relation_registry["entries"]
                 if entry["relation_kind_ref"] in RELATION_IDS]
    if {entry["relation_kind_ref"] for entry in relations} != RELATION_IDS:
        raise ValueError("relation kind selection is incomplete")
    relation_rows = [{**file_entry(lab, commit, entry["instance_path"]),
                      "relation_kind_ref": entry["relation_kind_ref"],
                      "lifecycle_state": entry["lifecycle_state"],
                      "exact_endpoint_pair_count": entry["exact_endpoint_pair_count"]}
                     for entry in sorted(relations, key=lambda e: e["relation_kind_ref"])]
    groups = {name: [file_entry(lab, commit, path) for path in selected]
              for name, selected in GROUP_PATHS.items()}
    copied = sorted((ARN_ROOT / "authority/artifact-types").rglob("schema.json"))
    copied_rows = []
    for local in copied:
        rel = str(local.relative_to(ARN_ROOT))
        source = file_entry(lab, commit, rel)
        copied_rows.append({"path": rel, "source_sha256": source["sha256"],
                            "byte_current": hashlib.sha256(local.read_bytes()).hexdigest() == source["sha256"]})
    return {
        "schema_version": "arn.lab-asset-inventory/v1",
        "status": "read-only-adoption-audit",
        "authority_effect": "none",
        "source_repository": "cyberAlchemyAI/CyberAlchemy-lab",
        "source_commit": commit,
        "tracked_file_count": len(paths),
        "tracked_area_counts": dict(sorted(areas.items())),
        "lab_definition_registry": {"admitted_versions": len(registry["entries"]),
                                    "current_identities": len(registry["current_lookup"])},
        "all_current_lab_definitions": current_rows,
        "noncurrent_admitted_versions": historical_rows,
        "selected_core_definitions": core_rows,
        "selected_relation_kinds": relation_rows,
        "selected_source_groups": groups,
        "existing_arn_schema_snapshots": copied_rows,
        "claim_ceiling": "Exact selected source bytes and inventory counts at one public Lab commit; no copied authority, runtime adoption, admission or Product effect.",
    }


def render_catalog(result: dict) -> str:
    commit = result["source_commit"]
    lines = [
        "# Current admitted Lab Definitions",
        "",
        "Status: read-only source catalog. Authority effect: none.",
        "",
        f"Source: `cyberAlchemyAI/CyberAlchemy-lab` at `{commit}`. The registry has "
        f"{result['lab_definition_registry']['admitted_versions']} admitted exact versions; "
        f"{result['lab_definition_registry']['current_identities']} identities are current. "
        f"The remaining {len(result['noncurrent_admitted_versions'])} admitted versions are "
        "historical/noncurrent. The 36-record shortlist in [INVENTORY.md](INVENTORY.md) "
        "is a reuse priority, not the full admitted set.",
        "",
        "The current lookup is keyed by identity, so distinct IDs can share a display term. "
        "Each source link below points to the exact pinned version. The complete "
        "[ARN source snapshot](../../../references/cyberalchemy-lab/definitions/README.md) "
        "copies these bytes. Importing a record does not admit it in ARN.",
        "",
        "| Term | Definition identity | Source |",
        "| --- | --- | --- |",
    ]
    for row in result["all_current_lab_definitions"]:
        url = f"https://github.com/cyberAlchemyAI/CyberAlchemy-lab/blob/{commit}/{row['path']}"
        lines.append(f"| {row['term']} | `{row['definition_id']}@{row['version']}` | [record]({url}) |")
    lines += ["", "The exact source paths, hashes, byte lengths and six noncurrent versions are in [source-manifest.json](source-manifest.json).", ""]
    return "\n".join(lines)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--lab-root", type=Path, required=True)
    parser.add_argument("--ref", default="origin/main")
    parser.add_argument("--out", type=Path, default=DEFAULT_OUT)
    parser.add_argument("--catalog-out", type=Path, default=DEFAULT_CATALOG_OUT)
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    result = build(args.lab_root.resolve(), args.ref)
    rendered = json.dumps(result, indent=2, sort_keys=True) + "\n"
    catalog = render_catalog(result)
    if args.check:
        if args.out.read_text() != rendered:
            raise SystemExit("FAIL: Lab asset inventory differs from pinned source")
        if args.catalog_out.read_text() != catalog:
            raise SystemExit("FAIL: Lab Definition catalog differs from pinned source")
        print("PASS: Lab asset inventory matches pinned source")
        return
    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text(rendered)
    args.catalog_out.parent.mkdir(parents=True, exist_ok=True)
    args.catalog_out.write_text(catalog)
    print(f"Wrote {args.out}: {len(result['selected_core_definitions'])} definitions, "
          f"{len(result['selected_relation_kinds'])} relation kinds, "
          f"{len(result['existing_arn_schema_snapshots'])} existing schema snapshots")
    print(f"Wrote {args.catalog_out}: {len(result['all_current_lab_definitions'])} current definitions")


if __name__ == "__main__":
    main()
