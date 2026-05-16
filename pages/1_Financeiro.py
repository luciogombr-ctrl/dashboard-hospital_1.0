import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Financeiro",
    page_icon="💰",
    layout="wide"
)

# BOTÃO HOME
st.page_link(
    "app.py",
    label="⬅️ Voltar para Home",
    icon="🏠"
)

st.title("💰 Dashboard Financeiro")

st.markdown("---")

# MÉTRICAS
col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Receita Mensal", "R$ 150.000", "+12%")

with col2:
    st.metric("Despesas", "R$ 90.000", "-5%")

with col3:
    st.metric("Lucro", "R$ 60.000", "+18%")

st.markdown("---")

# DADOS
financeiro = pd.DataFrame({
    "Mês": ["Jan", "Fev", "Mar", "Abr", "Mai", "Jun"],
    "Receita": [100, 120, 140, 130, 150, 170],
    "Despesas": [80, 90, 100, 95, 90, 110]
})

# GRÁFICOS
col1, col2 = st.columns(2)

with col1:
    st.subheader("📈 Receita Mensal")
    st.line_chart(financeiro.set_index("Mês")["Receita"])

with col2:
    st.subheader("📉 Despesas Mensais")
    st.bar_chart(financeiro.set_index("Mês")["Despesas"])

st.markdown("---")

st.subheader("📋 Resumo Financeiro")

st.dataframe(financeiro, use_container_width=True)

st.success("Financeiro atualizado com sucesso.")