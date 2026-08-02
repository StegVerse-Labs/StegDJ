# StegDJ Mirror Handoff

## Canonical status
- Goal ID: DJ-CHAT-MUSIC-001
- Active goal: expose governed music generation beside ecosystem chat nodes while delegating composition and raw generation to StegMusic.
- Originating session goal: use ElevenLabs as an interim music generator on the same page as ecosystem chat nodes while StegVerse modules are built.
- Repository / branch: `StegVerse-Labs/StegDJ` / `main`
- Canonical handoff: this file
- Claim state: CLAIMED_FOR_INTEGRATION
- Canonical task owner: StegDJ orchestration-contract lane
- Claim created: 2026-08-02T05:41:00-05:00
- Claim expiration / release: release when the UI host is identified, the request contract is committed, and an integration receipt identifies either activated runtime evidence or a precise deployment blocker.

## Authoritative files
- `README.md`
- `docs/STEGDJ_MIRROR_HANDOFF.md`
- `contracts/chat_music_node.schema.json` (required)
- `docs/CHAT_MUSIC_NODE_INTEGRATION.md` (required)
- `receipts/DJ-CHAT-MUSIC-001.json` (required)

## Collision boundaries
This claim owns the StegDJ-side chat-node request, playback, status, and governance contract. It does not own raw synthesis, ElevenLabs credentials, the StegMusic provider adapter, or mutation of an unidentified Site/chat repository.

## Session goal inventory
| Task ID | Destination | State | Validation | Integration | Next action |
|---|---|---|---|---|---|
| DJ-CHAT-MUSIC-001A | `contracts/chat_music_node.schema.json` | CLAIMED_FOR_IMPLEMENTATION | none | none | install provider-neutral node schema |
| DJ-CHAT-MUSIC-001B | `docs/CHAT_MUSIC_NODE_INTEGRATION.md` | CLAIMED_FOR_INTEGRATION | none | none | install orchestration and security contract |
| DJ-CHAT-MUSIC-001C | ecosystem chat-page repository | BLOCKED | none | none | discover canonical page host from live repository contracts |
| DJ-CHAT-MUSIC-001D | `receipts/DJ-CHAT-MUSIC-001.json` | MACHINE_OWNED | pending | pending | write after contract validation and host discovery |
| DJ-CHAT-MUSIC-001E | StegMusic provider adapter | MERGED_INTO_CANONICAL_WORKSTREAM | pending | pending | continue at `StegVerse-Labs/StegMusic/docs/STEGMUSIC_MIRROR_HANDOFF.md` |

## Required behavior
- Present music generation as a peer node on the ecosystem chat page, not as a client-side direct ElevenLabs call.
- Send provider-neutral requests to StegMusic.
- Never expose `ELEVENLABS_API_KEY` or provider authorization in browser code.
- Show deterministic states: IDLE, REQUESTED, GENERATING, READY, BLOCKED, REVIEW_REQUIRED, FAILED, SUPERSEDED.
- Preserve prompt, target state, governance scope, request ID, composition receipt, provider receipt, provenance, and compensation metadata.
- Support playback only after a READY receipt and authorized artifact URL or stream token are returned.

## Cross-repository dependencies
- Composition/generation owner: `StegVerse-Labs/StegMusic`.
- UI host: unresolved and must be discovered before implementation to prevent duplicate page ownership.
- Deployment/secret owner: unresolved server-side service.
- Site/Publisher/wiki propagation is blocked until runtime activation is validated.

## Validation commands
```bash
python -m json.tool contracts/chat_music_node.schema.json >/dev/null
```

## Completed work
- Canonical handoff and integration claim established.
- StegDJ boundary preserved: orchestration and playback, not raw generation.

## Incomplete work
- Chat music node schema.
- Integration contract.
- Canonical UI-host discovery.
- Runtime endpoint, auth/session binding, playback token flow, deployment, and direct observation.
- Machine workflow and receipts.

## Blocker and release condition
`DJ-CHAT-MUSIC-001C` is BLOCKED until a live repository handoff or contract identifies the canonical ecosystem chat-page host. Release condition: an inspectable repository/path owning the active chat-node page and accepting a nonconflicting StegDJ integration.

## Archive conditions
This session may be archived after all unique requirements are committed to this handoff and the StegMusic handoff, with remaining work machine-owned or assigned to precise repository locations.

## Percentages
- Developed files: 1/5 required control/integration files (20%).
- Validation: 0/2 required validation layers (0%).
- Integration: 0/3 required integration layers (0%).
- Goal activation: 5%.
- Session consolidation: 1/3 session goals durably transferred.
