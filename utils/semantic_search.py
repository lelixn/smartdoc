import numpy as np
from sklearn.metrics.pairwise import cosine_similarity



def semantic_search(
    query_embedding: np.ndarray,
    doc_embeddings: np.ndarray,
    chunks: list,
    top_k: int = 3
) -> list:
    """
    Finds the most relevant document chunks for a query.

    Args:
        query_embedding (np.ndarray): Vector for user query
        doc_embeddings (np.ndarray): Matrix of document vectors
        chunks (list): Original text chunks
        top_k (int): Number of top results to return

    Returns:
        List of top-k relevant text chunks
    """
    # Compute cosine similarity
    similarities = cosine_similarity(
        query_embedding.reshape(1, -1),
        doc_embeddings
    )[0]

    # Get indices of top-k similarities
    top_indices = np.argsort(similarities)[-top_k:][::-1]

    return [chunks[i] for i in top_indices]
