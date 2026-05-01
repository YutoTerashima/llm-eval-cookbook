# LLM Eval Cookbook V2 Research Report

## Abstract

This V2 upgrade turns the repository into a reproducible project-level experiment suite. The run records the dataset, device, experiment matrix, metrics, figures, failure analysis, and reproduction commands in committed small artifacts.

## Dataset

- Source path: `data/processed/rag_cases.jsonl`
- Profile: `full`
- Runtime: `22.165` seconds
- Device: `cuda` / `NVIDIA GeForce RTX 5090 Laptop GPU`

## Methods

Experiments declared in `configs/experiment_matrix.yaml`:

- `exact_match`: `exact`
- `token_f1_rouge`: `lexical`
- `embedding_lsa_similarity`: `lsa`
- `answerability_rubric`: `rubric`

## Experiments

The matrix produced `5` result rows. Best observed `token_f1`: `1.0000` from `exact_reference`.

## Results

Key artifacts:

- `reports\results\v2_eval_method_scores.csv`
- `reports\results\v2_metric_correlation.csv`
- `reports\results\v2_metric_disagreements.json`
- `reports\figures\v2_metric_correlation.png`
- `reports\figures\v2_metric_token_f1.png`
- `reports\figures\v2_rubric_score.png`

## Ablations

Configured ablations: prediction_style, answerability, length_bias, metric_disagreement. The generated ablation files quantify threshold, perturbation, architecture, retrieval, or metric sensitivity depending on the project.

## Failure Analysis

Failure records: `80`.

Top clusters:

- `case`: 80

## Discussion

Evaluation methods disagree for understandable reasons. V2 turns that disagreement into a diagnostic artifact rather than hiding it behind a single aggregate score.

## Limitations

- Full raw caches, model weights, and optimizer states are intentionally excluded from GitHub.
- Results are designed for reproducible portfolio research; they are not production safety, medical, or compliance guarantees.
- Some V2 experiments use compact local artifacts to keep the repository lightweight.

## Reproduction

```powershell
conda run -n Transformers python scripts/run_matrix.py --device cuda --profile full
conda run -n Transformers python scripts/analyze_failures.py
conda run -n Transformers python scripts/make_report.py
conda run -n Transformers python -m pytest
```
