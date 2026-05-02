import streamlit as st
from langchain_google_genai import GoogleGenerativeAIEmbeddings


@st.cache_resource(show_spinner=False)
def create_embeddings(api_key):
    return GoogleGenerativeAIEmbeddings(
        model="models/gemini-embedding-001",
        google_api_key=api_key
    )
