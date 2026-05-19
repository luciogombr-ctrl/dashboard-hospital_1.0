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
# CSS TEMA HOSPITALAR
# ---------------------------------------------------
st.markdown("""
<style>

/* FUNDO */
.stApp {
    background: linear-gradient(
        135deg,
        #064e3b 0%,
        #065f46 40%,
        #991b1b 100%
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

/* TÍTULO */
.main-title {
    font-size: 70px;
    font-weight: bold;
    text-align: center;
    color: white;
    margin-top: 80px;
    text-shadow: 2px 2px 20px rgba(0,0,0,0.5);
}

/* SUBTÍTULO */
.subtitle {
    font-size: 28px;
    text-align: center;
    color: #f1f5f9;
    margin-bottom: 50px;
}

/* CARD */
.card {
    background: rgba(255,255,255,0.10);
    padding: 45px;
    border-radius: 25px;
    backdrop-filter: blur(10px);
    box-shadow: 0px 10px 30px rgba(0,0,0,0.4);
    text-align: center;
    margin-top: 20px;
    border: 1px solid rgba(255,255,255,0.15);
}

/* TEXTO */
.card-text {
    font-size: 22px;
    color: white;
    line-height: 1.8;
}

/* BOTÕES */
div.stButton > button {
    background: linear-gradient(
        90deg,
        #dc2626,
        #16a34a
    );

    color: white;
    font-size: 22px;
    font-weight: bold;

    padding: 16px;
    border-radius: 15px;
    border: none;

    width: 100%;

    transition: 0.3s;

    box-shadow: 0px 5px 20px rgba(0,0,0,0.4);
}

/* HOVER */
div.stButton > button:hover {
    transform: scale(1.05);

    background: linear-gradient(
        90deg,
        #b91c1c,
        #15803d
    );
}

/* RODAPÉ */
.footer {
    text-align: center;
    color: white;
    margin-top: 80px;
    font-size: 16px;
}

</style>
""", unsafe_allow_html=True)

# ---------------------------------------------------
# TÍTULO
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
# CARD
# ---------------------------------------------------
st.markdown("""
<div class="card">

<h2 style="color:white; font-size:38px;">
📊 Plataforma Completa de Gestão
</h2>

<p class="card-text">

Monitore indicadores em tempo real,
acompanhe gráficos interativos e tenha
controle total das áreas estratégicas.

</p>

<p class="card-text">

📈 Financeiro <br>
🏥 Hospitalar <br>
🛒 Vendas

</p>

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
# BOTÕES
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
