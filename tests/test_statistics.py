from llm_eval_cookbook.statistics import bootstrap_ci, mean


def test_bootstrap_ci_bounds_mean():
    values = [0, 1, 1, 1]
    lo, hi = bootstrap_ci(values, samples=50)
    assert lo <= mean(values) <= hi
