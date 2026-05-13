from rank_bm25 import BM25Okapi
import numpy as np


class HybridRetriever:

    def __init__(
        self,
        vector_store,
        embedding_model,
        chunks
    ):

        self.vector_store = vector_store

        self.embedding_model = embedding_model

        self.chunks = chunks

        tokenized = [
            chunk["text"].split()
            for chunk in chunks
        ]

        self.bm25 = BM25Okapi(tokenized)

    def retrieve(self, query, top_k=10):

        query_embedding = (
            self.embedding_model.embed_query(query)
        )

        dense_results = self.vector_store.search(
            query_embedding,
            top_k=top_k
        )

        dense_chunks = []

        for r in dense_results:

            dense_chunks.append(r.payload)

        bm25_scores = self.bm25.get_scores(
            query.split()
        )

        bm25_indices = np.argsort(
            bm25_scores
        )[::-1][:top_k]

        sparse_chunks = [
            self.chunks[i]
            for i in bm25_indices
        ]

        merged = dense_chunks + sparse_chunks

        unique = []

        seen = set()

        for chunk in merged:

            if chunk["text"] not in seen:

                unique.append(chunk)

                seen.add(chunk["text"])

        return unique[:top_k]