from pdf2image import convert_from_path
import pytesseract

POPPLER_PATH = r"D:\SOFTWARES\poppler-25.07.0\Library\bin"
PDF_PATH = r"C:\Users\admin\Downloads\aadhar.pdf"  # change to your file
pytesseract.pytesseract.tesseract_cmd = r"D:\SOFTWARES\tesseract\tesseract.exe"
images = convert_from_path(PDF_PATH, poppler_path=POPPLER_PATH)
for i, img in enumerate(images):
    text = pytesseract.image_to_string(img)
    print(f"--- Page {i+1} ---")
    print(text)
