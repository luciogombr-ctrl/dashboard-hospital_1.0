import streamlit as st

# ---------------------------------------------------
# CONFIGURAÇÃO DA PÁGINA
# ---------------------------------------------------
st.set_page_config(
    page_title="Dashboard Inteligente",
    page_icon="🚀",
    layout="wide"
)

# ---------------------------------------------------
# ESTILO PERSONALIZADO
# ---------------------------------------------------
st.markdown("""
<style>

/* FUNDO GERAL */
.stApp {
    background: linear-gradient(
        135deg,
        #0f172a,
        #1e293b,
        #0f172a
    );
    color: white;
}

/* REMOVE MENU STREAMLIT */
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
header {visibility: hidden;}

/* TÍTULO */
.main-title {
    font-size: 60px;
    font-weight: bold;
    text-align: center;
    color: white;
    margin-top: 60px;
}

/* SUBTÍTULO */
.subtitle {
    font-size: 24px;
    text-align: center;
    color: #cbd5e1;
    margin-bottom: 40px;
}

/* CARD CENTRAL */
.card {
    background: rgba(255,255,255,0.08);
    padding: 40px;
    border-radius: 25px;
    backdrop-filter: blur(10px);
    box-shadow: 0px 8px 30px rgba(0,0,0,0.4);
    text-align: center;
    margin-top: 30px;
}

/* ÍCONES */
.icons {
    font-size: 28px;
    margin-top: 20px;
    line-height: 2;
}

/* BOTÃO */
div.stButton > button {
    background: linear-gradient(90deg, #2563eb, #3b82f6);
    color: white;
    font-size: 22px;
    font-weight: bold;
    padding: 15px 40px;
    border-radius: 15px;
    border: none;
    width: 100%;
    transition: 0.3s;
    box-shadow: 0px 5px 20px rgba(37,99,235,0.5);
}

/* EFEITO HOVER */
div.stButton > button:hover {
    transform: scale(1.05);
    background: linear-gradient(90deg, #1d4ed8, #2563eb);
}

/* RODAPÉ */
.footer {
    text-align: center;
    color: #94a3b8;
    margin-top: 80px;
    font-size: 15px;
}

</style>
""", unsafe_allow_html=True)

# ---------------------------------------------------
# TÍTULO PRINCIPAL
# ---------------------------------------------------
st.markdown("""
<div class="main-title">
🚀 Dashboard Inteligente
</div>
""", unsafe_allow_html=True)

# ---------------------------------------------------
# SUBTÍTULO
# ---------------------------------------------------
st.markdown("""
<div class="subtitle">
Transformando dados em decisões estratégicas
</div>
""", unsafe_allow_html=True)

# ---------------------------------------------------
# CARD CENTRAL
# ---------------------------------------------------
st.markdown("""
<div class="card">

<h2>📊 Plataforma Completa de Gestão</h2>

<p style="font-size:20px; color:#e2e8f0;">

Acompanhe métricas em tempo real, visualize gráficos
interativos e tenha controle total das áreas:

</p>

<div class="icons">

📈 Financeiro<br>
🏥 Hospitalar<br>
🛒 Vendas

</div>

<br>

<p style="font-size:18px; color:#cbd5e1;">

Uma experiência moderna, rápida e intuitiva
para impulsionar sua produtividade.

</p>

</div>
""", unsafe_allow_html=True)

# ---------------------------------------------------
# ESPAÇAMENTO
# ---------------------------------------------------
st.write("")
st.write("")
st.write("")

# ---------------------------------------------------
# BOTÃO CENTRAL
# ---------------------------------------------------
col1, col2, col3 = st.columns([1,2,1])

with col2:
    if st.button("🚀 Clique Aqui para Acessar o Dashboard"):
        st.switch_page("pages/1_Financeiro.py")

# ---------------------------------------------------
# RODAPÉ
# ---------------------------------------------------
st.markdown("""
<div class="footer">

Desenvolvido com ❤️ usando Python e Streamlit

</div>
""", unsafe_allow_html=True)
