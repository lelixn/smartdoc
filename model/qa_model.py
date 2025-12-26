from transformers import pipeline

# Load once (VERY IMPORTANT for performance)
_qa_pipeline = pipeline(
    task="question-answering",
    model="deepset/roberta-base-squad2",
    framework="pt"
)


def answer_question(context: str, question: str) -> dict:
    """
    Answers a question given relevant document context.

    Args:
        context (str): Retrieved document text
        question (str): User question

    Returns:
        dict: Answer, score, start, end
    """
    if not context or not question:
        return {"answer": "", "score": 0.0}

    result = _qa_pipeline(
        question=question,
        context=context
    )

    return result
