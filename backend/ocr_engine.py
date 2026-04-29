import pytesseract
import cv2
import numpy as np
from pdf2image import convert_from_path
import os

# change path if different
pytesseract.pytesseract.tesseract_cmd = r"C:\Users\Alam shaikh\AppData\Local\Programs\Tesseract-OCR\tesseract.exe"

POPPLER_PATH = r"G:\document-ai-system\poppler\Library\bin"


def pdf_to_image(pdf_path):

    pages = convert_from_path(
        pdf_path,
        dpi=200,
        first_page=1,
        last_page=1,
        poppler_path=POPPLER_PATH
    )

    image_path = pdf_path.replace(".pdf", ".png")

    pages[0].save(image_path, "PNG")

    return image_path


def preprocess_image(image_path):

    image = cv2.imread(image_path)

    image = cv2.resize(image, None, fx=2, fy=2)

    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    thresh = cv2.adaptiveThreshold(
        gray,
        255,
        cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
        cv2.THRESH_BINARY,
        11,
        2
    )

    return thresh


def extract_text(file_path):

    if file_path.endswith(".pdf"):

        file_path = pdf_to_image(file_path)

    processed = preprocess_image(file_path)

    text = pytesseract.image_to_string(
        processed,
        config="--oem 3 --psm 6"
    )

    return text