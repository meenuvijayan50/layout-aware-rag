from langchain_text_splitters import (
    RecursiveCharacterTextSplitter
)


class SemanticChunker:

    def __init__(self):

        self.splitter = RecursiveCharacterTextSplitter(
            chunk_size=1200,
            chunk_overlap=250,
            separators=[
                "\n\n",
                "\n",
                ". ",
                " "
            ]
        )

    def chunk_documents(self, pages):

        chunks = []

        for page in pages:

            split_chunks = self.splitter.split_text(
                page["text"]
            )

            for chunk in split_chunks:

                chunks.append({
                    "text": chunk,
                    "page": page["page"]
                })

        return chunks