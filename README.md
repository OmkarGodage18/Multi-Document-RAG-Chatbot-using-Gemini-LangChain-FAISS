# Multi-Document-RAG-Chatbot-using-Gemini-LangChain-FAISS
#  Multi-Document RAG Chatbot using Gemini, LangChain & FAISS

A **Retrieval-Augmented Generation (RAG)** based chatbot that enables users to ask natural language questions across **multiple PDF documents** and receive accurate, context-aware responses. The application leverages **Google Gemini 2.5 Flash**, **LangChain**, **FAISS**, **HuggingFace Embeddings**, and **Flask** to build an intelligent document question-answering system.

---

##  Features

-  Supports multiple PDF documents
-  Automatic PDF loading using DirectoryLoader
-  Intelligent text chunking with RecursiveCharacterTextSplitter
-  Semantic search using HuggingFace Embeddings
-  Fast vector similarity search with FAISS
-  Context-aware answers powered by Google Gemini 2.5 Flash
-  Retrieval-Augmented Generation (RAG)
-  Flask-based web interface
-  Secure API key management using environment variables

---

#  Project Architecture

```

Multiple PDF Documents
│
▼
DirectoryLoader
│
▼
RecursiveCharacterTextSplitter
│
▼
HuggingFace Embeddings
│
▼
FAISS Vector Database
│
▼
Retriever
│
▼
Google Gemini 2.5 Flash
│
▼
Flask Web Application
│
▼
User Response

```

---

#  Tech Stack

| Category | Technology |
|----------|------------|
| Programming Language | Python |
| LLM | Google Gemini 2.5 Flash |
| Framework | LangChain |
| Vector Database | FAISS |
| Embedding Model | all-MiniLM-L6-v2 |
| Backend | Flask |
| PDF Loader | DirectoryLoader, PyPDFLoader |
| Environment Variables | python-dotenv |

---

#  Project Structure

```

Multi-Document-RAG-Chatbot/

│── app.py
│── gen_ai.py
│── requirements.txt
│── README.md
│── .gitignore
│── .env.example
│── index.html

```

---

#  Installation

##  Clone Repository

```bash
git clone https://github.com/yourusername/Multi-Document-RAG-Chatbot.git

cd Multi-Document-RAG-Chatbot
```

---

##  Create Virtual Environment

### Windows

```bash
python -m venv venv

venv\Scripts\activate
```

### Linux / macOS

```bash
python3 -m venv venv

source venv/bin/activate
```

---
##  Install Dependencies

```bash
pip install -r requirements.txt
```

---

##  Configure Environment Variables

Create a `.env` file in the project root.

```
GOOGLE_API_KEY=YOUR_GOOGLE_API_KEY
```

> **Important:** Never commit your actual `.env` file to GitHub.

---

##  Add PDF Documents

Place all PDF files inside the `data/` folder.

Example:

```
data/
├── Machine_Learning.pdf
├── Deep_Learning.pdf
└── AI_Notes.pdf
```

---

##  Run the Application

```bash
python app.py
```

Open your browser:

```
http://127.0.0.1:5000/
```

---

# How It Works

1. Loads all PDF documents from the `data/` folder.
2. Splits documents into overlapping text chunks.
3. Generates semantic embeddings using HuggingFace.
4. Stores embeddings in a FAISS vector database.
5. Retrieves the most relevant document chunks.
6. Sends retrieved context to Google Gemini.
7. Returns accurate, context-aware responses.

---


---

#  Skills Demonstrated

- Python Programming
- Retrieval-Augmented Generation (RAG)
- Prompt Engineering
- LangChain
- Google Gemini API
- Vector Databases (FAISS)
- Semantic Search
- HuggingFace Embeddings
- Flask Web Development
- REST API Integration
- Document Question Answering
- Environment Variable Management

---

#  Future Enhancements

- Upload PDFs directly from the web interface
- Persistent FAISS vector database
- Conversation memory
- Multi-user support
- Chat history
- Docker containerization
- AWS deployment
- Authentication and authorization

---

#  Author

**Omkar Vikram Godage**

 Email: omkargodage18@gmail.com


 GitHub: https://github.com/OmkarGodage18

---

#  If you found this project useful, please consider giving it a star!
