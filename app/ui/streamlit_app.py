import sys
import os

sys.path.append(
    os.path.abspath(
        os.path.join(
            os.path.dirname(__file__),
            "../.."
        )
    )
)
os.environ["TRANSFORMERS_NO_ADVISORY_WARNINGS"] = "1"

import logging
logging.getLogger("transformers").setLevel(logging.ERROR)

import warnings
warnings.filterwarnings("ignore")

import streamlit as st
import tempfile

from app.ingestion.parser import PDFParser
from app.ingestion.chunker import SemanticChunker
from app.ingestion.metadata_builder import MetadataBuilder
from app.ingestion.figure_extractor import FigureExtractor

from app.retrieval.embeddings import EmbeddingModel
from app.retrieval.vector_store import VectorStore
from app.retrieval.hybrid_retriever import HybridRetriever
from app.retrieval.reranker import Reranker

from app.llm.generator import ResponseGenerator


st.set_page_config(
    page_title="Research Layout-Aware RAG",
    layout="wide"
)

st.title("📘 Research Layout-Aware RAG")


@st.cache_resource
def initialize_pipeline(pdf_path):

    parser = PDFParser(pdf_path)

    pages = parser.extract_pages()

    images = parser.extract_images()

    figure_extractor = FigureExtractor()

    figure_data = []

    for img in images:

        extracted = (
            figure_extractor.extract_text_from_figure(
                img["image"]
            )
        )

        figure_data.append(extracted)

    chunker = SemanticChunker()

    chunks = chunker.chunk_documents(pages)

    metadata_builder = MetadataBuilder()

    chunks = metadata_builder.build_metadata(chunks)

    embedding_model = EmbeddingModel()

    texts = [chunk["text"] for chunk in chunks]

    embeddings = embedding_model.embed_documents(texts)

    vector_store = VectorStore()

    vector_store.insert(
        embeddings,
        chunks
    )

    retriever = HybridRetriever(
        vector_store,
        embedding_model,
        chunks
    )

    reranker = Reranker()

    generator = ResponseGenerator()

    return {
        "retriever": retriever,
        "reranker": reranker,
        "generator": generator,
        "chunks": chunks
    }


uploaded_file = st.file_uploader(
    "Upload PDF",
    type=["pdf"]
)

if uploaded_file:

    with tempfile.NamedTemporaryFile(
        delete=False,
        suffix=".pdf"
    ) as tmp:

        tmp.write(uploaded_file.read())

        pdf_path = tmp.name

    with st.spinner(
        "Building intelligent document index..."
    ):

        pipeline = initialize_pipeline(pdf_path)

    st.success("PDF Processed Successfully")

    query = st.text_input(
        "Ask a research question"
    )

    if query:

        with st.spinner("Retrieving context..."):

            docs = pipeline["retriever"].retrieve(
                query,
                top_k=12
            )

            ranked = pipeline["reranker"].rerank(
                query,
                docs
            )

        with st.spinner("Generating answer..."):

            response = pipeline["generator"].generate(
                query,
                ranked[:6]
            )

        st.subheader("Answer")

        st.write(response)

        st.subheader("Retrieved Evidence")

        for idx, chunk in enumerate(ranked[:6]):

            with st.expander(
                f"Chunk {idx+1} | Page {chunk['metadata']['page']}"
            ):

                st.write(chunk["text"])