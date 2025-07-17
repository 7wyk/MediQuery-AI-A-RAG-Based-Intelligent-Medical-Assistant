# 🧠 MediQuery AI

**MediQuery AI** is an intelligent chatbot for the medical domain, built using Retrieval-Augmented Generation (RAG). It allows users to upload medical documents (e.g., textbooks, clinical notes), retrieve the most relevant content, and generate accurate answers using a powerful LLM.

---

## 🚀 Features

- 📄 Upload medical PDFs (books, notes, reports)
- 🔍 Chunk and embed documents with Google/BGE embeddings
- 🧠 Store and search vectors in Pinecone
- 🤖 Use Groq’s LLaMA3-70B model for response generation
- ⚡ FastAPI backend for real-time query handling

---

## 🧱 Tech Stack

| Component        | Technology                |
|------------------|----------------------------|
| **LLM**           | Groq API (LLaMA3-70B)       |
| **Embeddings**    | Google Generative AI / BGE |
| **Vector DB**     | Pinecone                   |
| **Framework**     | LangChain                  |
| **Backend**       | FastAPI                    |            |
| **PDF Handling**  | PyMuPDF, LangChain         |

---

## 🔄 RAG Architecture

User Query
↓
Query Embedding → Pinecone Vector DB ← Embedded Chunks ← Chunking ← PDF Upload
↓
Retrieved Documents
↓
RAG Chain (LangChain + Groq API)
↓
Generated Answer

