from __future__ import annotations

"""Report metadata for the mature portfolio iteration."""

PROJECT_TITLE = 'LLM Eval Cookbook'
RESEARCH_PROBLEM = 'When do exact, lexical, embedding, rubric, and pairwise metrics disagree on real QA cases?'
DATASET_SUMMARY = 'RED6k full processed split with 5,978 RAG evaluation cases transformed into answer-style comparisons.'
TAKEAWAYS = ['Exact match is too brittle for many semantically correct answer variants.', 'Lexical overlap can be misleading when extractive context contains related words without answering.', 'Rubric and disagreement artifacts make metric selection auditable.']
NEXT_EXPERIMENTS = ['Add a small pairwise preference judge fixture.', 'Add task-specific metric recommendations to CLI output.', 'Create a notebook showing metric disagreement examples end to end.']


def report_outline() -> list[str]:
    return [
        "Abstract",
        "Research question",
        "Dataset card",
        "Methods",
        "Experiment matrix",
        "Results",
        "Ablations",
        "Failure analysis",
        "Engineering notes",
        "Limitations",
        "Reproduction",
    ]


def maturity_claims() -> dict[str, object]:
    return {
        "title": PROJECT_TITLE,
        "problem": RESEARCH_PROBLEM,
        "dataset": DATASET_SUMMARY,
        "takeaways": TAKEAWAYS,
        "next_experiments": NEXT_EXPERIMENTS,
    }
