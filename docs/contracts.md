# Contracts

## Assumptions

- StegDJ is the governed discovery, playback, and adaptive music orchestration layer.
- It can select existing music or request governed composition from StegMusic.
- It does not decide final data admissibility or own raw music generation.

## Done Definition

This contract is done when every music action can be traced from listener or event intent to admissible data basis, selection or composition request, playback result, and receipt.

## Listener Or Event Intent

Required fields:

- `intent_id`
- `declared_by`
- `authority_ref`
- `listener_scope`
- `environment_id`
- `event_id`
- `current_state_ref`
- `target_state_ref`
- `allowed_music_modes`
- `disallowed_music_modes`
- `validity_window`

## Music Selection Request

Required fields:

- `request_id`
- `intent_ref`
- `catalog_scope`
- `preference_refs`
- `standing_class`
- `admissibility_scope`
- `retention_scope`
- `sharing_state`

## Composition Request To StegMusic

Required fields:

- `request_id`
- `intent_ref`
- `target_state_ref`
- `familiarity_constraints`
- `novelty_constraints`
- `lyric_constraints`
- `instrumentation_constraints`
- `provenance_requirements`
- `compensation_requirements`

## Playback Receipt

Required fields:

- `receipt_id`
- `intent_ref`
- `selection_ref`
- `composition_ref`
- `played_at`
- `environment_id`
- `event_id`
- `result_state_ref`
- `exceptions`

## Refusal Conditions

StegDJ must refuse or fail closed when:

- listener or event intent is not declared;
- target state lacks authority;
- preference or room-state data lacks standing metadata;
- requested music mode exceeds scope;
- composition would require unclear provenance or compensation treatment.
