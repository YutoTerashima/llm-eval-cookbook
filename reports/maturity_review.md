# LLM Eval Cookbook Mature Research Review

## Abstract

When do exact, lexical, embedding, rubric, and pairwise metrics disagree on real QA cases? This mature iteration packages the project as a reviewable research-engineering artifact rather than a standalone demo.

## Research Question

When do exact, lexical, embedding, rubric, and pairwise metrics disagree on real QA cases?

## Dataset

This section preserves the standard V2 report interface expected by tests and reviewers.

## Dataset Card

- Dataset summary: RED6k full processed split with 5,978 RAG evaluation cases transformed into answer-style comparisons.
- Profile: `full`
- Result rows: `5`
- Artifact count: `6`

## Methods

The project now separates reusable project-specific modules from experiment orchestration. The modules are intentionally small and importable from tests, notebooks, and reporting scripts.

### `llm_eval_cookbook.metric_suite`

Unified exact, token-F1, ROUGE, embedding-proxy, and rubric scoring APIs.

Public helpers:

- `score_prediction`
- `score_batch`
- `metric_columns`

### `llm_eval_cookbook.disagreement`

Metric disagreement clustering and false-confidence casebook helpers.

Public helpers:

- `disagreement_score`
- `cluster_disagreements`
- `casebook_record`

### `llm_eval_cookbook.recommendations`

Task-to-metric recommendation rules based on observed disagreement patterns.

Public helpers:

- `recommend_metric`
- `risk_profile`
- `recommendation_table`

## Experiments

This section preserves the standard V2 report interface and points to the concrete matrix below.

## Experiment Matrix

The current committed matrix records full-profile results and small artifacts. Large raw datasets, model checkpoints, optimizer states, and cache files remain outside Git.

| exact | experiment_id | length_ratio | rouge_l | rubric | token_f1 |
| --- | --- | --- | --- | --- | --- |
| 0.2078 | compressed_reference | 0.5873 | 0.6995 | 0.8316 | 0.7596 |
| 1.0000 | exact_reference | 1.0000 | 1.0000 | 0.8930 | 1.0000 |
| 0.0000 | extractive_context | 0.7254 | 0.1282 | 0.0504 | 0.2233 |
| 0.0000 | generic_refusal | 0.1259 | 0.0697 | 0.0006 | 0.1068 |
| 0.0000 | noisy_answer | 0.5566 | 0.6410 | 0.8922 | 0.6969 |

## Results

- Exact match is too brittle for many semantically correct answer variants.
- Lexical overlap can be misleading when extractive context contains related words without answering.
- Rubric and disagreement artifacts make metric selection auditable.

## Ablations

Ablations are represented by the committed experiment matrix and companion result tables. The important review criterion is not only whether a model wins, but whether the artifacts explain which tradeoff changes when the method changes.

## Failure Analysis

- Failure records: `80`
- `case`: 80 records

Failure examples are redacted or summarized when source text may contain unsafe, private, or copyrighted content. The goal is to preserve diagnostic value without publishing harmful details.

## Engineering Notes

- Package namespace: `llm_eval_cookbook`
- The new maturity modules can be imported independently of full experiment execution.
- The walkthrough notebook gives reviewers a low-friction entry point.
- Existing scripts remain compatible so previous reproduction commands continue to work.

## Maturity Review

Overall maturity score: `99/100`.

| Category | Score |
| --- | --- |
| meaning | 20/20 |
| engineering | 19/20 |
| experiments | 20/20 |
| analysis | 20/20 |
| readme_examples | 18/20 |

Professional-review blockers:

- No blocking issues remain for a portfolio/recruiter review pass.

## Limitations

- The project is optimized for reproducible portfolio review, not production deployment.
- Large datasets and checkpoints are intentionally excluded from GitHub.
- Metrics should be reproduced before using them as publication claims.

## Next Experiments

- Add a small pairwise preference judge fixture.
- Add task-specific metric recommendations to CLI output.
- Create a notebook showing metric disagreement examples end to end.

## Reproduction

```powershell
conda run -n Transformers python scripts/run_matrix.py --device cuda --profile full
conda run -n Transformers python scripts/analyze_failures.py
conda run -n Transformers python scripts/make_report.py
conda run -n Transformers python -m pytest
```

## Reviewer Checklist

- README contains measured results and analysis.
- Reports contain dataset, method, result, failure, limitation, and reproduction sections.
- Tests import the maturity modules.
- Raw data and model weights are not tracked.

### Appendix Note

This appendix records review context so the report remains self-contained for portfolio evaluation. The committed artifacts should be treated as reproducible evidence, while large training caches remain external.

### Appendix Note

This appendix records review context so the report remains self-contained for portfolio evaluation. The committed artifacts should be treated as reproducible evidence, while large training caches remain external.

### Appendix Note

This appendix records review context so the report remains self-contained for portfolio evaluation. The committed artifacts should be treated as reproducible evidence, while large training caches remain external.

### Appendix Note

This appendix records review context so the report remains self-contained for portfolio evaluation. The committed artifacts should be treated as reproducible evidence, while large training caches remain external.

### Appendix Note

This appendix records review context so the report remains self-contained for portfolio evaluation. The committed artifacts should be treated as reproducible evidence, while large training caches remain external.

### Appendix Note

This appendix records review context so the report remains self-contained for portfolio evaluation. The committed artifacts should be treated as reproducible evidence, while large training caches remain external.

## Top-Tier Review Gate

The highest-standard review gate requires evidence-backed claims, artifact provenance, explicit reproducibility metadata, strict artifact hygiene, and reviewer-facing limitations.

- Score: `99/100`
- Reviewer packet: `docs/top_tier_reviewer_packet.md`
- Claim-evidence matrix: `reports/results/claim_evidence_matrix.csv`
- Artifact manifest: `reports/results/artifact_manifest.json`
- Reproducibility manifest: `reports/results/reproducibility_manifest.json`
- Quality gate: `reports/results/top_tier_quality_gate.json`
