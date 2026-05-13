import uuid


class MetadataBuilder:

    def build_metadata(self, chunks):

        enhanced = []

        for chunk in chunks:

            enhanced.append({
                "id": str(uuid.uuid4()),
                "text": chunk["text"],
                "metadata": {
                    "page": chunk["page"],
                    "source": "research_paper",
                    "chunk_length": len(chunk["text"])
                }
            })

        return enhanced