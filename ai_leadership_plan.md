# AI Leadership Evaluation and Promotion Plan

This document enables a practical "stay-ahead" operating model for this repository.

## 1) North-Star Score

Compute one weekly composite score from these weighted metrics:

- Task success rate (40%)
- Reliability / error-free runs (20%)
- Latency target compliance (15%)
- Cost efficiency (10%)
- User satisfaction (15%)

Formula:

`composite = 0.40*success + 0.20*reliability + 0.15*latency + 0.10*cost + 0.15*satisfaction`

All metric inputs are normalized to 0-100.

## 2) Promotion Gate

A candidate is eligible for promotion only when all are true:

1. Core regression pass rate is 100%
2. Composite score improves over baseline by at least 3.0 points
3. Reliability does not regress
4. Rollback path is available

## 3) Weekly Tournament

Compare baseline and one or more candidates on a fixed scenario suite:

- Core regressions
- Shadow edge cases
- Fresh weekly samples

Use the same timeout, tools, and budget for each system.

## 4) Voice-Assistant Specific Reliability Checks

Before release, verify:

- only one voice output can play at a time
- microphone permission denied/allowed flows are handled
- app can start, stop, and recover cleanly
- logs are human-readable and include failure reasons

## 5) Cadence

- Nightly: run automated scorecard on known scenarios
- Weekly: run tournament and decide promote/hold
- Monthly: red-team failure drills and update scenarios
