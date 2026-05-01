from __future__ import annotations

from dataclasses import dataclass

from .graders import exact_match, json_has_keys, rubric_score


@dataclass(frozen=True)
class BatchCase:
    case_id: str
    grader: str
    expected: str
    actual: str
    criteria: tuple[str, ...] = ()


def grade_case(case: BatchCase) -> dict[str, object]:
    if case.grader == "exact_match":
        score = 1.0 if exact_match(case.expected, case.actual) else 0.0
    elif case.grader == "json_has_keys":
        score = 1.0 if json_has_keys(case.actual, set(case.criteria)) else 0.0
    elif case.grader == "rubric":
        score = rubric_score(case.actual, list(case.criteria))
    else:
        raise ValueError(f"unknown grader: {case.grader}")
    return {"case_id": case.case_id, "grader": case.grader, "score": score, "passed": score >= 0.8}


def grade_batch(cases: list[BatchCase]) -> list[dict[str, object]]:
    return [grade_case(case) for case in cases]
