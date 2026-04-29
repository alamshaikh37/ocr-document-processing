from fastapi import FastAPI, File, UploadFile
import shutil
import os
import joblib

from ocr_engine import extract_text
from nlp_extractor import extract_invoice_fields

app = FastAPI()

UPLOAD_FOLDER = "../dataset/uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

model = joblib.load("../models/document_classifier.pkl")
vectorizer = joblib.load("../models/vectorizer.pkl")


@app.get("/")
def home():

    return {"message": "Document AI running"}


@app.post("/analyze-document")
async def analyze_document(file: UploadFile = File(...)):

    path = os.path.join(UPLOAD_FOLDER, file.filename)

    with open(path, "wb") as buffer:

        shutil.copyfileobj(file.file, buffer)

    text = extract_text(path)

    X = vectorizer.transform([text])

    doc_type = model.predict(X)[0]

    result = {

        "document_type": doc_type

    }

    if doc_type == "invoices":

        result.update(

            extract_invoice_fields(text)

        )

    return result