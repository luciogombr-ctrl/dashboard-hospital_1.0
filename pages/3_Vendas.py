import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Vendas",
    page_icon="📈",
    layout="wide"
)

# BOTÃO HOME
st.page_link(
    "app.py",
    label="⬅️ Voltar para Home",
    icon="🏠"
)

st.title("📈 Dashboard de Vendas")

st.markdown("---")

# MÉTRICAS
col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Vendas do Dia", "320", "+15%")

with col2:
    st.metric("Clientes", "180", "+8%")

with col3:
    st.metric("Faturamento", "R$ 45.000", "+20%")

st.markdown("---")

# DADOS
vendas = pd.DataFrame({
    "Produto": ["Medicamentos", "Equipamentos", "Consultas", "Exames"],
    "Vendas": [150, 80, 120, 90]
})

# GRÁFICOS
col1, col2 = st.columns(2)

with col1:
    st.subheader("📊 Vendas por Categoria")
    st.bar_chart(vendas.set_index("Produto"))

with col2:
    st.subheader("📋 Dados de Vendas")
    st.dataframe(vendas, use_container_width=True)

st.markdown("---")

st.success("Sistema de vendas funcionando normalmente.")