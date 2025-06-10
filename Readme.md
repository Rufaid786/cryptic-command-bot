# 💬 Cryptic Command Chatbot

An interactive chatbot built with **Streamlit**, **LangChain**, and **gemini-2.0-flash** that helps users understand and interact with **cryptic commands** by retrieving content from URLs.

---

## 🚀 Features

- ✅ Loads real-time content from support articles
- ✅ Uses **Google's Gemini 2.0 Flash** for LLM responses
- ✅ Fast retrieval powered by **FAISS** vector store
- ✅ Embedding with **GoogleGenerativeAIEmbeddings**
- ✅ Beautiful chat interface with **Streamlit**
- ✅ Maintains chat history per session

---

## Setup Instructions

####  1. Clone the repo
i.git clone https://github.com/Rufaid786/cryptic-command-bot.git <br>
ii.cd cryptic-chatbot

####  2.Create virtual environment and activate it

**i. Creation:**
python -m venv venv

**ii. Activation:**
On macOS/Linux
source venv/bin/activate

On Windows
venv\Scripts\activate 

####  3.Install required packages
pip install -r requirements.txt

####  4. Add your API key to .env
Create a .env file in the project root and paste the following code in it where your_google_api_key is your model API key  <br>
GOOGLE_API_KEY=your_google_api_key



## Running Locally

####  1. Make sure you are in your virtual environment
If you are not you can do it by following step2 in setup Instructions

####  2. Start your streamlit app
Streamlit run app.py


🎥 **Demo**
We are currently analyzing the LLM's performance timing:<br>
without cache:https://www.youtube.com/watch?v=LE_ix2wCZUI <br>
with cache implemented : https://www.youtube.com/watch?v=Wbza2HFfGFw


**Hosted site**  <br>
https://cryptic-command.streamlit.app/
