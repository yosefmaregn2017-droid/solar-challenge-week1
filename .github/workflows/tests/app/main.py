import streamlit as st

st.set_page_config(page_title="Solar Data Discovery", layout="wide")
st.title("Solar Data Discovery - Yosef Maregn")

st.sidebar.header("Controls")
countries = st.sidebar.multiselect("Choose countries", ["Benin", "Sierra Leone", "Togo"], default=["Benin"])

st.write("This is a placeholder Streamlit app. Replace with visualizations from your notebooks.")
