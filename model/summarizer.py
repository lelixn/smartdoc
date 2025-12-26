from transformers import pipeline

# Load once for performance
_summarizer = pipeline(
    task="summarization",
    model="facebook/bart-large-cnn",
    framework="pt"
)


def summarize(text: str, max_length=150, min_length=40) -> str:
    """
    Generate abstractive summary for long text.

    Args:
        text (str): Input document text
        max_length (int): Max tokens in summary
        min_length (int): Min tokens in summary

    Returns:
        str: Summary text
    """
    if not text or len(text.strip()) == 0:
        return ""

    # Hugging Face models have max token limits
    text = text[:3000]

    summary = _summarizer(
        text,
        max_length=max_length,
        min_length=min_length,
        do_sample=False
    )

    return summary[0]["summary_text"]
