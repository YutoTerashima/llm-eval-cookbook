import json
from pathlib import Path


def test_real_rag_cookbook_cases_are_nontrivial():
    rows = [json.loads(line) for line in Path("datasets/external/rag_eval_cookbook_cases.jsonl").read_text(encoding="utf-8").splitlines()]
    assert len(rows) >= 100
    assert any(row["difficulty"] is not None for row in rows)
    assert all(row["source"] == "aizip/Rag-Eval-Dataset-6k" for row in rows)
