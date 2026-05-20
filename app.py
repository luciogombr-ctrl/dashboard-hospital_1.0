import streamlit as st

# CONFIGURAÇÃO DA PÁGINA
st.set_page_config(
    page_title="Dashboard Completa",
    page_icon="📊",
    layout="wide"
)

# ===== ESTILO =====
st.markdown("""
<style>

.main {
    background-color: #0f5132;
}

h1, h2, h3, h4, h5 {
    color: white;
    text-align: center;
}

p {
    color: white;
    text-align: center;
    font-size: 18px;
}

.stButton>button {
    width: 100%;
    border-radius: 12px;
    height: 55px;
    font-size: 18px;
    font-weight: bold;
    background-color: #198754;
    color: white;
    border: none;
}

.stButton>button:hover {
    background-color: #157347;
    color: white;
}

.block-container {
    padding-top: 2rem;
}

</style>
""", unsafe_allow_html=True)

# ===== TÍTULO =====
st.title("📊 Plataforma Completa de Gestão")

st.write("""
Bem-vindo ao sistema inteligente de gestão.

Escolha abaixo qual dashboard deseja acessar.
""")

st.divider()

# ===== COLUNAS =====
col1, col2, col3 = st.columns(3)

# ===== HOSPITAL =====
with col1:

    st.markdown("## 🏥 Hospital")

    st.write("""
    Gestão hospitalar completa com:
    
    - Pacientes
    - Leitos
    - Médicos
    - Atendimentos
    - Indicadores
    """)

    st.page_link(
        "pages/1_Hospital.py",
        label="🏥 Abrir Hospital",
        icon="🏥"
    )

# ===== FINANCEIRO =====
with col2:

    st.markdown("## 💰 Financeiro")

    st.write("""
    Controle financeiro completo:
    
    - Receitas
    - Despesas
    - Fluxo de caixa
    - Indicadores
    - Relatórios
    """)

    st.page_link(
        "pages/2_Financeiro.py",
        label="💰 Abrir Financeiro",
        icon="💰"
    )

# ===== VENDAS =====
with col3:

    st.markdown("## 📊 Vendas")

    st.write("""
    Dashboard de vendas completo:
    
    - Produtos
    - Clientes
    - Metas
    - Faturamento
    - Gráficos
    """)

    st.page_link(
        "pages/3_Vendas.py",
        label="📊 Abrir Vendas",
        icon="📊"
    )

st.divider()

st.markdown("""
<p style='text-align: center; color: white;'>
© 2026 Plataforma de Gestão Inteligente
</p>
""", unsafe_allow_html=True)
