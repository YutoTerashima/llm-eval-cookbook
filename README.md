# LLM Eval Cookbook

A small library of reusable evaluation recipes: exact match, rubric grading,
preference comparison, pairwise ranking, and JSON-schema checks.

## Quick Start

```bash
pip install -e ".[dev]"
python examples/run_eval_recipes.py
pytest
```

## Research Brief

See [`docs/research_brief.md`](docs/research_brief.md) for evaluation design
principles and extension ideas.

## Portfolio Notes

This is the reusable eval toolbox that supports the larger portfolio projects.

## Experiment Artifacts

- Scores: [`reports/eval_recipe_scores.csv`](reports/eval_recipe_scores.csv)
- Analysis: [`reports/eval_recipe_analysis.md`](reports/eval_recipe_analysis.md)

## Batch Evaluation

`llm_eval_cookbook.batch` adds a small batch runner that normalizes exact-match,
JSON-schema, and rubric cases into a shared result format.

## Full Eval Dataset

The cookbook includes 40 eval records in
[`datasets/eval_cases.jsonl`](datasets/eval_cases.jsonl), with generated results
and analysis in [`reports/full_eval_analysis.md`](reports/full_eval_analysis.md).
