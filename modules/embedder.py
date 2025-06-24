import streamlit as st
from langchain_community.embeddings import HuggingFaceEmbeddings


@st.cache_resource(show_spinner=False)
def create_embeddings():
    model_name = "sentence-transformers/all-MiniLM-L6-v2"
    return HuggingFaceEmbeddings(model_name=model_name)
    
