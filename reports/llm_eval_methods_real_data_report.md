# LLM Eval Methods Real Data Report

Exact, lexical, embedding, and rubric-style metrics on real RAG evaluation rows.

## Dataset

- Source: `aizip/Rag-Eval-Dataset-6k`
- Config: `default`
- Split: `train`

## Reproducibility

```powershell
conda run -n Transformers python scripts/download_data.py --smoke
conda run -n Transformers python scripts/preprocess_data.py --max-samples 384
conda run -n Transformers python scripts/run_experiment.py --device cuda --smoke
conda run -n Transformers python scripts/make_report.py
```

## Generated Artifacts

- Result JSON: `results/eval_method_summary.json`
- Result CSV: `results/eval_method_scores.csv`
- Figure: `figures/eval_method_distribution.png`

## Result Snapshot

```json
{
  "dataset": "aizip/Rag-Eval-Dataset-6k",
  "rows": 3000,
  "device": {
    "requested_device": "cuda",
    "actual_device": "cuda",
    "cuda_available": true,
    "gpu_name": "NVIDIA GeForce RTX 5090 Laptop GPU",
    "torch_version": "2.10.0+cu128",
    "cuda_runtime": "12.8"
  },
  "mean_exact": 0.0017,
  "mean_lexical_overlap": 0.7598,
  "correlation": 0.0604
}
```

## Failure Analysis

The experiment stores model disagreements, retrieval misses, or policy-risk examples in the result JSON/CSV files when available. These examples are intentionally kept as previews or structured metadata where the source data can contain unsafe or sensitive text.

## Limitations

- Smoke mode prioritizes reproducibility and runtime over leaderboard-scale performance.
- Raw datasets are downloaded to `data/raw/` and are not committed.
- Metrics should be interpreted as portfolio research baselines, not production claims.
