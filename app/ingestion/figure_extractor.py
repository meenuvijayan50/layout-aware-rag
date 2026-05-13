import pytesseract
from transformers import pipeline


class FigureExtractor:

    def __init__(self):

        pytesseract.pytesseract.tesseract_cmd = (
            r"C:\Program Files\Tesseract-OCR\tesseract.exe"
        )

        # Updated pipeline task
        self.captioner = pipeline(
            "image-text-to-text",
            model="Salesforce/blip-image-captioning-base"
        )

    def extract_text_from_figure(self, image):

        # OCR extraction
        try:

            ocr_text = pytesseract.image_to_string(
                image
            )

        except:

            ocr_text = ""

        # Caption extraction
        try:

            result = self.captioner(image)

            caption = result[0]["generated_text"]

        except:

            caption = ""

        return {
            "ocr_text": ocr_text,
            "caption": caption
        }