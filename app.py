# app.py

import streamlit as st

st.set_page_config(
    page_title="Dashboard Empresarial",
    page_icon="📊",
    layout="wide"
)

# =========================
# CSS
# =========================
st.markdown("""
<style>

.stApp{
    background-color:#0f5132;
}

.titulo{
    text-align:center;
    color:white;
    font-size:60px;
    font-weight:bold;
}

.subtitulo{
    text-align:center;
    color:#d9fff0;
    font-size:24px;
    margin-bottom:40px;
}

.card{
    background:rgba(255,255,255,0.08);
    padding:30px;
    border-radius:20px;
    text-align:center;
    color:white;
}

.section{
    color:white;
    text-align:center;
    font-size:35px;
    font-weight:bold;
    margin-top:40px;
}

/* SOMENTE A COR DO "ACESSAR DASHBOARD" */
[data-testid="stPageLink-NavLink"] p{
    color:white !important;
}

</style>
""", unsafe_allow_html=True)

# =========================
# TÍTULO
# =========================
st.markdown(
    "<div class='titulo'>Dashboard Empresarial</div>",
    unsafe_allow_html=True
)

st.markdown(
    "<div class='subtitulo'>Sistema inteligente de gestão empresarial</div>",
    unsafe_allow_html=True
)

# =========================
# IMAGEM
# =========================
st.image(
    "https://raw.githubusercontent.com/luciogombr-ctrl/dashboard-hospital_1.0/refs/heads/main/Gemini_Generated_Image_5r18v25r18v25r18%20(1).png",
    use_container_width=True
)

# =========================
# SOBRE
# =========================
st.markdown(
    "<div class='section'>Sobre a Plataforma</div>",
    unsafe_allow_html=True
)

st.write("")

st.markdown("""
<div style='text-align:center;color:white;font-size:20px'>
Acompanhe indicadores financeiros, hospitalares e comerciais
em tempo real através de gráficos modernos e dashboards profissionais.
</div>
""", unsafe_allow_html=True)

st.write("")
st.write("")

# =========================
# CARDS
# =========================
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    <div class='card'>
        <h2>💰 Financeiro</h2>
        <p>Controle receitas e despesas.</p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class='card'>
        <h2>🏥 Hospital</h2>
        <p>Gestão hospitalar completa.</p>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class='card'>
        <h2>📈 Vendas</h2>
        <p>Monitoramento de vendas.</p>
    </div>
    """, unsafe_allow_html=True)

st.write("")
st.write("")
st.write("")

# =========================
# BOTÃO PRINCIPAL
# =========================
st.markdown(
    "<div class='section'>Entrar na Dashboard</div>",
    unsafe_allow_html=True
)

col1, col2, col3 = st.columns([1,2,1])

with col2:
    st.page_link(
        "pages/1_Financeiro.py",
        label="🚀 ACESSAR DASHBOARD",
        icon="📊",
        use_container_width=True
    )

st.write("")
st.write("")

st.markdown("""
<div style='text-align:center;color:white'>
Desenvolvido por Lucio Gomes de Oliveira © 2026
</div>
""", unsafe_allow_html=True)
