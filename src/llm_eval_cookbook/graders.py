from __future__ import annotations

import json


def exact_match(expected: str, actual: str) -> bool:
    return expected.strip().lower() == actual.strip().lower()


def json_has_keys(text: str, required: set[str]) -> bool:
    try:
        data = json.loads(text)
    except json.JSONDecodeError:
        return False
    return required.issubset(data.keys())


def rubric_score(text: str, criteria: list[str]) -> float:
    if not criteria:
        return 1.0
    lowered = text.lower()
    hits = sum(criterion.lower() in lowered for criterion in criteria)
    return hits / len(criteria)


def pairwise_preference(a_score: float, b_score: float) -> str:
    if a_score == b_score:
        return "tie"
    return "a" if a_score > b_score else "b"
