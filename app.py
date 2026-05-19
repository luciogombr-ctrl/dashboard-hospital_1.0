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

/* FUNDO VERDE SUAVE */
.stApp {
    background-color: #dff5e1;
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
    color: #166534;
    margin-top: 70px;
}

/* SUBTÍTULO */
.subtitle {
    font-size: 30px;
    text-align: center;
    color: #15803d;
    margin-bottom: 50px;
    font-weight: 600;
}

/* CARD CENTRAL */
.card {

    background: rgba(0,140,0,0.75);

    padding: 55px;

    border-radius: 25px;

    box-shadow: 0px 8px 25px rgba(0,0,0,0.10);

    text-align: center;

    margin-top: 20px;
}

/* TÍTULO DO CARD */
.card-title {

    color: #166534;

    font-size: 42px;

    font-weight: bold;
}

/* TEXTO */
.card-text {

    font-size: 24px;

    color: #14532d;

    line-height: 1.8;

    font-weight: 600;
}

/* BOTÕES */
div.stButton > button {

    background-color: #16a34a;

    color: white;

    font-size: 22px;

    font-weight: bold;

    padding: 16px;

    border-radius: 15px;

    border: none;

    width: 100%;

    transition: 0.3s;
}

/* HOVER */
div.stButton > button:hover {

    background-color: #15803d;

    transform: scale(1.03);
}

/* RODAPÉ */
.footer {

    text-align: center;

    color: #166534;

    margin-top: 80px;

    font-size: 16px;

    font-weight: 600;
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
# CARD CENTRAL
# ---------------------------------------------------
st.markdown("""
<div class="card">

<div class="card-title">
📊 Plataforma Completa de Gestão
</div>

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
