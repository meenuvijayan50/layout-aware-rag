from sentence_transformers import SentenceTransformer


class EmbeddingModel:

    def __init__(self):

        self.model = SentenceTransformer(
            "BAAI/bge-base-en-v1.5"
        )

    def embed_documents(self, texts):

        return self.model.encode(
            texts,
            normalize_embeddings=True
        ).tolist()

    def embed_query(self, query):

        return self.model.encode(
            query,
            normalize_embeddings=True
        ).tolist()