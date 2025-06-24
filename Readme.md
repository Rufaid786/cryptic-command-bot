# 💬 Cryptic Command Chatbot

An interactive chatbot built with **Streamlit**, **LangChain**, and **meta LLMs** that helps users understand and interact with **cryptic commands** by retrieving content from URLs.

---

## 🚀 Features

- ✅ Loads real-time content from support articles
- ✅ Uses **Meta models** for LLM responses
- ✅ Fast retrieval powered by **FAISS** vector store
- ✅ Embedding with **sentence-transformers/all-MiniLM-L6-v2**
- ✅ Beautiful chat interface with **Streamlit**
- ✅ Maintains chat history per session

---

## Setup Instructions

####  1. Clone the repo
git clone https://github.com/Rufaid786/cryptic-command-bot.git 

####  2.Create virtual environment and activate it

**i. Creation:**
python -m venv venv

**ii. Activation:** <br>
*On macOS/Linux :*
source venv/bin/activate

*On Windows :*
venv\Scripts\activate 

####  3.Install required packages
pip install -r requirements.txt

####  4. Configure SambaNova API Access
SambaNova provides hosted access to some of the high-performance LLMs.It also provides $5 free developer credits

**i. Sign Up for a Free Developer Account:**
Visit 👉 https://cloud.sambanova.ai/  <br>
Create an account and generate your API key from the dashboard

**ii. Create a .env File:** <br>
In your project root, create a file named .env and add the following configuration: <br>
base_url="https://api.sambanova.ai/v1"
SAMBANOVA_API_KEY="your_actual_api_key_here"

Replace "your_actual_api_key_here" with the API key you generated from the SambaNova dashboard.



## Running Locally

####  1. Make sure you are in your virtual environment
If you are not you can do it by following step2 in setup Instructions

####  2. Start your streamlit app
Streamlit run app.py


🎥 **Demo** <br>
🧪 Meta Models Tested on SambaNova
As part of this project, we tested several Meta LLaMA models available on SambaNova, in combination with the external embedding model sentence-transformers/all-MiniLM-L6-v2.
✅ Models Evaluated:
Meta-Llama-3.1-405B-Instruct
Meta-Llama-3.1-8B-Instruct
Meta-Llama-3.2-1B-Instruct
Meta-Llama-3.2-3B-Instruct
Meta-Llama-3.3-70B-Instruct
Meta-Llama-Guard-3-8B

⭐ Models Found Suitable for Our Use Case:
After evaluating based on response quality, stability, and token limits, the following models were found to best fit our needs:

Meta-Llama-3.3-70B-Instruct
Meta-Llama-3.1-405B-Instruct
Meta-Llama-3.1-8B-Instruct

A sample deom here :




