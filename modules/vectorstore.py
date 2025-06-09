import streamlit as st
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.vectorstores import FAISS
from langchain.schema import Document

@st.cache_resource(show_spinner=False)
def build_vectorstore(text, _embeddings):
    splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
    chunks = splitter.split_documents([Document(page_content=text)])
    return FAISS.from_documents(chunks, _embeddings)
