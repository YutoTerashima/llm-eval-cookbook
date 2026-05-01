from llm_eval_cookbook.suite import run_recipe_suite


if __name__ == "__main__":
    for record in run_recipe_suite():
        print(record.name, record.score, record.passed)
