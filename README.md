# Document Processing and Data Extraction using OCR

## Overview
This project extracts key information from invoices using OCR and Computer Vision.

## Features
- OCR using Tesseract
- Image preprocessing using OpenCV
- Data extraction using Regex
- Streamlit UI

## Technologies Used
- Python
- OpenCV
- Tesseract OCR
- Streamlit

## How to Run
```bash
pip install -r requirements.txt
streamlit run app.py


Output Example
{
"document_type": "invoices"
"invoice_number": "AAEPS5285"
"invoice_date": "28-04-2026"
"due_date": "Not Found"
"total_amount": "3140.00"
"vendor_name": "AIZEL PHARMA PRIVATE LIMITED"
"customer_name": "DUTT CHSL"
"gst_number": "27ABBCA4221G1Z4"
"phone": "8355869658"
} 

Author 
Alam Shaikh
