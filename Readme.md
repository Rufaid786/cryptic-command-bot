# 💬 Cryptic Command Chatbot

An interactive chatbot built with **Streamlit**, **LangChain**, and **Meta LLMs** that helps users understand and interact with **cryptic commands** by retrieving content from URLs.

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
In your project root, create a file named .env and add the following configuration: 
<ul>
    <li>base_url="https://api.sambanova.ai/v1"</li>
    <li>SAMBANOVA_API_KEY="your_actual_api_key_here"</li>
</ul>

Replace "your_actual_api_key_here" with the API key you generated from the SambaNova dashboard.



## Running Locally

####  1. Make sure you are in your virtual environment
If you are not you can do it by following step2 in setup Instructions

####  2. Start your streamlit app
Streamlit run app.py


## 🎥 Demo

As part of this project, we tested several Meta LLaMA models available on SambaNova, in combination with the external embedding model sentence-transformers/all-MiniLM-L6-v2. <br>

<h4>✅ Models Evaluated:</h4>
<ul>
    <li>Meta-Llama-3.1-405B-Instruct</li>
    <li>Meta-Llama-3.1-8B-Instruct</li>
    <li>Meta-Llama-3.2-1B-Instruct</li>
    <li>Meta-Llama-3.2-3B-Instruct</li>
    <li>Meta-Llama-3.3-70B-Instruct</li>
    <li>Meta-Llama-Guard-3-8B</li>
</ul>

<h4>⭐ Models Found Suitable for Our Use Case: </h4>
After evaluating based on response quality, stability, and token limits, the following models were found to best fit our needs: <br>

<ul>
    <li>Meta-Llama-3.3-70B-Instruct</li>
    <li>Meta-Llama-3.1-405B-Instruct</li>
    <li>Meta-Llama-3.1-8B-Instruct</li>
</ul>


<b>
A sample demo here : https://youtu.be/QBDciR0XUz4
</b>






