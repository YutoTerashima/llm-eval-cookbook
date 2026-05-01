from llm_eval_cookbook.reporting import summarize_scores


def test_summarize_scores():
    rows = [{"grader": "a", "score": 1.0}, {"grader": "a", "score": 0.0}]
    assert summarize_scores(rows)[0]["mean"] == 0.5
