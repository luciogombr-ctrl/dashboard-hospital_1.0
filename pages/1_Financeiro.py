import streamlit as st

st.set_page_config(
    page_title="Financeiro",
    layout="wide"
)

st.title("💰 Dashboard Financeiro")

st.write("Bem-vindo ao painel financeiro.")

col1, col2, col3 = st.columns(3)

col1.metric("Receita", "R$ 150.000")
col2.metric("Despesas", "R$ 80.000")
col3.metric("Lucro", "R$ 70.000")

st.line_chart({
    "Receitas": [10, 20, 30, 40, 50],
    "Lucros": [5, 10, 15, 20, 25]
})

if st.button("⬅ Voltar"):
    st.switch_page("app.py")
