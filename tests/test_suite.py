from llm_eval_cookbook.suite import run_recipe_suite


def test_recipe_suite_passes():
    records = run_recipe_suite()
    assert len(records) == 3
    assert all(record.passed for record in records)
