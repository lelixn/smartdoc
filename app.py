import streamlit as st

from utils.pdf_loader import load_pdf
from utils.text_splitter import split_text
from utils.semantic_search import semantic_search

from model.embedder import embed_text, embed_query
from model.qa_model import answer_question
from model.summarizer import summarize
from utils.vector_store import build_vector_store, load_vector_store
from utils.faiss_search import faiss_search
import os



st.set_page_config(
    page_title="SmartDoc AI",
    page_icon="📘",
    layout="wide"
)


st.markdown("""
<style>
.main {
    background-color: #0e1117;
    color: #fafafa;
}

h1, h2, h3 {
    font-family: 'Segoe UI', sans-serif;
    font-weight: 600;
}

.block-container {
    padding-top: 2rem;
}

input, textarea {
    border-radius: 10px !important;
}

.stButton button {
    background: linear-gradient(90deg, #4f46e5, #9333ea);
    color: white;
    border-radius: 10px;
    padding: 0.6rem 1.2rem;
    font-weight: 600;
    border: none;
}

.stButton button:hover {
    opacity: 0.9;
}

[data-testid="stFileUploader"] {
    border: 1px dashed #4f46e5;
    padding: 1rem;
    border-radius: 12px;
}

.answer-box {
    background: #111827;
    padding: 1.2rem;
    border-radius: 12px;
    border-left: 4px solid #4f46e5;
}
</style>
""", unsafe_allow_html=True)


st.markdown("## 📘 SmartDoc AI")
st.markdown(
    "<span style='color:#9ca3af'>Ask questions, retrieve insights, and summarize documents using AI.</span>",
    unsafe_allow_html=True
)
st.divider()


uploaded_file = st.file_uploader(
    "📄 Upload a PDF document",
    type=["pdf"]
)

if uploaded_file:
    with st.spinner("📄 Reading PDF..."):
        raw_text = load_pdf(uploaded_file)

    if not raw_text.strip():
        st.error("No readable text found in the PDF.")
        st.stop()

    with st.spinner("✂️ Splitting document into chunks..."):
        chunks = split_text(raw_text)

    with st.spinner("🧠 Creating embeddings (runs once)..."):
        doc_embeddings = embed_text(chunks)

    st.success(f"Document processed successfully ({len(chunks)} chunks).")

    
    st.subheader("❓ Ask a Question")
    question = st.text_input("Type your question here")

    if question:
        with st.spinner("🔍 Searching relevant context..."):
            query_embedding = embed_query(question)
            relevant_chunks = semantic_search(
                query_embedding,
                doc_embeddings,
                chunks,
                top_k=3
            )

        combined_context = " ".join(relevant_chunks)

        with st.spinner("🤖 Generating answer..."):
            result = answer_question(
                combined_context,
                question
            )

        st.markdown("### 🧠 Answer")
        st.markdown(
            f"<div class='answer-box'>{result['answer']}</div>",
            unsafe_allow_html=True
        )

        with st.expander("📌 Source Context"):
            st.write(combined_context)

   
    with st.sidebar:
        st.markdown("## ⚙️ Controls")
        st.markdown("Use AI to explore your document.")

        if st.button("📄 Generate Summary"):
            with st.spinner("✍️ Summarizing document..."):
                summary = summarize(raw_text)
            st.markdown("### ✨ Summary")
            st.write(summary)


st.markdown("---")
st.markdown(
    "<center style='color:#6b7280'>Built with ❤️ using PyTorch, Hugging Face & Streamlit</center>",
    unsafe_allow_html=True
)
