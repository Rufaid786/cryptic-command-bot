import os
import streamlit as st
from dotenv import load_dotenv

from modules.loader import load_combined_data
from modules.embedder import create_embeddings
from modules.vectorstore import build_vectorstore
from modules.llm import create_llm
from modules.customprompt import get_custom_prompt
from modules.qa_chain import create_qa_chain

# Load API key
load_dotenv()
google_api_key = os.getenv("GOOGLE_API_KEY")

st.set_page_config(page_title="Cryptic Command Chatbot")
st.title("💬 Cryptic Command Chatbot")

# Chat history
if "history" not in st.session_state:
    st.session_state.history = []

# Load URLs from file
with open("datas/urls.txt") as f:
    urls = [line.strip() for line in f.readlines() if line.strip()]

#PDFs location
pdfs="datas/pdfs"

# Load and process data
full_text = load_combined_data(urls,pdfs)
embeddings = create_embeddings(google_api_key)
vectorstore = build_vectorstore(full_text, embeddings)
retriever = vectorstore.as_retriever()

llm = create_llm(google_api_key)
prompt = get_custom_prompt()
qa_chain = create_qa_chain(llm, retriever, prompt)

# Input
query = st.chat_input("Ask about cryptic commands...")

# History
for q, a in st.session_state.history:
    with st.chat_message("user"):
        st.markdown(q)
    with st.chat_message("assistant"):
        st.markdown(a)

# On Query
if query:
    with st.chat_message("user"):
        st.markdown(query)
    response = qa_chain.run(query)
    with st.chat_message("assistant"):
        st.markdown(response)
    st.session_state.history.append((query, response))
