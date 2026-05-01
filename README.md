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

## Score Reporting

`llm_eval_cookbook.reporting` summarizes score distributions by grader, which is
useful when turning JSONL eval runs into release notes or model cards.
## Real Public Dataset Experiment

The cookbook now includes `datasets/external/rag_eval_cookbook_cases.jsonl`, derived from
[aizip/Rag-Eval-Dataset-6k](https://huggingface.co/datasets/aizip/Rag-Eval-Dataset-6k). These are
real answerability and grounding cases used to test exact-match, rubric, abstention, and regression
evaluation recipes.

## GPU-Backed Real Experiment

This repository now includes a reproducible GPU-backed experiment using `aizip/Rag-Eval-Dataset-6k`.
The smoke path runs on the local RTX 5090 Laptop GPU through the `Transformers` conda
environment and writes metrics, figures, and a markdown report.

```powershell
conda run -n Transformers python scripts/download_data.py --smoke
conda run -n Transformers python scripts/preprocess_data.py --max-samples 384
conda run -n Transformers python scripts/run_experiment.py --device cuda --smoke
conda run -n Transformers python scripts/make_report.py
```

Main report: `reports/llm_eval_methods_real_data_report.md`.

<!-- V2_RESEARCH_UPGRADE -->
## Publishable V2 Research Upgrade

This repository now includes a project-level V2 experiment suite:

- Reproducible matrix: `configs/experiment_matrix.yaml`
- Main runner: `scripts/run_matrix.py --device cuda --profile full`
- Failure analysis: `scripts/analyze_failures.py`
- Research report: `reports/llm_eval_cookbook_v2_research_report.md`
- Experiment index: `reports/results/experiment_index.json`

The V2 artifacts include multiple experiments, ablations, figures, failure cases, and a discussion section while keeping raw caches and large checkpoints out of Git.

