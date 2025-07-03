import streamlit as st
from langchain_ollama import OllamaLLM
import os

st.title("🦜🔗 Langchain Quickstart App (Ollama)")


def generate_response(input_text):
    base_url = os.environ.get("OLLAMA_URL", "localhost:11434")
    llm = OllamaLLM(model="gemma:2b", base_url=f"http://{base_url}")
    st.info(llm.invoke(input_text))


with st.form("my_form"):
    text = st.text_area("Enter text:", "What are 3 key advice for learning how to code?")
    submitted = st.form_submit_button("Submit")
    if submitted:
        generate_response(text)