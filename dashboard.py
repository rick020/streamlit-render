import streamlit as st

st.set_page_config(page_title="Sample Dashboard", layout="wide")

st.title("Welcome to Your Streamlit Dashboard!")
st.write("This is a simple dashboard deployed on Render.com using uv as the package manager.")

st.header("Sample Chart")
st.line_chart({
    'data': [1, 5, 2, 6, 2, 1]
}) 