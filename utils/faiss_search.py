import numpy as np


def faiss_search(index, query_embedding, chunks, top_k=3):
    """
    Perform FAISS vector similarity search
    """
    query_embedding = np.array([query_embedding]).astype("float32")

    distances, indices = index.search(query_embedding, top_k)

    return [chunks[i] for i in indices[0]]
