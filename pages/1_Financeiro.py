import streamlit as st

st.set_page_config(
    page_title="Financeiro",
    page_icon="💰",
    layout="wide"
)

st.title("💰 Dashboard Financeiro")

st.write("Área financeira do sistema")

st.page_link(
    "app.py",
    label="⬅ Voltar",
    icon="🏠"
)
