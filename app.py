import streamlit as st

from utils.pdf_loader import load_pdf
from utils.text_splitter import split_text
from utils.semantic_search import semantic_search

from model.embedder import embed_text, embed_query
from model.qa_model import answer_question
from model.summarizer import summarize



st.set_page_config(
    page_title="SmartDoc AI",
    page_icon="📘",
    layout="wide"
)

st.title("📘 SmartDoc AI — Advanced Document Intelligence")
st.write("Ask questions, retrieve answers, and summarize documents using AI.")


uploaded_file = st.file_uploader(
    "Upload a PDF document",
    type=["pdf"]
)

if uploaded_file:
    with st.spinner("📄 Reading PDF..."):
        raw_text = load_pdf(uploaded_file)

    if not raw_text.strip():
        st.error("No readable text found in PDF.")
        st.stop()

    with st.spinner("✂️ Splitting document into chunks..."):
        chunks = split_text(raw_text)

    with st.spinner("🧠 Creating embeddings (this runs once)..."):
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

        st.subheader("🧠 Answer")
        st.success(result["answer"])

        with st.expander("📌 Source Context"):
            st.write(combined_context)

    
    st.divider()
    st.subheader("📄 Document Summary")

    if st.button("Generate Summary"):
        with st.spinner("✍️ Summarizing document..."):
            summary = summarize(raw_text)

        st.info(summary)
