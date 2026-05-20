import streamlit as st

# -----------------------------------
# CONFIGURAÇÃO DA PÁGINA
# -----------------------------------
st.set_page_config(
    page_title="Dashboard Empresarial",
    page_icon="📊",
    layout="wide"
)

# -----------------------------------
# ESTILO PERSONALIZADO
# -----------------------------------
st.markdown("""
<style>

.stApp {
    background-color: #0f5132;
}

h1, h2, h3, h4, h5, h6 {
    color: white;
}

p, div {
    color: white;
}

[data-testid="stSidebar"] {
    background-color: #198754;
}

.stButton>button {
    background-color: white;
    color: #198754;
    border-radius: 10px;
    padding: 10px 20px;
    font-weight: bold;
    border: none;
}

.stButton>button:hover {
    background-color: #d1e7dd;
    color: #0f5132;
}

</style>
""", unsafe_allow_html=True)

# -----------------------------------
# TÍTULO
# -----------------------------------
st.title("📊 Plataforma Completa de Gestão")

st.write("""
Bem-vindo à plataforma empresarial.

Acesse abaixo os módulos disponíveis:

- 🏥 Hospital
- 💰 Financeiro
- 📈 Vendas
""")

# -----------------------------------
# BANNER ONLINE
# -----------------------------------
st.image(
    "https://images.unsplash.com/photo-1519494026892-80bbd2d6fd0d",
    use_container_width=True
)

st.divider()

# -----------------------------------
# BOTÕES DE NAVEGAÇÃO
# -----------------------------------
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

# -----------------------------------
# RODAPÉ
# -----------------------------------
st.divider()

st.markdown("""
<div style='text-align: center; color: white;'>
    © 2026 Plataforma de Gestão Empresarial
</div>
""", unsafe_allow_html=True)
