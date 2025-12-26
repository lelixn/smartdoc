def split_text(
    text: str,
    chunk_size: int = 500,
    overlap: int = 50
) -> list:
    """
    Splits text into overlapping chunks for embedding.

    Args:
        text (str): Full document text
        chunk_size (int): Number of words per chunk
        overlap (int): Overlapping words between chunks

    Returns:
        List of text chunks
    """
    words = text.split()
    chunks = []

    start = 0
    total_words = len(words)

    while start < total_words:
        end = start + chunk_size
        chunk_words = words[start:end]
        chunk_text = " ".join(chunk_words)

        if chunk_text.strip():
            chunks.append(chunk_text)

        start += chunk_size - overlap

    return chunks
