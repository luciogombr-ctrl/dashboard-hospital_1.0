import streamlit as st

st.set_page_config(
    page_title="Hospital",
    page_icon="🏥",
    layout="wide"
)

st.title("🏥 Dashboard Hospitalar")

st.write("Área hospitalar do sistema")

st.page_link(
    "app.py",
    label="⬅ Voltar",
    icon="🏠"
)
