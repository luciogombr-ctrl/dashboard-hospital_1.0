import streamlit as st

# CONFIGURAÇÃO DA PÁGINA
st.set_page_config(
    page_title="Dashboard Empresarial",
    page_icon="📊",
    layout="wide"
)

# CORES E ESTILO
st.markdown("""
<style>

.stApp {
    background-color: #0f5132;
}

h1, h2, h3, h4, h5, h6 {
    color: white;
}

p {
    color: white;
}

[data-testid="stSidebar"] {
    background-color: #198754;
}

.botao {
    background-color: white;
    color: #198754;
    padding: 15px;
    border-radius: 10px;
    text-align: center;
    font-size: 18px;
    font-weight: bold;
}

</style>
""", unsafe_allow_html=True)

# TÍTULO
st.title("📊 Plataforma Completa de Gestão")

st.write("""
Bem-vindo à plataforma empresarial.

Acesse abaixo os módulos disponíveis:
- Hospital
- Financeiro
- Vendas
""")

# BANNER
st.image("assets/banner.jpg", use_container_width=True)

st.divider()

# BOTÕES DE ACESSO
col1, col2, col3 = st.columns(3)

with col1:
    st.page_link(
        "pages/1_Hospital.py",
        label="🏥 Abrir Hospital",
        icon="🏥"
    )

with col2:
    st.page_link(
        "pages/2_Financeiro.py",
        label="💰 Abrir Financeiro",
        icon="💰"
    )

with col3:
    st.page_link(
        "pages/3_Vendas.py",
        label="📈 Abrir Vendas",
        icon="📈"
    )
