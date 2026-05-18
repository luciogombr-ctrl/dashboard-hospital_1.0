import streamlit as st

# -----------------------------------
# CONFIGURAÇÃO DA PÁGINA
# -----------------------------------
st.set_page_config(
    page_title="Dashboard Inteligente",
    page_icon="🚀",
    layout="wide"
)

# -----------------------------------
# TÍTULO
# -----------------------------------
st.markdown("""
<h1 style='text-align:center; color:#2563eb;'>
🚀 Dashboard Inteligente de Gestão
</h1>
""", unsafe_allow_html=True)

# -----------------------------------
# DESCRIÇÃO
# -----------------------------------
st.markdown("""
<div style='text-align:center; font-size:20px;'>

Transforme dados em decisões com uma plataforma moderna,
rápida e intuitiva.

<br><br>

📊 Financeiro<br>
🏥 Hospitalar<br>
🛒 Vendas

<br><br>

Gráficos interativos, indicadores em tempo real
e análises estratégicas para o seu negócio.

</div>
""", unsafe_allow_html=True)

# -----------------------------------
# BOTÃO CENTRAL
# -----------------------------------
col1, col2, col3 = st.columns(3)

with col2:
    if st.button("🚀 Clique Aqui para Acessar o Dashboard"):
        st.switch_page("pages/1_Financeiro.py")

# -----------------------------------
# RODAPÉ
# -----------------------------------
st.markdown("""
<hr>

<p style='text-align:center; color:gray;'>
Desenvolvido com Python e Streamlit
</p>
""", unsafe_allow_html=True)
