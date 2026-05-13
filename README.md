# Layout-Aware Research RAG System

Production-grade layout-aware Retrieval-Augmented Generation (RAG) system for complex research papers, scientific PDFs, and technical documents.

---

# Features

## Layout-Aware PDF Parsing
- Preserves reading order
- Handles multi-column documents
- Extracts structured page blocks
- Maintains semantic continuity

## Semantic Chunking
- Context-preserving chunk generation
- Overlap-aware splitting
- Research-paper optimized chunk sizes

## Figure & Diagram Understanding
- Figure extraction from PDFs
- OCR-based text extraction
- Caption-aware enrichment
- Embedded media metadata support

## Hybrid Retrieval
- Dense vector retrieval
- Metadata-aware search
- High-precision chunk retrieval
- Stateless retrieval pipeline

## Reranking
- Cross-encoder reranking
- Relevance scoring
- Reduced hallucinations
- Improved answer grounding

## LLM Generation
- Ollama integration
- Context-grounded prompting
- Source-aware answer generation
- Citation-friendly responses

## Interactive UI
- Streamlit-based interface
- PDF upload support
- Retrieved chunk inspection
- Metadata visualization

---

# System Architecture

```text
PDF
 ↓
Layout-Aware Parser
 ↓
Semantic Chunker
 ↓
Metadata Enrichment
 ↓
Embedding Generation
 ↓
Qdrant Vector Store
 ↓
Hybrid Retrieval
 ↓
Reranker
 ↓
LLM Generator (Ollama)
 ↓
Final Response + Retrieved Sources
```

---

# Project Structure

```text

│
├── app/
│   ├── ingestion/
│   │   ├── parser.py
│   │   ├── chunker.py
│   │   ├── figure_extractor.py
│   │   └── metadata_builder.py
│   │
│   ├── retrieval/
│   │   ├── embeddings.py
│   │   ├── vector_store.py
│   │   ├── hybrid_retriever.py
│   │   └── reranker.py
│   │
│   ├── llm/
│   │   ├── prompts.py
│   │   └── generator.py
│   │
│   ├── ui/
│   │   └── streamlit_app.py
│   │
│   └── utils/
│       └── helpers.py
│
├── data/
│   └── sample.pdf
│
├── README.md
├── STRATEGY.md
├── requirements.txt
├── main.py
└── .gitignore
```

---

# Tech Stack

| Component | Technology |
|---|---|
| UI | Streamlit |
| PDF Parsing | PyMuPDF |
| Embeddings | SentenceTransformers |
| Vector DB | Qdrant |
| OCR | Tesseract |
| LLM | Ollama |
| Reranking | CrossEncoder |
| NLP | Transformers |

---

# Installation

## Clone Repository

```bash
git clone https://github.com/meenuvijayan50/layout-aware-rag.git

```

---

## Create Virtual Environment

### Windows

```bash
python -m venv .env
.env\Scripts\activate
```

### Linux/Mac

```bash
python3 -m venv .env
source .env/bin/activate
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

# Install Ollama

Install Ollama:

[Ollama Official Website](https://ollama.com?utm_source=chatgpt.com)

Pull required model:

```bash
ollama pull phi3
```

You may also use:

```bash
ollama pull mistral
```

---

# Install Tesseract OCR

Download:

[Tesseract OCR Windows Installer](https://github.com/UB-Mannheim/tesseract/wiki?utm_source=chatgpt.com)

Add Tesseract to PATH.

Verify installation:

```bash
tesseract --version
```

---

# Running the Application

```bash
streamlit run app/ui/streamlit_app.py
```

Application will open at:

```text
http://localhost:8501
```

---

# Workflow

1. Upload research PDF
2. Extract layout-aware text blocks
3. Generate semantic chunks
4. Create embeddings
5. Store vectors in Qdrant
6. Retrieve relevant chunks
7. Rerank retrieved results
8. Generate grounded response
9. Display response + source chunks

---

# Example Queries

- What is the core contribution of the paper?
- Explain the transformer architecture.
- Summarize the experimental results.
- What are the limitations discussed?
- Compare encoder and decoder attention.

---

# Retrieval Features

| Feature | Supported |
|---|---|
| Multi-column PDFs | Yes |
| Figure extraction | Yes |
| OCR support | Yes |
| Semantic chunking | Yes |
| Metadata filtering | Yes |
| Dense retrieval | Yes |
| Reranking | Yes |
| Source inspection | Yes |

---

# QA & Evaluation Strategy

- Manual PDF validation
- Retrieval relevance testing
- Hallucination reduction checks
- Chunk continuity validation
- OCR verification
- Metadata consistency testing

Detailed evaluation available in:

```text
STRATEGY.md
```

---

# Future Improvements

- Table structure extraction
- Multimodal embeddings
- Citation generation
- Agentic retrieval
- Knowledge graph integration
- GPU acceleration
- Multi-document querying

---

# Demo

The Streamlit UI supports:

- Interactive PDF upload
- Question-answering
- Retrieved chunk visualization
- Metadata exploration
- Research-paper analysis

---

# Author

Meenu Vijayan

---

# License

MIT License
