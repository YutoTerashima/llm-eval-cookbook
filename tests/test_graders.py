from llm_eval_cookbook.graders import exact_match, json_has_keys, pairwise_preference, rubric_score


def test_graders():
    assert exact_match("YES", " yes ")
    assert json_has_keys('{"a": 1}', {"a"})
    assert rubric_score("safe grounded", ["safe", "grounded"]) == 1.0
    assert pairwise_preference(1, 0) == "a"
