from sentence_transformers import SentenceTransformer
import numpy as np

import streamlit as st
from sentence_transformers import SentenceTransformer
import numpy as np


@st.cache_resource(show_spinner=False)
def load_embedding_model():
    return SentenceTransformer("all-MiniLM-L6-v2")


_embedding_model = load_embedding_model()


def embed_text(texts: list) -> np.ndarray:
    return _embedding_model.encode(
        texts,
        convert_to_numpy=True,
        show_progress_bar=False
    )


def embed_query(query: str) -> np.ndarray:
    return _embedding_model.encode(
        query,
        convert_to_numpy=True
    )
from sentence_transformers import SentenceTransformer
import numpy as np

# # Load once (IMPORTANT)
# _embedding_model = SentenceTransformer("all-MiniLM-L6-v2")


def embed_text(texts: list) -> np.ndarray:
    """
    Generate embeddings for document chunks.

    Args:
        texts (list): List of text chunks

    Returns:
        numpy.ndarray: Embeddings matrix
    """
    return _embedding_model.encode(
        texts,
        convert_to_numpy=True,
        show_progress_bar=False
    )


def embed_query(query: str) -> np.ndarray:
    """
    Generate embedding for a user query.

    Args:
        query (str): User question

    Returns:
        numpy.ndarray: Query embedding
    """
    return _embedding_model.encode(
        query,
        convert_to_numpy=True
    )

from model.embedder import embed_text, embed_query

docs = ["AI is amazing", "I love programming", "Football is fun"]
doc_vecs = embed_text(docs)
query_vec = embed_query("I like coding")

print(doc_vecs.shape)
print(query_vec.shape)
