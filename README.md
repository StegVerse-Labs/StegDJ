# StegDJ

StegDJ is the governed discovery, playback, and adaptive music orchestration layer for StegVerse environments.

## Role

StegDJ selects, sequences, blends, or requests music for a listener, group, event, or environment. It does not own the raw generation engine and does not make final governance decisions about data standing or admissibility.

## Primary Responsibilities

- Discover music that matches declared listener or event goals.
- Play existing music when generated music is not needed.
- Request new music from StegMusic when an adaptive composition is required.
- Maintain listener-facing controls for mood, state, event, and environment intent.
- Consume only data that is admissible for music adaptation under the applicable governance decision.

## Boundary

StegDJ may infer musical fit, but it must not silently decide the listener's desired state. The target state must come from the listener, event host, event profile, or another authorized governance path.

## Data Standing Dependency

StegDJ relies on a shared StegVerse data-standing method that will later align KnowledgeVault, environmental sensing, listener preference, event-state data, and compensation value across the ecosystem.

Until that method is finalized, StegDJ treats all external data as requiring explicit standing, admissibility, scope, retention, and compensation metadata before use.

## Initial Done State

This repo is initially complete when it defines:

- playback and discovery scope;
- adaptive music request flow into StegMusic;
- listener or event target-state declaration;
- admissible data requirements;
- non-goals that prevent it from becoming a surveillance, generation, or governance engine.
