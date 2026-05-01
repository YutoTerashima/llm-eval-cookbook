from llm_eval_cookbook.graders import exact_match, json_has_keys, pairwise_preference, rubric_score


if __name__ == "__main__":
    print("exact", exact_match("Safe", " safe "))
    print("json", json_has_keys('{"answer": "ok", "score": 1}', {"answer", "score"}))
    print("rubric", rubric_score("This answer is safe and grounded.", ["safe", "grounded"]))
    print("pairwise", pairwise_preference(0.8, 0.6))
