# Lab Definition source snapshot

This directory contains the exact public CyberAlchemy Lab Definition source files from commit [`19d860e719d6d65c05bff74b1c7547b3d48defcc`](https://github.com/cyberAlchemyAI/CyberAlchemy-lab/tree/19d860e719d6d65c05bff74b1c7547b3d48defcc). It copies **189 admitted exact versions**: **183 current identities** plus **six historical/noncurrent versions**. The original source-relative paths are preserved under [`source/`](source/), including files whose Lab home is under `evidence/migrations/`.

The copy includes the [full Lab registry](source/authority/definitions/registry.json), its generated index and drift audit, Definition v1/v2 schemas, and the candidate Definition lifecycle profile and projection. [manifest.json](manifest.json) gives every Definition's ID, version, Lab currentness, source path, SHA-256 and Lab admission decision reference. The [current Definition catalog](../../../docs/lab-asset-adoption/2026-11-01/CURRENT-DEFINITIONS.md) is a readable index.

**Authority effect in ARN: none.** The registry's `owner-admitted` status and each record's Lab admission apply only in the Lab's authority scope. The Definition lifecycle profile remains `candidate-unadmitted`. ARN's [41 local definitions](../../../docs/proposals/agentic-research-network/2026-10-29/model-v1/definitions.json) remain candidates until a separate ARN owner decision. No term-name match or file copy makes one definition a specialization of another.

Treat `source/` as immutable reference data. Reproduce or verify it from a local Lab checkout with the pinned commit:

```sh
python3 scripts/sync_lab_definitions.py --lab-root /path/to/CyberAlchemy-lab --check
```

The next modeling task is an explicit ARN-to-Lab semantic mapping: for each ARN definition, record whether it reuses, specializes, introduces, or leaves open a Lab meaning, with exact IDs and versions. No such mapping or ARN admission is asserted by this snapshot.
