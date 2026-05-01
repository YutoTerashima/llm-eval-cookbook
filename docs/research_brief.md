# Research Brief

## Problem

LLM projects need more than demos. They need regression tests, schema checks, rubric
scoring, and comparison methods that can be replayed.

## Method

This cookbook implements deterministic graders first, then leaves room for model-judged
rubrics where determinism is not enough.

## Depth Signal

The project shows evaluation design as reusable infrastructure rather than one-off
notebook code.

## Next Experiments

- Add bootstrap confidence intervals.
- Add inter-rater agreement for rubric labels.
- Add JSONL batch evaluation.
