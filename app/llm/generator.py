import ollama
from app.llm.prompts import SYSTEM_PROMPT


class ResponseGenerator:

    def __init__(self, model_name="phi3"):

        self.model_name = model_name

    def generate(self, query, chunks):

        context = "\n\n".join(
            [chunk["text"] for chunk in chunks]
        )

        prompt = f"""
Question:
{query}

Context:
{context}
"""

        response = ollama.chat(
            model=self.model_name,
            messages=[
                {
                    "role": "system",
                    "content": SYSTEM_PROMPT
                },
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        )

        return response["message"]["content"]