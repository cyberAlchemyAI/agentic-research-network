# Build plan from model to permissioned developer pilot

Status: candidate implementation sequence. No deployment, participant invitation or vendor processing is authorized by this plan. The first real-user target is Layer 1 in [implementation layering](../model/IMPLEMENTATION-LAYERING.md): all three sessions, human-reviewed provisional feedback and a controlled research extract.

| Slice | Build and integration output | Acceptance evidence |
| --- | --- | --- |
| B0 repository/runtime | App/API/worker packages, configuration, database migrations, private object-store adapter, local fake clock and synthetic fixtures. | Local startup and teardown; no secrets or participant data in repository; reproducible fixture journey. |
| B1 identity/purpose | Invite redemption, notice versions, separate purpose choices, pseudonymous participant, rights-request entry, access-role enforcement. | Refused optional research stays out of extract; no answer captured before applicable notice/action; cross-participant access denied. |
| B2 case/session | Three reviewed case/rubric versions, practice flow, assignment manifest, server timer/reveal, state machine and retry receipts. | Three `≤600s` scored slots, exact case/version replay; duplicate/reordered calls and timeout tested. |
| B3 media/transcript | Browser video capture plus approved alternate path, resumable private upload, digest/duration verification, ASR adapter, correction versions. | Interruption/recovery, corrupt media, ASR failure and correction lineage demonstrated; no public object read. |
| B4 scoring/feedback | Pseudonymous rater queue, evidence spans and `0–4/NA/UNK` anchors, optional pinned AI evidence draft in shadow mode, double human ratings/adjudication, report projection with uncertainty and limitation text. | Blind rating check; AI draft kept separate from human judgments; unusual valid and fluent wrong fixture; same pinned inputs replay to same report; no employer action. |
| B5 research/rights | Event ledger, approved cohort dashboard, purpose-filtered extract manifest, withdrawal/deletion propagation and access audit. | Opt-out/withdrawal before and after export, rights response, backup retention exercise and reidentification boundary tested. |
| B6 release trial | Device/accessibility review, security review, dry-run with synthetic participants, staff training and incident rehearsal. | Named owners accept protocol, vendor/region, retention, three case releases, pilot precision/stopping rules and support contact; private invitations can then begin. |

## First pilot release packet

The packet binds exact Git commit/build image, database migration, protocol version, invitation source, notice/choice text, three case and rubric hashes, time/retry rules, media/ASR vendor and region, rater assignments/training, feedback copy, retention schedule, incident route, data-rights test, accessibility review and registered formative E03 and candidate-feedback measures. A dry run uses synthetic records; the real pilot begins only after the required owner decisions exist. Record the first real session as an operational receipt, not as proof of validity.

## Engineering acceptance checks

1. State-machine property tests reject impossible transitions, over-limit duration, extra scored slots and changing pinned versions after `shown`.
2. Authorization tests cover each actor/resource pair, including signed media grants and research-purpose removal.
3. Replay test reconstructs a report from exact case, media/transcript, rubric, scorer and rater versions.
4. Data-rights integration test traces correction, withdrawal, export revocation and deletion across source and derivatives.
5. Browser journey checks keyboard/timer/device/error paths and transcript correction on mobile and desktop.
6. Pilot analytics test reconciles invited, eligible, started, completed, withdrawn, excluded and exported counts without dropping failed sessions.

Stop at B0/L0 if the synthetic flow cannot preserve identity and provenance. Continue to B6/L1 only with reviewed cases and collection decisions. AI scoring can run in shadow mode later, and the first participant report can remain entirely human-reviewed. This keeps the real-user MVP useful while leaving predictive hiring claims to later studies.

## B0/L0 local proof — 2026-10-26

The [synthetic runtime](../runtime/README.md) now exercises one fixture case from assignment through purpose choice, deadline, verified fixture media receipt, fixed transcript, two synthetic ratings, provisional report, rights actions and deterministic replay. It uses loopback HTTP, SQLite, a private local blob directory, an injected fake clock in tests and Python 3.14.4 standard library only. The fixture is **not** an independently reviewed or released Session 1 case; this is a technical B0/L0 subset and does not satisfy L1 case, privacy, accessibility, custody or participant gates. The separate visual prototype remains a depiction, not this runtime's product UI.

## B1/B2 synthetic progression — 2026-10-26

The [three-session pilot domain](../runtime/PILOT-SYNTHETIC.md) adds one-time invites, participant-scoped cookie sessions, separate purpose receipts, exactly three pinned fixture slots, server deadlines, prompt/reveal acknowledgments, same-assignment recovery, resumable exact-fixture part transfer, immutable fixture transcript/correction versions and replay. A separate [synthetic browser capture probe](../runtime/CAPTURE-SPIKE-RESULT.md) passed in one Chromium environment. Loopback HTTP journeys and ten domain tests passed. This does **not** release any authored case, support real recording/ASR, complete B1 staff authorization, or complete B2–B4 acceptance. The [Brazil-only pilot scope](pilot-scope.json) keeps collection disabled until owner decisions.
