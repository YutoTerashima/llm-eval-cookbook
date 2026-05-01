from llm_eval_cookbook.batch import BatchCase, grade_batch


def test_grade_batch():
    rows = grade_batch([BatchCase("c1", "exact_match", "yes", " YES ")])
    assert rows[0]["passed"]
