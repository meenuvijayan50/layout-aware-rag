# Strategy Log – Layout-Aware Research Document Intelligence System

---

# 1. Project Objective

The objective of this project is to build a research-grade, layout-aware Retrieval-Augmented Generation (RAG) system capable of understanding complex academic PDFs and answering high-precision questions with minimal hallucination.

Traditional RAG systems often fail on scientific documents due to:

- Multi-column layouts
- Floating figures
- Complex tables
- OCR-heavy scanned pages
- Broken reading order
- Fragmented semantic chunking

This project addresses those limitations through:

- Layout-aware ingestion
- Semantic chunking
- Hybrid retrieval
- Metadata-aware indexing
- OCR-enhanced figure understanding
- Cross-encoder reranking
- Grounded response generation

The final system supports:

- Research paper question answering
- Scientific document intelligence
- High-precision semantic retrieval
- Stateless QA workflows
- Explainable retrieval visualization

---

# 2. System Architecture

The system follows a modular Retrieval-Augmented Generation architecture optimized for scientific and technical PDFs.

## High-Level Pipeline

```text
PDF Document
      ↓
Layout-Aware Parser
      ↓
Semantic Chunker
      ↓
Metadata Builder
      ↓
Figure & OCR Extractor
      ↓
Embedding Generator
      ↓
Qdrant Vector Store
      ↓
Hybrid Retriever
      ↓
Cross-Encoder Reranker
      ↓
LLM Generator (Ollama)
      ↓
Streamlit User Interface

# 3. Core Components

| Component | File | Responsibility |
|------------|------|----------------|
| PDF Parser | `app/ingestion/parser.py` | Extracts layout-aware text and images from PDFs while preserving reading order |
| Semantic Chunker | `app/ingestion/chunker.py` | Splits extracted text into semantically meaningful chunks with overlap |
| Metadata Builder | `app/ingestion/metadata_builder.py` | Attaches metadata such as page number, source, and section information |
| Figure Extractor | `app/ingestion/figure_extractor.py` | Extracts figures/images and performs OCR on embedded visual content |
| Embedding Generator | `app/retrieval/embeddings.py` | Generates dense vector embeddings for semantic retrieval |
| Vector Store | `app/retrieval/vector_store.py` | Stores embeddings and metadata inside Qdrant |
| Hybrid Retriever | `app/retrieval/hybrid_retriever.py` | Retrieves relevant chunks using dense semantic search |
| Reranker | `app/retrieval/reranker.py` | Improves retrieval precision using cross-encoder reranking |
| Prompt Templates | `app/llm/prompts.py` | Defines grounding prompts and hallucination-reduction instructions |
| LLM Generator | `app/llm/generator.py` | Generates final grounded answers using Ollama LLMs |
| Streamlit UI | `app/ui/streamlit_app.py` | Provides interactive user interface for document QA |
| Utility Helpers | `app/utils/helpers.py` | Common utility functions and helper methods |

# 4. Project Folder Structure

```text
layout-aware-rag/
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
│   └── bert.pdf
│
├── requirements.txt
├── STRATEGY.md
├── README.md
└── main.py


---

# 5. Design Goals

```md
# 5. Design Goals

The system was designed with the following objectives:

- Preserve scientific document layout integrity
- Maintain semantic continuity during chunking
- Support OCR-enhanced figure understanding
- Reduce hallucinations through grounded generation
- Enable explainable retrieval
- Support fully local deployment
- Ensure modular scalability
- Optimize for stateless research QA

# 6. Why Traditional RAG Fails on Research PDFs

Traditional RAG pipelines struggle with scientific documents because:

- Multi-column layouts break reading order
- Figures interrupt paragraph continuity
- Tables lose semantic structure
- OCR-heavy scans degrade extraction quality
- Fixed chunking splits complete ideas
- Dense retrieval alone misses exact technical terms

These limitations result in:
- Fragmented retrieval
- Missing context
- Hallucinated answers
- Low retrieval precision

This project addresses those problems through layout-aware parsing and hybrid retrieval.

# 7. End-to-End Pipeline

## Step 1 — PDF Ingestion

The parser extracts:
- Ordered text blocks
- Images
- Layout information
- Page metadata

---

## Step 2 — Semantic Chunking

Text is divided into semantically meaningful chunks using overlap-aware recursive splitting.

---

## Step 3 — Metadata Enrichment

Chunks are enriched with:
- Page numbers
- Source references
- Figure associations
- Section information

---

## Step 4 — Embedding Generation

Chunks are converted into dense semantic embeddings.

---

## Step 5 — Vector Storage

Embeddings and metadata are indexed in Qdrant.

---

## Step 6 — Hybrid Retrieval

Relevant chunks are retrieved using semantic similarity.

---

## Step 7 — Reranking

Cross-encoder reranking improves retrieval precision.

---

## Step 8 — Grounded Generation

The LLM generates answers strictly from retrieved evidence.

---

## Step 9 — Interactive Visualization

The Streamlit UI displays:
- Final answers
- Retrieved chunks
- Metadata
- Source traceability

# 8. Retrieval Flow Diagram

```text
User Query
     ↓
Embedding Generation
     ↓
Qdrant Vector Search
     ↓
Top-K Retrieval
     ↓
Cross-Encoder Reranking
     ↓
Context Assembly
     ↓
LLM Generation
     ↓
Final Response


---

# 9. OCR & Figure Intelligence

```md
# 9. OCR & Figure Intelligence

Scientific documents frequently contain critical information inside figures and diagrams.

The system performs:

- Figure extraction
- OCR processing
- Caption extraction
- Figure-text association

OCR is implemented using Tesseract.

Extracted figure text is indexed alongside normal text chunks to improve multimodal retrieval quality.

# 10. Prompt Engineering Strategy

The prompting system enforces grounded generation.

## Prompt Constraints

The LLM is instructed to:

- Use only retrieved evidence
- Avoid unsupported assumptions
- Refuse unsupported answers
- Cite relevant context implicitly

## Example Prompt

```text
You are a research assistant.

Answer ONLY using the provided context.

If the answer is not available in the context, say:
"I could not find sufficient evidence in the document."


---

# 11. Why Hybrid Retrieval Was Used

```md
# 11. Why Hybrid Retrieval Was Used

Dense semantic retrieval is strong for contextual similarity but may miss:

- Exact terminology
- Acronyms
- Scientific notation
- Formula references

Hybrid retrieval improves:
- Recall
- Precision
- Scientific terminology matching

The architecture combines:
- Semantic vector retrieval
- Lexical matching
- Cross-encoder reranking


# 12. Explainability Features

The Streamlit interface exposes:

- Retrieved chunks
- Similarity scores
- Page numbers
- Metadata
- OCR-derived figure text

This enables:
- Retrieval debugging
- Transparency
- Source verification
- Trustworthy QA

# 12. Explainability Features

The Streamlit interface exposes:

- Retrieved chunks
- Similarity scores
- Page numbers
- Metadata
- OCR-derived figure text

This enables:
- Retrieval debugging
- Transparency
- Source verification
- Trustworthy QA

# 13. Error Handling Strategy

The system includes robust exception handling for:

- Missing PDFs
- Empty retrieval results
- OCR failures
- Embedding mismatches
- Qdrant connection issues
- Invalid model configurations

Fallback responses are returned gracefully without crashing the pipeline.

# 14. Scalability Considerations

The architecture is designed to scale through:

- Modular components
- Batched embeddings
- ANN vector search
- Persistent vector storage
- Local inference support

Future deployment can support:
- Distributed indexing
- GPU acceleration
- Multi-user APIs
- Cloud vector databases

# 15. Technology Stack

| Technology | Purpose |
|------------|---------|
| Python | Core application development |
| Streamlit | Interactive UI |
| PyMuPDF | PDF parsing |
| Qdrant | Vector database |
| Sentence Transformers | Embedding generation |
| Ollama | Local LLM inference |
| Tesseract OCR | Figure text extraction |
| Transformers | NLP and reranking |
| Pillow | Image processing |

# 16. Local Deployment Strategy

The system supports fully local execution.

## Local Components

- Local Ollama LLM
- Local Qdrant database
- Local embedding generation
- Local OCR processing

## Benefits

- Privacy preservation
- Offline execution
- Reduced API cost
- Faster experimentation

# 17. Benchmarking Goals

The system was optimized for:

- Retrieval precision
- Semantic continuity
- Low hallucination rate
- Figure comprehension
- Stateless QA quality

Evaluation focused on:
- Research papers
- Technical PDFs
- Figure-heavy documents

# 18. Research-Oriented Improvements

Future upgrades may include:

- LayoutLMv3 integration
- Table structure parsing
- Formula-aware embeddings
- Citation-aware generation
- Vision-language retrieval
- Graph-based document understanding

# 19. Production Readiness

The project emphasizes production-grade engineering through:

- Modular architecture
- Configurable components
- Exception handling
- Retrieval explainability
- Stateless execution
- Local deployment support
- Scalable vector indexing

# 20. Final Summary

This project delivers a research-grade layout-aware document intelligence system optimized for scientific and technical PDFs.

Key strengths include:

- Layout-aware parsing
- Semantic chunking
- OCR-enhanced retrieval
- Hybrid semantic search
- Cross-encoder reranking
- Grounded generation
- Explainable QA

The architecture significantly improves upon traditional RAG systems when handling complex academic documents.