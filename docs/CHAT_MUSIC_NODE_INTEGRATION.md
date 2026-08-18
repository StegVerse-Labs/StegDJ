# Chat Music Node Integration

Updated: 2026-08-18

## Goal

Place a StegDJ music node beside ecosystem chat nodes while raw generation remains governed behind StegMusic.

**StegVerse-native generation is the primary path. Third-party generators are fallback-only and require explicit TV/TVC admission.**

## Required flow

1. The client creates a provider-neutral `chat_music_node` request with a unique request ID, declared target state, governance scope, prompt, duration, and `provider_policy.primary = STEGVERSE_NATIVE`.
2. The authenticated StegVerse server/runtime forwards the bounded request to StegMusic. Browser code does not call a third-party music provider directly.
3. StegMusic validates request/standing boundaries and attempts the credentialless StegVerse-native generator first.
4. A third-party fallback may be attempted only when it is both declared in the request policy and separately admitted by TV/TVC. Native failure alone never authorizes external egress.
5. When sympathetic-recognition analysis is in scope, provider generation success is provisional until the post-generation similarity/reconstruction gate is bound to the receipt.
6. The node enters READY only after the StegMusic receipt is READY, including required recognition evidence when applicable.
7. StegMusic or its canonical artifact/custody owner stores/hashes the artifact and exposes only an authorized playback reference.
8. StegDJ enables playback only when receipt/request/session binding is valid.
9. BLOCKED, REVIEW_REQUIRED, FAILED, RETRY, and SUPERSEDED states remain visible and cannot be upgraded by UI fallback behavior.
10. Affective observations, when enabled, are separately consent-scoped and bind to stimulus receipts; inferred emotion does not grant action/publication/licensing authority.

## Provider precedence

```text
primary: STEGVERSE_NATIVE
native credential requirement: NONE
native network requirement: false
third-party primary allowed: false
known optional fallback adapter: ELEVENLABS
fallback admission authority: TV/TVC
NON-TV/TVC secret/token allowed: false
silent failover: prohibited
```

The presence of an external adapter is capability scaffolding only; it does not mean an external provider is activated or required.

## Recognition evidence binding

`contracts/chat_music_node.schema.json` can bind:

- `state_family_id`;
- `sympathetic_recognition_profile_hash`;
- `sympathetic_recognition_gate_status`;
- `sympathetic_recognition_evidence_hash`.

A `REVIEW_REQUIRED` or `BLOCKED` recognition gate cannot coexist with node READY.

## Affective feedback binding

The node may additionally bind:

- `affective_experiment_id`;
- `affective_observation_refs`;
- `consent_receipt_id`.

StegDJ orchestrates stimulus/observation relationships. StegMusic owns observation semantics and non-diagnostic feature normalization. HIL operational authority remains with its canonical Site/TVC handoffs and is not duplicated here.

## Streaming-development loop

Traditional streaming/release services are observation surfaces, not primary music-generation providers or unlicensed training corpora.

StegDJ supports a credentialless StegVerse-native observation path:

```text
authorized artist/distributor export or bounded public metadata
-> contracts/streaming_observation.schema.json
-> script/ingest_streaming_observation.py
-> canonical observation hash + UNKNOWN-preserving metrics
-> state-family scoring
```

Direct platform APIs are optional convenience integrations only and require TV/TVC-managed authority. Lack of an API credential does not block bounded authorized export ingestion.

## Security and authority boundary

- No provider API key, GitHub token, PAT, or equivalent credential is accepted in music requests.
- TV/TVC owns any external-provider or external-platform credential path.
- Playback authorization must not become provider credential delegation.
- Affective observation does not create medical/psychological fact.
- Streaming engagement does not grant publication/licensing/custody authority.
- Similarity thresholds do not create a legal safe harbor.

## Provider-neutral service contract candidates

A canonical server host may expose bounded paths such as:

- `POST /api/music/requests` — create governed request;
- `GET /api/music/requests/{request_id}` — retrieve state/receipt;
- `POST /api/music/requests/{request_id}/supersede` — stop/replace;
- `GET /api/music/artifacts/{artifact_id}` — authorized playback reference.

These paths remain contract candidates until the canonical host handoff accepts them. Do not install them into an arbitrary page/runtime repository.

## Integration acceptance

Source-level acceptance requires:

- provider policy bound to `STEGVERSE_NATIVE` primary;
- StegMusic native generator/receipt contract available;
- recognition evidence fields bound into the node contract;
- affective stimulus/observation references bound;
- streaming observation import available without platform API dependency;
- deterministic validators/tests installed;
- credential-clean validation path installed.

Live activation additionally requires exact runtime/artifact/playback evidence through the canonical StegVerse runtime/custody chain. Third-party fallback activation, if used, requires separate TV/TVC admission and is never a prerequisite for StegVerse-native operation.

## Canonical continuation

- StegDJ: `docs/STEGDJ_MIRROR_HANDOFF.md`
- StegMusic: `StegVerse-Labs/StegMusic/docs/STEGMUSIC_MIRROR_HANDOFF.md`
- provider precedence/credential authority: `StegVerse-Labs/TVC/docs/PROVIDER_PRECEDENCE_MIRROR_HANDOFF.md`
- sovereign model/runtime (do not duplicate): `StegVerse-002/micro-node-runtime/docs/SOVEREIGN_LOCAL_MODEL_RUNTIME_MIRROR_HANDOFF.md`
- HIL operational continuation: `StegVerse-Labs/Site/docs/HIL_MIRROR_HANDOFF.md`
