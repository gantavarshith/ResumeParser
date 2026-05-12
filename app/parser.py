import fitz  
import docx
import easyocr
import io

reader = None

def get_reader():
    global reader
    if reader is None:
        reader = easyocr.Reader(['en'])
    return reader

def extract_pdf_text(file_path: str) -> str:
    text = ""
    try:
        with fitz.open(file_path) as doc:
            for page in doc:
                text += page.get_text()
    except Exception as e:
        print(f"Error reading PDF: {e}")
    return text

def extract_scanned_pdf_text(file_path: str) -> str:
    text = ""
    try:
        ocr_reader = get_reader()
        with fitz.open(file_path) as doc:
            for page in doc:
                pix = page.get_pixmap()
                img_data = pix.tobytes("png")
                results = ocr_reader.readtext(img_data)
                for (bbox, t, prob) in results:
                    text += t + " "
                text += "\n"
    except Exception as e:
        print(f"Error OCRing PDF: {e}")
    return text

def extract_image_text(file_path: str) -> str:
    text = ""
    try:
        ocr_reader = get_reader()
        results = ocr_reader.readtext(file_path)
        for (bbox, t, prob) in results:
            text += t + " "
    except Exception as e:
        print(f"Error OCRing image: {e}")
    return text

def extract_docx_text(file_path: str) -> str:
    text = ""
    try:
        doc = docx.Document(file_path)
        for para in doc.paragraphs:
            text += para.text + "\n"
    except Exception as e:
        print(f"Error reading DOCX: {e}")
    return text
