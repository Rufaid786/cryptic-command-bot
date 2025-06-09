# modules/loader.py
import requests
import streamlit as st
from unstructured.partition.html import partition_html
from langchain.document_loaders import PyMuPDFLoader
import os

def load_data_from_urls(urls):
    from streamlit import warning
    all_text = ""
    for url in urls:
        try:
            html = requests.get(url, timeout=10).text
            elements = partition_html(text=html)
            page_text = "\n".join(str(el) for el in elements)
            all_text += page_text + "\n"
        except Exception as e:
            warning(f"⚠️ Failed to fetch {url}: {e}")
    return all_text


def load_data_from_pdfs(pdf_dir):
    all_text = ""
    if not os.path.exists(pdf_dir):
        return all_text

    for filename in os.listdir(pdf_dir):
        if filename.endswith(".pdf"):
            loader = PyMuPDFLoader(os.path.join(pdf_dir, filename))
            docs = loader.load()
            all_text += "\n".join([doc.page_content for doc in docs]) + "\n"
    return all_text


@st.cache_data(show_spinner=False)
def load_combined_data(urls, pdf_dir):
    url_text = load_data_from_urls(urls)
    pdf_text = load_data_from_pdfs(pdf_dir)
    return url_text + pdf_text
