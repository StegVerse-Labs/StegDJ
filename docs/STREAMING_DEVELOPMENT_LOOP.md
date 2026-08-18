# StegDJ Streaming Development Loop

Date: 2026-08-18
Adjacent goal: `DJ-SR-001`
Upstream: `StegVerse-Labs/StegMusic/docs/BURNIN_BRIDGES_CASE_STUDY.md`

## Goal

Use traditional music release and streaming services as governed audience-observation surfaces for StegMusic development while preserving StegDJ's existing boundary: StegDJ orchestrates selection, sequencing, playback, experimentation, and feedback; StegMusic owns composition/generation/provenance.

The development target is **sympathetic recognition without reproduction**. A StegDJ program may evoke a familiar musical neighborhood or ensemble tradition through generalized musical-state descriptors, but it must not use an unlicensed copyrighted sample, protected lyric passage, distinctive copied melody/riff, or performer voice replica simply to achieve recognition.

There is no universal `N seconds is royalty-free` rule. Any element that actually requires licensing must move onto an explicit rights/compensation path rather than being shortened to evade licensing.

## Derived lesson from BURNIN' BRIDGES Ai Music

Observed public chronology:

- `BLACK WATER DAMNED` — 2026-04-10.
- `BLACKWATER BILLY` — 2026-04-18.

The breakout track therefore preceded the named character by eight days. A useful product inference is:

`discover resonant musical state -> observe audience -> reinforce successful state -> build persistent identity/world -> test adjacent states`

StegDJ should operationalize that loop rather than assuming the first identity concept must be correct before release.

## State-family model

StegDJ receives a READY StegMusic artifact plus:

- composition receipt;
- sympathetic-recognition profile hash;
- rights basis;
- similarity-gate status;
- provenance record;
- publication authorization;
- compensation obligations;
- candidate's state-family ID.

StegDJ groups candidates by **state family**, not by copied source track.

A state family can contain generalized descriptors such as:

- tempo and meter;
- groove topology;
- instrumentation families;
- orchestration density;
- timbral envelope;
- harmonic behavior;
- form topology;
- dynamic contour;
- spatial production grammar;
- affective descriptors;
- broad genre/era grammar.

## Release cohort

A release cohort is a governed experiment containing multiple independently generated candidates.

Required cohort record:

- cohort ID;
- state-family ID;
- candidate receipt IDs;
- release date/window;
- distributor and destination services;
- canonical artist/project identity;
- experiment hypothesis;
- controlled descriptor mutations;
- approved metrics;
- minimum observation window;
- privacy/analytics restrictions;
- promotion rules;
- stop conditions.

## Traditional streaming services as development surfaces

Permitted role:

- distribution;
- audience discovery;
- public release validation;
- authorized artist/distributor analytics;
- playlist and catalog observations where legitimately available;
- evidence that a state family is or is not producing listener recognition/engagement.

Not permitted by default:

- scraping or downloading streaming audio to create an unlicensed training corpus;
- bypassing platform controls;
- treating another artist's streamed recording as a reusable StegMusic sample;
- fabricating streams, engagement, saves, follows, or playlist signals;
- using user-level analytics beyond the rights and privacy scope granted by the platform/account.

## Observation contract

Normalize each available metric into a time-bound observation rather than treating raw totals as equivalent across platforms.

Potential metrics when legitimately available:

- starts/plays;
- completion or consumption depth;
- skips;
- repeat listening;
- saves/library adds;
- follows attributable to release windows;
- playlist adds;
- shares;
- search/discovery traffic;
- audience retention across follow-on releases;
- cross-platform conversion;
- downstream direct engagement.

Unavailable metrics remain `UNKNOWN`; they must not be inferred as zero.

## Feedback algorithm

1. Select a governed state family.
2. Request multiple independent candidates from StegMusic.
3. Require `READY` plus similarity/provenance/rights gates.
4. Form a release cohort.
5. Distribute through authorized release channels.
6. Observe only legitimate platform/distributor analytics and public metadata.
7. Normalize by platform, audience exposure, release age, and promotion level where data exists.
8. Estimate which descriptor combinations correlate with stronger outcomes.
9. Promote the **descriptor family**, not the source recording.
10. Mutate a bounded subset of descriptors for the next cohort.
11. Preserve the transition and result as a receipt.
12. When a family repeatedly outperforms controls, optionally bind it to a persistent StegMusic/StegDJ identity or narrative world.

## Sympathetic-recognition experiments

### DJ-SR-EXP-001 — Recognition distance

Release candidates at multiple descriptor distances from one generalized musical neighborhood. Measure whether listeners respond similarly even though no copied audio or protected melody/lyrics are used.

### DJ-SR-EXP-002 — Ensemble-part ablation

Hold most descriptors stable and remove one ensemble role at a time: percussion behavior, bass role, harmonic bed, lead role, vocal density, spatial treatment. Determine which minimum subset sustains recognition.

### DJ-SR-EXP-003 — Cross-ensemble synthesis

Combine descriptor families from two or more independently cleared musical neighborhoods while forcing independent melody, lyrics, performance, and recording. Test whether StegMusic can create a new coherent state rather than a collage of source works.

### DJ-SR-EXP-004 — Identity reinforcement

After one state family wins multiple cohorts, attach a persistent project/character/world and compare retention with a control release from the same musical state without the persistent identity.

## Governance states

- `IDLE` — no active cohort.
- `REQUESTED` — candidates requested.
- `GENERATING` — StegMusic generation active.
- `REVIEW_REQUIRED` — rights/similarity/metadata review required.
- `READY` — release candidate cleared for the authorized scope.
- `RELEASED` — distribution receipt exists.
- `OBSERVING` — cohort observation window active.
- `PROMOTED` — state family selected for additional exploration.
- `SUPERSEDED` — replaced by a newer state family/cohort.
- `BLOCKED` — rights, provenance, similarity, platform, or authorization gate failed.
- `FAILED` — operational failure.

## Separation of authorities

StegDJ MUST NOT convert strong audience response into publication authority, licensing authority, or a claim that a similar work is non-infringing. Audience success is development evidence only.

StegMusic remains responsible for generation and expression/provenance gates. Distribution/account authority remains with the authorized release owner. Rights and compensation records remain explicit.

## Next implementation targets

1. Add a machine-readable `release_cohort` schema in StegDJ.
2. Add a `streaming_observation` schema with `UNKNOWN` semantics and platform/time-window binding.
3. Bind `sympathetic_recognition_profile` hashes from StegMusic into the StegDJ chat/music-node contract.
4. Add deterministic validation that unlicensed-reference cohorts cannot contain direct samples or verbatim lyric material.
5. Add receipts for cohort creation, release, observation, promotion, and supersession.
6. Integrate only authorized analytics sources; do not introduce new non-TV/TVC secrets or tokens.
