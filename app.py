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
# IMAGEM DE FUNDO
# ---------------------------------------------------
background_image = "https://raw.githubusercontent.com/luciogombr-ctrl/dashboard-hospital/main/imagem.jpg"

# ---------------------------------------------------
# CSS PERSONALIZADO
# ---------------------------------------------------
st.markdown(f"""
<style>

/* FUNDO */
.stApp {{
    background:
        linear-gradient(
            rgba(0,0,0,0.75),
            rgba(0,0,0,0.75)
        ),
        url("{background_image}");

    background-size: cover;
    background-position: center;
    background-repeat: no-repeat;
    background-attachment: fixed;
}}

/* ESCONDER MENU */
#MainMenu {{
    visibility: hidden;
}}

footer {{
    visibility: hidden;
}}

header {{
    visibility: hidden;
}}

/* TÍTULO */
.main-title {{
    font-size: 70px;
    font-weight: bold;
    text-align: center;
    color: white;
    margin-top: 80px;
    text-shadow: 2px 2px 20px rgba(0,0,0,0.8);
}}

/* SUBTÍTULO */
.subtitle {{
    font-size: 28px;
    text-align: center;
    color: #e2e8f0;
    margin-bottom: 60px;
}}

/* CARD */
.card {{
    background: rgba(255,255,255,0.10);
    padding: 45px;
    border-radius: 25px;
    backdrop-filter: blur(12px);
    box-shadow: 0px 8px 30px rgba(0,0,0,0.5);
    text-align: center;
    margin-top: 20px;
}}

/* TEXTO */
.card-text {{
    font-size: 22px;
    color: #f1f5f9;
    line-height: 1.8;
}}

/* BOTÕES */
div.stButton > button {{
    background: linear-gradient(90deg, #2563eb, #3b82f6);
    color: white;
    font-size: 22px;
    font-weight: bold;
    padding: 16px;
    border-radius: 15px;
    border: none;
    width: 100%;
    transition: 0.3s;
    box-shadow: 0px 5px 20px rgba(37,99,235,0.5);
}}

/* HOVER */
div.stButton > button:hover {{
    transform: scale(1.05);
    background: linear-gradient(90deg, #1d4ed8, #2563eb);
}}

/* RODAPÉ */
.footer {{
    text-align: center;
    color: #cbd5e1;
    margin-top: 80px;
    font-size: 16px;
}}

</style>
""", unsafe_allow_html=True)

# ---------------------------------------------------
# TÍTULO
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

<h2 style="color:white; font-size:36px;">
📊 Plataforma Completa de Gestão
</h2>

<p class="card-text">

Acompanhe métricas em tempo real, visualize gráficos
interativos e tenha controle total das áreas:

</p>

<p class="card-text">
📈 Financeiro <br>
🏥 Hospitalar <br>
🛒 Vendas
</p>

<p class="card-text">

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
# BOTÕES DE NAVEGAÇÃO
# ---------------------------------------------------
col1, col2, col3 = st.columns(3)

# FINANCEIRO
with col1:
    if st.button("📈 Financeiro"):
        st.switch_page("pages/1_Financeiro.py")

# HOSPITAL
with col2:
    if st.button("🏥 Hospital"):
        st.switch_page("pages/2_Hospital.py")

# VENDAS
with col3:
    if st.button("🛒 Vendas"):
        st.switch_page("pages/3_Vendas.py")

# ---------------------------------------------------
# RODAPÉ
# ---------------------------------------------------
st.markdown("""
<div class="footer">

Desenvolvido com ❤️ usando Python e Streamlit

</div>
""", unsafe_allow_html=True)
