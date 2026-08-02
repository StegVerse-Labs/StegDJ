# Chat Music Node Integration

## Goal
Place a StegDJ music node beside ecosystem chat nodes while raw generation remains server-side behind StegMusic. ElevenLabs is an interim provider, not the public contract.

## Required flow
1. The page creates a provider-neutral `chat_music_node` request with a unique request ID, declared target state, governance scope, prompt, and duration.
2. The authenticated server forwards the request to StegMusic. Browser code must not call ElevenLabs directly.
3. StegMusic validates standing and request boundaries, records the composition request, and invokes an authorized provider adapter.
4. The node enters `GENERATING` only after an accepted StegMusic receipt.
5. StegMusic stores returned bytes in governed artifact storage, hashes the artifact, and returns a READY generation receipt plus an authorized artifact URL or short-lived stream token.
6. StegDJ enables playback only when the receipt is READY and request/session binding is valid.
7. BLOCKED, REVIEW_REQUIRED, FAILED, RETRY, and SUPERSEDED states remain visible and must not be converted to READY by UI fallback behavior.

## Security boundary
- `ELEVENLABS_API_KEY` is a server-side secret owned by the eventual deployment service.
- The browser receives neither the key nor a reusable provider authorization header.
- Requests are bound to authenticated StegVerse session identity and `request_id`.
- Artifact URLs should be short-lived or access-controlled; permanent public URLs require an explicit sharing decision.
- Provider errors are mapped into durable StegMusic receipts and surfaced without leaking secrets or raw provider diagnostics.

## UI behavior
The music node is a peer panel on the chat page with:
- prompt input;
- duration control within 3 seconds to 10 minutes;
- instrumental/vocal preference;
- explicit target-state declaration;
- generation status;
- playback and stop controls;
- provenance/receipt disclosure;
- supersede/regenerate control.

The first activation target may support a single generated track. Seamless or effectively endless bass playback requires a later governed queue/extension strategy because one provider request is duration-bounded.

## Provider-neutral endpoints
The page should target a StegMusic service contract such as:
- `POST /api/music/requests` — create governed request;
- `GET /api/music/requests/{request_id}` — retrieve state/receipt;
- `POST /api/music/requests/{request_id}/supersede` — stop and replace;
- `GET /api/music/artifacts/{artifact_id}` — authorized playback or redirect.

These paths are contract candidates until a canonical server host is identified. They must not be installed into an arbitrary page repository without its mirror handoff confirming ownership.

## Integration acceptance
Activation requires all of the following evidence:
- canonical chat-page repository and exact component path identified;
- server endpoint deployed with provider key configured outside source control;
- StegMusic deterministic tests passing;
- request and receipt schemas validated;
- a real provider request succeeds under an authorized paid ElevenLabs account;
- resulting artifact hash and receipt are inspectable;
- the chat-page node plays the authorized artifact without exposing the provider key;
- failure and blocked states are directly observed.

## Canonical continuation
- StegDJ integration state: `docs/STEGDJ_MIRROR_HANDOFF.md`
- StegMusic provider state: `StegVerse-Labs/StegMusic/docs/STEGMUSIC_MIRROR_HANDOFF.md`
