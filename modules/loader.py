import requests
from unstructured.partition.html import partition_html
import streamlit as st

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
            st.warning(f"Failed to fetch {url}: {e}")
    return all_text
