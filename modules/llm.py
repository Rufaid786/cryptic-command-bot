import streamlit as st
from langchain_sambanova import ChatSambaNovaCloud

@st.cache_resource(show_spinner=False)
def create_llm(api_key):
    return ChatSambaNovaCloud(
    model="Meta-Llama-3.2-3B-Instruct",
    max_tokens=1024,
    temperature=0.7,
    top_p=0.01,
    api_key=api_key
)



