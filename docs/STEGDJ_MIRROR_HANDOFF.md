# StegDJ Mirror Handoff

## Canonical status

### Goal DJ-CHAT-MUSIC-001 — chat/music integration
- Active goal: expose governed music generation beside ecosystem chat nodes while delegating composition and raw generation to StegMusic.
- Repository / branch: `StegVerse-Labs/StegDJ` / `main`.
- Canonical handoff: this file.
- Canonical owner: StegDJ orchestration-contract lane.
- Claim state: CLAIMED_FOR_INTEGRATION.

### Goal DJ-SR-001 — streaming development loop
- Added: 2026-08-18.
- Active goal: use traditional release/streaming services as governed development-observation surfaces for StegMusic state families while preserving StegDJ's orchestration boundary.
- Upstream design: `StegVerse-Labs/StegMusic/docs/BURNIN_BRIDGES_CASE_STUDY.md`.
- Core principle: promote high-performing generalized **state families**, not copied source recordings.
- Development target: sympathetic recognition without reproduction.
- No `N seconds is royalty-free` assumption is permitted. Material requiring rights must enter an explicit rights/compensation path.

## Authoritative files

### DJ-CHAT-MUSIC-001
- `README.md`
- `contracts/chat_music_node.schema.json` (required)
- `docs/CHAT_MUSIC_NODE_INTEGRATION.md` (required)
- `receipts/DJ-CHAT-MUSIC-001.json` (required)

### DJ-SR-001
- `docs/STREAMING_DEVELOPMENT_LOOP.md`
- `docs/STEGDJ_MIRROR_HANDOFF.md`
- upstream `StegVerse-Labs/StegMusic/contracts/sympathetic_recognition_profile.schema.json`

## Collision boundaries
StegDJ owns orchestration, candidate selection, sequencing, playback, cohort experimentation, state-family scoring, feedback routing, and compensation metadata. It does not own raw synthesis, provider credentials, licensing authority, StegMusic provider adapters, or ungoverned mutation of a Site/chat host.

StegMusic remains responsible for composition/generation/provenance, expression-firewall behavior, sympathetic-recognition profiles, and similarity/reconstruction gates.

No NON-TV/TVC secrets or tokens are to be introduced. TV/TVC remains credential authority.

## Required behavior

### Existing chat/music path
- Present music generation as a peer node, not a client-side direct provider call.
- Send provider-neutral requests to StegMusic.
- Never expose provider authorization in browser code.
- Preserve prompt, target state, governance scope, request ID, composition receipt, provider receipt, provenance, and compensation metadata.
- Playback requires READY plus an authorized artifact URL/stream token.

### Streaming development path
- Accept only READY StegMusic candidates with rights/provenance/similarity evidence.
- Group experiments by `state_family_id`, not source-track identity.
- Form governed release cohorts with explicit hypotheses, controlled descriptor mutations, authorized destinations, metrics, observation windows, promotion rules, and stop conditions.
- Use only authorized artist/distributor analytics and legitimately available public metadata.
- Do not scrape/download streaming audio into an unlicensed training corpus.
- Do not fabricate streams, saves, follows, playlist activity, or other engagement.
- Treat unavailable metrics as `UNKNOWN`, never silently as zero.
- Audience response is development evidence only; it grants no publication, licensing, custody, or legal authority.

## DJ-SR-001 state model
- `IDLE`
- `REQUESTED`
- `GENERATING`
- `REVIEW_REQUIRED`
- `READY`
- `RELEASED`
- `OBSERVING`
- `PROMOTED`
- `SUPERSEDED`
- `BLOCKED`
- `FAILED`

## Development loop
`state family -> independent candidates -> StegMusic gates -> release cohort -> authorized streaming observations -> normalized outcome -> descriptor-family promotion/mutation -> receipt`

The BURNIN' BRIDGES case study motivates a second-stage identity step after a state family materially outperforms controls:

`discover resonant state -> observe audience -> reinforce state -> persistent identity/world`

This is an inference from the public chronology in which `BLACK WATER DAMNED` (2026-04-10) preceded `BLACKWATER BILLY` (2026-04-18).

## Execution inventory

### DJ-CHAT-MUSIC-001 preserved inventory
| Task ID | Destination | State | Next action |
|---|---|---|---|
| DJ-CHAT-MUSIC-001A | `contracts/chat_music_node.schema.json` | CLAIMED_FOR_IMPLEMENTATION | install provider-neutral node schema |
| DJ-CHAT-MUSIC-001B | `docs/CHAT_MUSIC_NODE_INTEGRATION.md` | CLAIMED_FOR_INTEGRATION | install orchestration/security contract |
| DJ-CHAT-MUSIC-001C | ecosystem chat-page repository | BLOCKED | discover canonical page host |
| DJ-CHAT-MUSIC-001D | `receipts/DJ-CHAT-MUSIC-001.json` | MACHINE_OWNED | write after contract validation/host discovery |
| DJ-CHAT-MUSIC-001E | StegMusic provider adapter | MERGED_INTO_CANONICAL_WORKSTREAM | continue through StegMusic handoff |

### DJ-SR-001 inventory
| Task ID | Destination | State | Validation | Next action |
|---|---|---|---|---|
| DJ-SR-001A | `docs/STREAMING_DEVELOPMENT_LOOP.md` | COMPLETE | design installed | maintain with implementation |
| DJ-SR-001B | `contracts/release_cohort.schema.json` | NOT_STARTED | none | install machine-readable cohort contract |
| DJ-SR-001C | `contracts/streaming_observation.schema.json` | NOT_STARTED | none | install platform/time-window observation contract |
| DJ-SR-001D | chat/music-node profile binding | NOT_STARTED | none | bind StegMusic profile hash + gate state |
| DJ-SR-001E | cohort/observation receipts | NOT_STARTED | none | install receipts and validation |
| DJ-SR-001F | authorized analytics adapters | BLOCKED | none | identify authorized platform/distributor interfaces; use TV/TVC authority only |
| DJ-SR-001G | controlled release experiment | BLOCKED | none | requires cleared artifacts, release authority, and live analytics path |

## Cross-repository dependencies
- Composition/generation: `StegVerse-Labs/StegMusic`.
- Sympathetic-recognition contract: `StegVerse-Labs/StegMusic/contracts/sympathetic_recognition_profile.schema.json`.
- UI host remains unresolved until a live repository handoff/contract identifies the canonical ecosystem chat page.
- Deployment and secret authority remains outside browser code and must remain TV/TVC-governed.
- Pertinent release/integration state must eventually propagate to `StegVerse-Labs/Site`, `GCAT-BCAT-Engine/Publisher`, `StegVerse-Labs/admissibility-wiki`, and `StegVerse-002/stegguardian-wiki` when the work reaches release/tagging state.

## Validation
Existing required JSON validation remains applicable to the chat/music contract when installed.

New DJ-SR-001 validation must eventually include:
- JSON-schema validation of release cohorts and streaming observations;
- deterministic `UNKNOWN` handling for missing metrics;
- receipt hash binding to state-family/profile IDs;
- fail-closed rejection of BLOCKED/REVIEW_REQUIRED StegMusic candidates;
- secret scanning proving no non-TV/TVC credentials are introduced;
- fixtures proving strong audience response cannot auto-grant publication/licensing authority.

## Completion rules
Work counts complete only when installed in the correct repository, committed/applied where authority permits, validated through the strongest available path, backed by inspectable evidence, and reflected here. A release appearing on a streaming service or receiving positive engagement is not itself activation proof.

## Percentages

### DJ-CHAT-MUSIC-001 — preserved prior goal state
- Developed files: 1/5 required control/integration files (20%).
- Validation: 0/2 required validation layers (0%).
- Integration: 0/3 required integration layers (0%).
- Goal activation: 5%.

### DJ-SR-001 — reset on new goal
- Planned deliverables currently tracked: 7.
- Developed/installed: 1/7 (14%).
- Validated at strongest intended path: 0/7 (0%).
- Upstream StegMusic contract dependency: installed, downstream binding pending.
- Goal activation: 10%.

## Archive state
DJ-SR-001 is not complete. The goal and remaining tasks are durable in this handoff, but active implementation remains appropriate until cohort/observation contracts, receipt binding, chat-node profile binding, and an authorized analytics/release experiment path are installed or explicitly transferred to active workers.
