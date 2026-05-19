import streamlit as st

# ---------------------------------------------------
# CONFIGURAÇÃO DA PÁGINA
# ---------------------------------------------------
st.set_page_config(
    page_title="Dashboard Hospitalar",
    page_icon="🏥",
    layout="wide"
)

# ---------------------------------------------------
# CSS PERSONALIZADO
# ---------------------------------------------------
st.markdown("""
<style>

/* FUNDO GRADIENTE */
.stApp {
    background: linear-gradient(
        135deg,
        #ffffff 0%,
        #dcfce7 45%,
        #22c55e 100%
    );
}

/* ESCONDER MENU */
#MainMenu {
    visibility: hidden;
}

footer {
    visibility: hidden;
}

header {
    visibility: hidden;
}

/* TÍTULO PRINCIPAL */
.main-title {
    font-size: 72px;
    font-weight: bold;
    text-align: center;
    color: #14532d;
    margin-top: 70px;
    text-shadow: 2px 2px 10px rgba(0,0,0,0.10);
}

/* SUBTÍTULO */
.subtitle {
    font-size: 30px;
    text-align: center;
    color: #166534;
    margin-bottom: 50px;
    font-weight: 600;
}

/* CARD CENTRAL */
.card {
    background: rgba(255,255,255,0.92);

    padding: 55px;

    border-radius: 25px;

    backdrop-filter: blur(10px);

    box-shadow: 0px 10px 35px rgba(0,0,0,0.15);

    text-align: center;

    margin-top: 20px;

    border: 1px solid rgba(255,255,255,0.7);
}

/* TEXTO DO CARD */
.card-text {
    font-size: 24px;

    color: #14532d;

    line-height: 1.8;

    font-weight: bold;
}

/* BOTÕES */
div.stButton > button {

    background: linear-gradient(
        90deg,
        #16a34a,
        #22c55e
    );

    color: white;

    font-size: 22px;

    font-weight: bold;

    padding: 16px;

    border-radius: 15px;

    border: none;

    width: 100%;

    transition: 0.3s;

    box-shadow: 0px 5px 20px rgba(22,163,74,0.35);
}

/* HOVER BOTÕES */
div.stButton > button:hover {

    transform: scale(1.05);

    background: linear-gradient(
        90deg,
        #15803d,
        #16a34a
    );
}

/* RODAPÉ */
.footer {

    text-align: center;

    color: #14532d;

    margin-top: 80px;

    font-size: 16px;

    font-weight: 600;
}

</style>
""", unsafe_allow_html=True)

# ---------------------------------------------------
# TÍTULO PRINCIPAL
# ---------------------------------------------------
st.markdown("""
<div class="main-title">
🏥 Dashboard Hospitalar
</div>
""", unsafe_allow_html=True)

# ---------------------------------------------------
# SUBTÍTULO
# ---------------------------------------------------
st.markdown("""
<div class="subtitle">
Gestão inteligente para hospitais e clínicas
</div>
""", unsafe_allow_html=True)

# ---------------------------------------------------
# CARD CENTRAL
# ---------------------------------------------------
st.markdown("""
<div class="card">

<h2 style="
color:#15803d;
font-size:42px;
font-weight:bold;
">

📊 Plataforma Completa de Gestão

</h2>

<br>

<p class="card-text">

Monitore indicadores em tempo real,
acompanhe gráficos interativos e tenha
controle total das áreas estratégicas.

</p>

<br>

<p class="card-text">

📈 Financeiro <br><br>

🏥 Hospitalar <br><br>

🛒 Vendas

</p>

<br>

<p class="card-text">

Tecnologia moderna para decisões rápidas
e eficientes.

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

Desenvolvido com ❤️ usando Python + Streamlit

</div>
""", unsafe_allow_html=True)
