# Real Dataset Analysis: RAG Eval Cookbook Cases

Source: [aizip/Rag-Eval-Dataset-6k](https://huggingface.co/datasets/aizip/Rag-Eval-Dataset-6k)

This report converts 120 real RAG evaluation rows into reusable cookbook cases.

- Answerable distribution: {'True': 113, 'False': 7}
- Average question/answer lexical overlap: 0.622
- Suggested eval family: answerability, context grounding, abstention, and retrieval diagnosis

Interpretation: the cookbook now has real cases for regression-style LLM evaluation. These rows
are better than toy exact-match samples because they include difficulty and answerability labels.
