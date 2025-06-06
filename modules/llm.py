from langchain_google_genai import ChatGoogleGenerativeAI

def create_llm(api_key):
    return ChatGoogleGenerativeAI(
        model="gemini-2.0-flash",
        google_api_key=api_key,
        convert_system_message_to_human=True
    )
