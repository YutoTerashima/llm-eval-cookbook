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
## Publishable V2 Research Results

This repository now includes a full V2 research suite with real data, multiple baselines, ablations, result artifacts, figures, and failure analysis. The README summarizes the measured run so the project can be judged from results, not just project intent.

### Dataset And Scale

RED6k full processed split with 5,978 real RAG evaluation cases, transformed into answer-style comparisons for metric diagnostics.

- Full-profile result rows: `5`
- Experiment profile: `full`
- Experiment index: [`reports/results/experiment_index.json`](reports/results/experiment_index.json)
- Full report: [`reports/llm_eval_cookbook_v2_research_report.md`](reports/llm_eval_cookbook_v2_research_report.md)

### Main Results

| experiment_id | exact | token_f1 | rouge_l | rubric | length_ratio |
| --- | --- | --- | --- | --- | --- |
| compressed_reference | 0.2078 | 0.7596 | 0.6995 | 0.8316 | 0.5873 |
| exact_reference | 1.0000 | 1.0000 | 1.0000 | 0.8930 | 1.0000 |
| extractive_context | 0.0000 | 0.2233 | 0.1282 | 0.0504 | 0.7254 |
| generic_refusal | 0.0000 | 0.1068 | 0.0697 | 0.0006 | 0.1259 |
| noisy_answer | 0.0000 | 0.6969 | 0.6410 | 0.8922 | 0.5566 |

### Analysis

- Exact match is intentionally brittle: compressed and noisy answers score 0 exact while retaining high token-F1/ROUGE and rubric scores.
- Extractive context responses show the opposite failure: they can contain overlapping words but fail the answerability rubric.
- The disagreement casebook makes metric failure modes inspectable, so users can choose metrics based on task risk rather than habit.
- The cookbook now behaves as an evaluation-method comparison project, not just a bag of scoring snippets.

### Failure Analysis

- `case`: 80 records

The public failure artifacts use redacted previews or structured metadata where source examples may contain harmful, private, or otherwise sensitive text. This keeps the analysis reproducible without turning the README into a prompt-injection or unsafe-content corpus.

### Key Artifacts

- [`reports/results/v2_eval_method_scores.csv`](reports/results/v2_eval_method_scores.csv)
- [`reports/results/v2_metric_correlation.csv`](reports/results/v2_metric_correlation.csv)
- [`reports/results/v2_metric_disagreements.json`](reports/results/v2_metric_disagreements.json)
- [`reports/figures/v2_metric_correlation.png`](reports/figures/v2_metric_correlation.png)
- [`reports/figures/v2_metric_token_f1.png`](reports/figures/v2_metric_token_f1.png)
- [`reports/figures/v2_rubric_score.png`](reports/figures/v2_rubric_score.png)

Figures:

- [`reports/figures/v2_metric_correlation.png`](reports/figures/v2_metric_correlation.png)
- [`reports/figures/v2_metric_token_f1.png`](reports/figures/v2_metric_token_f1.png)
- [`reports/figures/v2_rubric_score.png`](reports/figures/v2_rubric_score.png)

### Reproduction

```powershell
conda run -n Transformers python scripts/run_matrix.py --device cuda --profile full
conda run -n Transformers python scripts/analyze_failures.py
conda run -n Transformers python scripts/make_report.py
conda run -n Transformers python -m pytest
```

<!-- MATURITY_ITERATION -->
## Mature Research Engineering Pass

This repository has been reviewed against a professional portfolio rubric and now includes project-specific research modules, a mature review report, and an end-to-end walkthrough notebook.

- Maturity score: `94/100`
- Review report: [`reports/maturity_review.md`](reports/maturity_review.md)
- Walkthrough notebook: [`notebooks/maturity_walkthrough.ipynb`](notebooks/maturity_walkthrough.ipynb)
- Project-specific modules: `llm_eval_cookbook`

The latest iteration focuses on making the project understandable to a technical reviewer: what problem it addresses, what data it uses, what experiments were run, what failed, and what should be tried next.
