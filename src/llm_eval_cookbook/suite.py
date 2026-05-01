from __future__ import annotations

from dataclasses import dataclass

from .graders import exact_match, json_has_keys, rubric_score


@dataclass(frozen=True)
class EvalRecord:
    name: str
    score: float
    passed: bool


def run_recipe_suite() -> list[EvalRecord]:
    return [
        EvalRecord("exact_match", 1.0, exact_match("yes", " YES ")),
        EvalRecord("json_schema", 1.0, json_has_keys('{"answer": "ok", "score": 1}', {"answer", "score"})),
        EvalRecord("rubric", rubric_score("safe grounded concise", ["safe", "grounded"]), True),
    ]
