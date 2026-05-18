import streamlit as st

# ---------------------------------------------------
# IMAGEM DE FUNDO
# ---------------------------------------------------
https://raw.githubusercontent.com/SEU-USUARIO/SEU-REPOSITORIO/main/imagem.jpg

# ---------------------------------------------------
# CONFIGURAÇÃO DA PÁGINA
# ---------------------------------------------------
st.set_page_config(
    page_title="Dashboard Inteligente",
    page_icon="🚀",
    layout="wide"
)

# ---------------------------------------------------
# CSS PERSONALIZADO
# ---------------------------------------------------
st.markdown(f"""
<style>

/* FUNDO COM IMAGEM */
.stApp {{
    background:
        linear-gradient(
            rgba(0,0,0,0.70),
            rgba(0,0,0,0.70)
        ),
        url("{background_image}");

    background-size: cover;
    background-position: center;
    background-repeat: no-repeat;
    background-attachment: fixed;
}}

/* ESCONDER MENU E RODAPÉ */
#MainMenu {{
    visibility: hidden;
}}

footer {{
    visibility: hidden;
}}

header {{
    visibility: hidden;
}}

/* TÍTULO PRINCIPAL */
.main-title {{
    font-size: 65px;
    font-weight: bold;
    text-align: center;
    color: white;
    margin-top: 80px;
    text-shadow: 2px 2px 15px rgba(0,0,0,0.8);
}}

/* SUBTÍTULO */
.subtitle {{
    font-size: 28px;
    text-align: center;
    color: #e2e8f0;
    margin-bottom: 50px;
}}

/* CARD CENTRAL */
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

/* ÍCONES */
.icons {{
    font-size: 30px;
    margin-top: 25px;
    line-height: 2;
}}

/* BOTÃO */
div.stButton > button {{
    background: linear-gradient(90deg, #2563eb, #3b82f6);
    color: white;
    font-size: 24px;
    font-weight: bold;
    padding: 16px 40px;
    border-radius: 15px;
    border: none;
    width: 100%;
    transition: 0.3s;
    box-shadow: 0px 5px 20px rgba(37,99,235,0.5);
}}

/* HOVER DO BOTÃO */
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

<h2 style="color:white; font-size:36px;">
📊 Plataforma Completa de Gestão
</h2>

<p class="card-text">

Acompanhe métricas em tempo real, visualize gráficos
interativos e tenha controle total das áreas:

</p>

<div class="icons">

📈 Financeiro<br>
🏥 Hospitalar<br>
🛒 Vendas

</div>

<br>

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
