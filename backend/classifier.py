import os
import joblib

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression

from ocr_engine import extract_text


# =============================
# LOAD DATASET
# =============================

def load_dataset(dataset_path):

    texts = []
    labels = []

    print("Loading dataset...\n")

    for label in os.listdir(dataset_path):

        folder_path = os.path.join(dataset_path, label)

        if not os.path.isdir(folder_path):
            continue

        print("Reading folder:", label)

        for file_name in os.listdir(folder_path):

            file_path = os.path.join(folder_path, file_name)

            try:

                text = extract_text(file_path)

                if len(text.strip()) > 10:

                    texts.append(text)

                    labels.append(label)

                    print("Loaded:", file_name)

            except Exception as e:

                print("Error reading file:", file_name)

                print(e)

    print("\nTotal samples:", len(texts))

    return texts, labels


# =============================
# TRAIN MODEL
# =============================

def train_model(dataset_path):

    texts, labels = load_dataset(dataset_path)

    if len(texts) == 0:

        print("No training data found")

        return

    print("\nTraining model...\n")

    vectorizer = TfidfVectorizer(
        stop_words="english"
    )

    X = vectorizer.fit_transform(texts)

    model = LogisticRegression()

    model.fit(X, labels)

    # save models

    os.makedirs("../models", exist_ok=True)

    joblib.dump(
        model,
        "../models/document_classifier.pkl"
    )

    joblib.dump(
        vectorizer,
        "../models/vectorizer.pkl"
    )

    print("\nModel saved successfully!")


# =============================
# RUN TRAINING
# =============================

if __name__ == "__main__":

    dataset_path = "../dataset"

    train_model(dataset_path)