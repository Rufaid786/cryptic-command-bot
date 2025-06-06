from langchain.prompts import PromptTemplate

def get_custom_prompt():
    return PromptTemplate.from_template("""
You are an expert in Amadeus cryptic commands. Use the following context to answer questions accurately.
If you don't know the answer, say you don't know. Never make up an answer.

Context:
{context}

Question:
{question}
""")
