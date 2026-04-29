import streamlit as st
import requests

API_URL = "http://127.0.0.1:8000/analyze-document"

st.set_page_config(page_title="Document AI System")

st.title("📄 Document AI System")
st.write("Upload Invoice, Contract, or Report")

uploaded_file = st.file_uploader("Upload Document", type=["pdf", "png", "jpg"])

if uploaded_file is not None:

    st.success("File uploaded successfully")

    if st.button("Analyze Document"):

        files = {
            "file": (
                uploaded_file.name,
                uploaded_file.getvalue(),
                uploaded_file.type
            )
        }

        response = requests.post(API_URL, files=files)

        if response.status_code == 200:

            result = response.json()

            st.subheader("📊 Analysis Result")

            st.json(result)

        else:

            st.error("Error analyzing document")