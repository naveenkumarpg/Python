from PIL import Image
import pytesseract

class ImageTextExtractor:
    def __init__(self, tesseract_cmd=None):
        if tesseract_cmd:
            pytesseract.pytesseract.tesseract_cmd = tesseract_cmd

    def extract_text(self, image_path):
        try:
            # Open the image file
            img = Image.open(image_path)
            # Use Tesseract to do OCR on the image
            text = pytesseract.image_to_string(img)
            return text
        except Exception as e:
            return str(e)

def detect_text_pytesseract(image_path):
    extractor = ImageTextExtractor()
    extracted_text = extractor.extract_text(image_path)
    return extracted_text
