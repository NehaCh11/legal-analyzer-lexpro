import streamlit as st
import requests

st.title("⚖️ Legal Document Analyzer")

text_input = st.text_area(
    "Paste legal text here:",
    height=300
)

if st.button("Analyze"):
    response = requests.post(
        "http://localhost:8000/analyze/",
        data={"text": text_input}
    )

    results = response.json()

    st.subheader("📄 Document Summary")
    st.write(results["summary"])

    st.subheader("📌 Key Clauses")
    st.write(results["clauses"])

    st.subheader("🔍 Named Entities")
    st.write(results["entities"])
