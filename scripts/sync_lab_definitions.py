"""Copy and verify the exact admitted Lab Definition source cut as ARN reference data."""

from __future__ import annotations

import argparse
import hashlib
import json
import subprocess
from pathlib import Path, PurePosixPath


ARN_ROOT = Path(__file__).resolve().parents[1]
SNAPSHOT_ROOT = ARN_ROOT / "references/cyberalchemy-lab/definitions"
SOURCE_COMMIT = "19d860e719d6d65c05bff74b1c7547b3d48defcc"
SOURCE_REPOSITORY = "cyberAlchemyAI/CyberAlchemy-lab"
REGISTRY_PATH = "authority/definitions/registry.json"
SUPPORT_PATHS = (
    "authority/definitions/DEFINITIONS-INDEX.md",
    "authority/definitions/drift-audit.json",
    "authority/artifact-types/definition/v1/schema.json",
    "authority/artifact-types/definition/v2/schema.json",
    "authority/profiles/definition/v1/lifecycle.json",
    "authority/profiles/definition/v1/LIFECYCLE.md",
)


def git_show(lab_root: Path, source_path: str) -> bytes:
    return subprocess.run(
        ["git", "show", f"{SOURCE_COMMIT}:{source_path}"],
        cwd=lab_root, check=True, capture_output=True,
    ).stdout


def safe_path(source_path: str) -> Path:
    parts = PurePosixPath(source_path)
    if parts.is_absolute() or not parts.parts or ".." in parts.parts:
        raise ValueError(f"unsafe source path: {source_path}")
    return Path(*parts.parts)


def digest(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def build(lab_root: Path) -> tuple[dict, dict[str, bytes]]:
    source_commit = subprocess.run(
        ["git", "rev-parse", SOURCE_COMMIT],
        cwd=lab_root, check=True, capture_output=True, text=True,
    ).stdout.strip()
    if source_commit != SOURCE_COMMIT:
        raise ValueError("source commit mismatch")

    registry_bytes = git_show(lab_root, REGISTRY_PATH)
    registry = json.loads(registry_bytes)
    if registry["status"] != "owner-admitted":
        raise ValueError("source registry is not owner-admitted")
    current_lookup = registry["current_lookup"]
    current_refs = set(current_lookup.values())
    if len(registry["entries"]) != 189 or len(current_lookup) != 183:
        raise ValueError("pinned source registry count changed")

    files = {REGISTRY_PATH: registry_bytes}
    rows = []
    seen_refs = set()
    for entry in sorted(registry["entries"], key=lambda e: (e["definition_id"], e["version"])):
        source_path = entry["path"]
        safe_path(source_path)
        if source_path in files:
            raise ValueError(f"duplicate source path: {source_path}")
        ref = f"{entry['definition_id']}@{entry['version']}"
        if ref in seen_refs:
            raise ValueError(f"duplicate Definition version: {ref}")
        seen_refs.add(ref)
        raw = git_show(lab_root, source_path)
        sha = digest(raw)
        if sha != entry["sha256"]:
            raise ValueError(f"registry digest mismatch: {source_path}")
        record = json.loads(raw)
        if (record["definition_id"], record["version"], record["term"]) != (
            entry["definition_id"], entry["version"], entry["term"]
        ):
            raise ValueError(f"registry/record identity mismatch: {source_path}")
        files[source_path] = raw
        rows.append({
            "definition_id": entry["definition_id"],
            "version": entry["version"],
            "term": entry["term"],
            "lifecycle_state_in_lab": entry["lifecycle_state"],
            "current_in_lab": ref in current_refs,
            "source_path": source_path,
            "sha256": sha,
            "bytes": len(raw),
            "admission_decision_ref_in_lab": entry["admission_decision_ref"],
        })
    if len(current_refs - seen_refs) or sum(row["current_in_lab"] for row in rows) != 183:
        raise ValueError("current lookup does not resolve to 183 source records")

    support = []
    for source_path in SUPPORT_PATHS:
        safe_path(source_path)
        raw = git_show(lab_root, source_path)
        files[source_path] = raw
        support.append({"source_path": source_path, "sha256": digest(raw), "bytes": len(raw)})
    manifest = {
        "schema_version": "arn.lab-definition-source-snapshot/v1",
        "status": "read-only-source-snapshot",
        "authority_effect": "none",
        "source_repository": SOURCE_REPOSITORY,
        "source_commit": SOURCE_COMMIT,
        "source_registry_path": REGISTRY_PATH,
        "source_registry_sha256": digest(registry_bytes),
        "current_definition_count": 183,
        "historical_definition_count": 6,
        "definitions": rows,
        "support_files": support,
        "claim_ceiling": "Exact public Lab source bytes at the pinned commit; Lab admission remains scoped to Lab and this snapshot grants no ARN authority.",
    }
    return manifest, files


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--lab-root", required=True, type=Path)
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    manifest, files = build(args.lab_root.resolve())
    manifest_bytes = (json.dumps(manifest, indent=2, sort_keys=True) + "\n").encode()
    expected = {Path("source") / safe_path(path) for path in files}
    actual = {path.relative_to(SNAPSHOT_ROOT) for path in (SNAPSHOT_ROOT / "source").rglob("*") if path.is_file()}
    extras = actual - expected
    if extras:
        raise SystemExit(f"unexpected snapshot source files: {sorted(map(str, extras))[:5]}")
    if args.check:
        if (SNAPSHOT_ROOT / "manifest.json").read_bytes() != manifest_bytes:
            raise SystemExit("snapshot manifest differs from pinned Lab source")
        for source_path, raw in files.items():
            dest = SNAPSHOT_ROOT / "source" / safe_path(source_path)
            if not dest.is_file() or dest.read_bytes() != raw:
                raise SystemExit(f"snapshot file differs: {source_path}")
        print(f"PASS: {len(manifest['definitions'])} exact Definition records, "
              f"{len(manifest['support_files'])} support files, registry and manifest")
        return
    for source_path, raw in files.items():
        dest = SNAPSHOT_ROOT / "source" / safe_path(source_path)
        dest.parent.mkdir(parents=True, exist_ok=True)
        dest.write_bytes(raw)
    SNAPSHOT_ROOT.mkdir(parents=True, exist_ok=True)
    (SNAPSHOT_ROOT / "manifest.json").write_bytes(manifest_bytes)
    print(f"Copied {len(manifest['definitions'])} Definition records, "
          f"{len(manifest['support_files'])} support files and source registry")


if __name__ == "__main__":
    main()
