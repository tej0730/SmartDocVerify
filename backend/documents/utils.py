import os
import pytesseract
from pdf2image import convert_from_path
from PIL import Image
import cv2
from django.core.files.storage import default_storage

# Set up paths
POPPLER_PATH = r"D:\SOFTWARES\poppler-25.07.0\Library\bin"
pytesseract.pytesseract.tesseract_cmd = r"D:\SOFTWARES\tesseract\tesseract.exe"  # full path to exe

def extract_text_from_file(file_field):
    """
    Extract text from uploaded file (PDF or image).
    Works with Django FileField (file_field is model.file).
    """
    file_path = default_storage.path(file_field.name)
    text = ""

    if file_path.lower().endswith(".pdf"):
        # Convert PDF pages to images with Poppler
        images = convert_from_path(file_path, poppler_path=POPPLER_PATH)
        for img in images:
            text += pytesseract.image_to_string(img)
    else:
        # Handle image (JPG, PNG, etc.)
        img = cv2.imread(file_path)
        if img is None:  # fallback if cv2 can't read
            img = Image.open(file_path)
        text = pytesseract.image_to_string(img)

    return text

def dummy_field_parser(text):
    """Very simple placeholder parser. Later we add regex-based Aadhaar/PAN/DL extraction."""
    data = {}

    if "aadhaar" in text.lower():
        data["aadhaar_number"] = "xxxx xxxx xxxx"
    if "pan" in text.lower():
        data["pan_number"] = "ABCDE1234F"
    if "license" in text.lower():
        data["dl_number"] = "GJ-01-2025-XXXX"

    return data
