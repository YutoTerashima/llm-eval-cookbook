from __future__ import annotations


def summarize_scores(rows: list[dict]) -> list[dict[str, object]]:
    groups: dict[str, list[float]] = {}
    for row in rows:
        groups.setdefault(row["grader"], []).append(float(row["score"]))
    return [
        {"grader": grader, "cases": len(scores), "mean": round(sum(scores) / len(scores), 3), "min": min(scores), "max": max(scores)}
        for grader, scores in sorted(groups.items())
    ]
