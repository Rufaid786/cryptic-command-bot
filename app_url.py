import os
import streamlit as st
from dotenv import load_dotenv
import requests
from unstructured.partition.html import partition_html
from langchain_google_genai import ChatGoogleGenerativeAI, GoogleGenerativeAIEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.vectorstores import FAISS
from langchain.schema import Document
from langchain.chains import RetrievalQA
from langchain.prompts import PromptTemplate

# ---------- Load API Key ----------
load_dotenv()
google_api_key = os.getenv("GOOGLE_API_KEY")

# ---------- Streamlit UI ----------
st.set_page_config(page_title="Cryptic Command Chatbot")
st.title("💬 Cryptic Command Chatbot")

# ---------- Maintain Chat History ----------
if "history" not in st.session_state:
    st.session_state.history = []

# ---------- Cached function to fetch and clean content from URLs ----------
@st.cache_data(show_spinner=False)
def load_data_from_urls(urls):
    all_text = ""
    for url in urls:
        try:
            html = requests.get(url, timeout=10).text
            elements = partition_html(text=html)
            page_text = "\n".join(str(el) for el in elements)
            all_text += page_text + "\n"
        except Exception as e:
            st.warning(f"⚠️ Failed to fetch {url}: {e}")
    return all_text

# ---------- Load knowledge base from URLs ----------
amadeus_urls = [
    "https://servicehub.amadeus.com/c/portal/view-solution/906462/how-to-issue-an-e-ticket-cryptic-",
    "https://servicehub.amadeus.com/c/portal/view-solution/906460/how-to-create-a-group-pnr"
]
full_text = load_data_from_urls(amadeus_urls)

# ---------- Chunk the content ----------
splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
chunks = splitter.split_documents([Document(page_content=full_text)])

# ---------- Embedding model ----------
embeddings = GoogleGenerativeAIEmbeddings(
    model="models/text-embedding-004",
    google_api_key=google_api_key
)

# ---------- Vector store ----------
vectorstore = FAISS.from_documents(chunks, embeddings)

# ---------- Gemini LLM ----------
llm = ChatGoogleGenerativeAI(
    model="gemini-2.0-flash",
    google_api_key=google_api_key,
    convert_system_message_to_human=True
)

# ---------- Prompt template ----------
custom_prompt = PromptTemplate.from_template("""
You are an expert in Amadeus cryptic commands. Use the following context to answer questions accurately.
If you don't know the answer, say you don't know. Never make up an answer.

Context:
{context}

Question:
{question}
""")

# ---------- QA chain ----------
retriever = vectorstore.as_retriever()
qa_chain = RetrievalQA.from_chain_type(
    llm=llm,
    retriever=retriever,
    chain_type_kwargs={"prompt": custom_prompt}
)

# ---------- User Input ----------
query = st.chat_input("Ask about Amadeus cryptic commands...")

# ---------- Display chat history ----------
for q, a in st.session_state.history:
    with st.chat_message("user"):
        st.markdown(q)
    with st.chat_message("assistant"):
        st.markdown(a)

# ---------- Handle new query ----------
if query:
    with st.chat_message("user"):
        st.markdown(query)

    response = qa_chain.run(query)

    with st.chat_message("assistant"):
        st.markdown(response)

    st.session_state.history.append((query, response))
