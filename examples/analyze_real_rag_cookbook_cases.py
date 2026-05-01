import json
from collections import Counter
from pathlib import Path

rows = [json.loads(line) for line in Path("datasets/external/rag_eval_cookbook_cases.jsonl").read_text(encoding="utf-8").splitlines()]
print({"rows": len(rows), "answerable": Counter(str(r["answerable"]) for r in rows), "avg_overlap": round(sum(r["question_answer_overlap"] for r in rows) / len(rows), 3)})
