import streamlit as st

st.set_page_config(
    page_title="Vendas",
    page_icon="📈",
    layout="wide"
)

st.title("📈 Dashboard de Vendas")

st.write("Área de vendas do sistema")

st.page_link(
    "app.py",
    label="⬅ Voltar",
    icon="🏠"
)
