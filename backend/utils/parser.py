from PyPDF2 import PdfReader
import docx
import pytesseract
from PIL import Image

def parse(file):
    if file.filename.endswith(".pdf"):
        return " ".join([p.extract_text() for p in PdfReader(file.file).pages])
    elif file.filename.endswith(".docx"):
        doc = docx.Document(file.file)
        return " ".join([p.text for p in doc.paragraphs])
    elif file.content_type.startswith("image/"):
        img = Image.open(file.file)
        return pytesseract.image_to_string(img)
    return "Unsupported format"