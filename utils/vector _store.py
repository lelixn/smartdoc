import faiss
import numpy as np
import pickle
import os

INDEX_FILE = "data/faiss.index"
META_FILE = "data/chunks.pkl"


def build_vector_store(embeddings: np.ndarray, chunks: list):
    """
    Create and persist FAISS vector store
    """
    dim = embeddings.shape[1]
    index = faiss.IndexFlatL2(dim)
    index.add(embeddings)

    os.makedirs("data", exist_ok=True)

    faiss.write_index(index, INDEX_FILE)

    with open(META_FILE, "wb") as f:
        pickle.dump(chunks, f)


def load_vector_store():
    """
    Load FAISS index and chunk metadata
    """
    index = faiss.read_index(INDEX_FILE)

    with open(META_FILE, "rb") as f:
        chunks = pickle.load(f)

    return index, chunks
