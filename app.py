import streamlit as st

st.set_page_config(
    page_title="Dashboard Principal",
    page_icon="📊",
    layout="wide"
)

st.title("📊 Dashboard Hospitalar")

st.markdown("---")

st.subheader("Escolha uma área do sistema")

col1, col2, col3 = st.columns(3)

with col1:
    st.page_link(
        "pages/1_Financeiro.py",
        label="💰 Financeiro"
    )

with col2:
    st.page_link(
        "pages/2_Hospital.py",
        label="🏥 Hospital"
    )

with col3:
    st.page_link(
        "pages/3_Vendas.py",
        label="📈 Vendas"
    )

st.markdown("---")

st.info("Sistema completo de gestão hospitalar com indicadores e gráficos em tempo real.")