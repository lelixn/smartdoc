# 📘 SmartDoc AI  
<p align="center">
  <img src="https://img.shields.io/badge/Python-3.10+-blue.svg" />
  <img src="https://img.shields.io/badge/PyTorch-ML-red.svg" />
  <img src="https://img.shields.io/badge/HuggingFace-Transformers-yellow.svg" />
  <img src="https://img.shields.io/badge/Streamlit-App-brightgreen.svg" />
  <img src="https://img.shields.io/badge/License-MIT-purple.svg" />
</p>

### AI-Powered Document Intelligence System

📸 UI Preview
<p align="center">
  <img width="1901" height="919" alt="Screenshot 2025-12-27 195701"        src="https://github.com/user-attachments/assets/3ff4f7df-6bc8-420a-b30d-56d74373b5c6" />
</p>

SmartDoc AI is an end-to-end **document intelligence platform** that enables users to upload PDFs, ask natural-language questions, retrieve accurate answers using **semantic search**, and generate concise **AI-powered summaries** — all through a clean, modern web interface.

---

## ✨ Key Features

- 📄 Upload and analyze PDF documents  
- 🧠 Semantic search using transformer embeddings  
- ❓ Context-aware question answering  
- ✍️ Abstractive document summarization  
- 🎨 Polished, modern Streamlit UI  
- ⚡ Efficient PyTorch-based inference  

---

## 🧠 System Architecture

```text
PDF Upload
   ↓
Text Extraction
   ↓
Chunking with Overlap
   ↓
Transformer Embeddings
   ↓
Cosine Similarity Retrieval
   ↓
Question Answering / Summarization
```
🛠️ Tech Stack
| Layer             | Technology                |
| ----------------- | ------------------------- |
| Language          | Python                    |
| ML Framework      | PyTorch                   |
| NLP Models        | Hugging Face Transformers |
| Embeddings        | Sentence Transformers     |
| UI                | Streamlit                 |
| PDF Parsing       | PyPDF2                    |
| Similarity Search | scikit-learn              |
| Deployment        | Streamlit-ready           |

📂 Project Structure
SmartDoc-AI/
│
├── app.py                 # Streamlit application
├── requirements.txt
│
├── model/
│   ├── embedder.py        # Embedding logic
│   ├── qa_model.py        # Question answering pipeline
│   └── summarizer.py      # Summarization pipeline
│
├── utils/
│   ├── pdf_loader.py       # PDF text extraction
│   ├── text_splitter.py    # Text chunking
│   └── semantic_search.py  # Vector similarity search
│
└── assets/                

🚀 Getting Started

```
1️⃣ Clone the Repository
git clone https://github.com/lelixn/SmartDoc-AI.git
cd SmartDoc-AI

2️⃣ Create Virtual Environment (Recommended)
python -m venv venv
venv\Scripts\activate

3️⃣ Install Dependencies
pip install -r requirements.txt

4️⃣ Run the App
streamlit run app.py

Open in browser:
http://localhost:8501
```

## 🤝 Contributing

Contributions are welcome!

If you'd like to improve SmartDoc AI:
1. Fork the repository
2. Create a new branch
3. Make your changes
4. Open a Pull Request

Ideas for contributions:
- UI improvements
- Multi-PDF support
- Vector DB integration
- Deployment automation


🧪 Example Use Cases-
📚 Research paper Q&A
🧾 Legal or policy document exploration
📝 Academic notes summarization
🏢 Enterprise document intelligence

👤 Author
Lelien Panda
📍 Bhubaneswar, Odisha


