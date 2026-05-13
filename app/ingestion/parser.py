import fitz
from PIL import Image
import io


class PDFParser:

    def __init__(self, pdf_path):

        self.pdf_path = pdf_path

        self.doc = fitz.open(pdf_path)

    def extract_pages(self):

        pages = []

        for page_num in range(len(self.doc)):

            page = self.doc[page_num]

            # Extract layout-aware blocks
            blocks = page.get_text("blocks")

            # Preserve reading order
            blocks = sorted(
                blocks,
                key=lambda b: (
                    round(b[1] / 10),
                    b[0]
                )
            )

            ordered_text = ""

            for block in blocks:

                text = block[4].strip()

                if text:

                    ordered_text += text + "\n\n"

            pages.append({
                "page": page_num + 1,
                "text": ordered_text
            })

        return pages

    def extract_images(self):

        images = []

        for page_index in range(len(self.doc)):

            page = self.doc[page_index]

            image_list = page.get_images(full=True)

            for img in image_list:

                xref = img[0]

                base_image = self.doc.extract_image(xref)

                image_bytes = base_image["image"]

                image = Image.open(
                    io.BytesIO(image_bytes)
                )

                images.append({
                    "page": page_index + 1,
                    "image": image
                })

        return images