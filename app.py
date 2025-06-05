import os
import streamlit as st
from dotenv import load_dotenv

from langchain_google_genai import ChatGoogleGenerativeAI, GoogleGenerativeAIEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.vectorstores import FAISS
from langchain.schema import Document
from langchain.chains import RetrievalQA
from langchain.prompts import PromptTemplate

# 1. Load API Key
load_dotenv()
google_api_key = os.getenv("GOOGLE_API_KEY")

# 2. Streamlit UI
st.set_page_config(page_title="Cryptic Command Chatbot")
st.title("💬 Cryptic Command Chatbot")

# 3. Maintain Chat History in Session State
if "history" not in st.session_state:
    st.session_state.history = []

# 4. Load Knowledge Base
with open("data.txt", "r") as f:
    full_text = f.read()

splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
chunks = splitter.split_documents([Document(page_content=full_text)])

# 5. Embedding Setup
embeddings = GoogleGenerativeAIEmbeddings(
    model="models/text-embedding-004",
    google_api_key=google_api_key
)

# 6. Create VectorStore
vectorstore = FAISS.from_documents(chunks, embeddings)

# 7. Gemini LLM with fix for system message
llm = ChatGoogleGenerativeAI(
    model="gemini-2.0-flash",
    google_api_key=google_api_key,
    convert_system_message_to_human=True
)

# 8. Prompt Template to Focus LLM
custom_prompt = PromptTemplate.from_template(
    """You are an expert in Amadeus cryptic commands. Use the following context to answer questions accurately.
If you don't know the answer, just say you don't know — don't make things up.

Context:
{context}

Question:
{question}
"""
)

# 9. Retrieval QA Chain
retriever = vectorstore.as_retriever()
qa_chain = RetrievalQA.from_chain_type(
    llm=llm,
    retriever=retriever,
    chain_type_kwargs={"prompt": custom_prompt}
)

# 10. Input Box
query = st.chat_input("Ask about Amadeus cryptic commands...")

# 11. Display Chat History
for q, a in st.session_state.history:
    with st.chat_message("user"):
        st.markdown(q)
    with st.chat_message("assistant"):
        st.markdown(a)

# 12. On User Input
if query:
    with st.chat_message("user"):
        st.markdown(query)

    with st.spinner("🤔 Thinking..."):
        response = qa_chain.run(query)

    with st.chat_message("assistant"):
        st.markdown(response)

    st.session_state.history.append((query, response))
