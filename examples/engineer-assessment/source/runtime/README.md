# L0 synthetic vertical slice

Status: **local technical proof only**. It is a separate runtime from the visual Mantine prototype. It binds to `127.0.0.1`, accepts only the exact built-in synthetic media fixture, and uses no browser camera, microphone, participant identity, external vendor, AI scoring or employer route. Do not invite real developers to it. No case or rubric here is reviewed or released.

## Run

From the project root with Python **3.14.4**:

```sh
python3 -m unittest runtime.test_l0 -v
python3 -m runtime.server
```

Open `http://127.0.0.1:5181/`. The server stores SQLite state and synthetic fixture bytes under `data/l0/`, which is gitignored. Stop with Ctrl-C. `EA_L0_PORT` and `EA_L0_DATA_DIR` may change the local port and storage path. No package installation is required: Python standard library is the only B0/L0 runtime dependency. The existing Mantine/Vite dependencies belong to the separate visual prototype and are not part of this slice.

The initial SQLite schema is version 1. An incompatible old data directory fails closed with `SCHEMA_MIGRATION_REQUIRED`; the runtime does not overwrite it. New schema changes need explicit migrations and replay checks.

`python3 -m runtime.worker` performs one idempotent local pass over verified fixture media awaiting a transcript. The page also exposes a manual synthetic transcript trigger so the journey can be walked through interactively. Neither path calls an ASR service.

## Implemented path

1. Create one synthetic Session 1 journey with frozen [case/rubric/notice/policy fixture](fixture.json) SHA-256 and event receipt.
2. Record challenge, optional research and optional contact choices independently. Challenge acceptance is required before start; optional refusal does not block the fixture.
3. Commit `start` to a server deadline 600 seconds later. The prompt route opens only after start. `stop` clamps capture time to the original deadline; recovery returns the same assignment and deadline.
4. Accept only the exact built-in synthetic bytes. Check size/digest and upload window, store a private local blob, then issue a server media receipt. A duplicate idempotency key returns the same receipt.
5. Produce a fixed transcript tied to the verified media, retain two separate immutable synthetic ratings, and build a provisional report only on agreement. Disagreement leaves the anchor pending. Replay verifies the event hash chain, source bytes, transcript and report rebuilt from pinned inputs and ratings.
6. Issue separate pending rights-request receipts. A pending withdrawal immediately blocks new research extract eligibility; a pending deletion holds further processing. Resolution of research withdrawal removes the purpose choice; deletion tombstones the journey, removes media/ratings/report, and keeps a minimal synthetic event trail. Startup removes uncommitted or tombstoned blobs after an interrupted write/deletion.

## Evidence and limits

`python3 -m unittest runtime.test_l0 -v` exercises deadline recovery, purpose refusal, duplicate and invalid uploads, expiry, transcript/rater order, disagreement, restart replay, tampering, research withdrawal, deletion and orphan cleanup. A loopback HTTP smoke check exercises page delivery, journey creation, purpose choice, start and prompt release. These are deterministic engineering checks, not usability, accessibility, privacy compliance, scoring validity or a hiring result.

This slice deliberately has one synthetic case, a fixed transcript and fake media. It does **not** implement real MediaRecorder capture, resumable multipart transfer, ASR, transcript correction, human rating assignment, three released cases, production authentication, purpose-scoped staff access, PostgreSQL/S3, retention scheduling or distributed worker recovery. The current server is single process and single writer. Its SQLite event chain detects local accidental drift/tampering but is not a security-grade external audit log. L1 requires the owner decisions, reviewed cases/rubrics, accessibility and privacy gates, real custody adapters, and permissioned study registration in [the build plan](../software/BUILD-PLAN.md).

## Dependency decision

| L0 need | Selected and pinned | Reconsider when |
| --- | --- | --- |
| HTTP, local database, hashing, test runner | Python 3.14.4 standard library (`http.server`, `sqlite3`, `hashlib`, `unittest`); zero third-party packages | L1 needs concurrent authenticated service, migrations, worker operations or deployment support. |
| Local media mock | Exact fixture bytes in code and private gitignored `data/l0/media/` | Browser capture/resumable transport and object-store custody enter the selected release. |
| Clock | Injected fake clock for tests; server wall clock for manual local flow | Distributed deadlines and server time assurance are exercised. |

The L1 stack candidates remain in [integration stack](../software/INTEGRATION-STACK.md). No vendor/library is selected for production by this runtime proof.
