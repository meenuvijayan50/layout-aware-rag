from qdrant_client import QdrantClient
from qdrant_client.models import (
    Distance,
    VectorParams,
    PointStruct
)


class VectorStore:

    def __init__(self):

        self.collection_name = "research_chunks"

        self.client = QdrantClient(":memory:")

        self.client.recreate_collection(
            collection_name=self.collection_name,
            vectors_config=VectorParams(
                size=768,
                distance=Distance.COSINE
            )
        )

    def insert(self, embeddings, chunks):

        points = []

        for idx, embedding in enumerate(embeddings):

            points.append(
                PointStruct(
                    id=idx,
                    vector=embedding,
                    payload=chunks[idx]
                )
            )

        self.client.upsert(
            collection_name=self.collection_name,
            points=points
        )

    def search(self, query_embedding, top_k=10):

        results = self.client.query_points(
            collection_name=self.collection_name,
            query=query_embedding,
            limit=top_k
        )

        return results.points