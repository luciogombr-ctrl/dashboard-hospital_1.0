import streamlit as st

# ---------------------------------
# APRESENTAÇÃO
# ---------------------------------
st.markdown("<div class='section-title'>Sobre a Plataforma</div>", unsafe_allow_html=True)

st.markdown(
    """
<div class='description'>
Nossa plataforma foi desenvolvida para facilitar a gestão de dados e indicadores.
A dashboard permite monitorar informações financeiras, hospitalares e comerciais
em tempo real através de gráficos modernos e relatórios interativos.
</div>
""",
    unsafe_allow_html=True
)

# ---------------------------------
# CARDS
# ---------------------------------
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown(
        """
        <div class='card'>
            <h2>💰 Financeiro</h2>
            <p>Controle receitas, despesas, lucro e indicadores financeiros.</p>
        </div>
        """,
        unsafe_allow_html=True
    )

with col2:
    st.markdown(
        """
        <div class='card'>
            <h2>🏥 Hospital</h2>
            <p>Acompanhe atendimentos, pacientes e desempenho hospitalar.</p>
        </div>
        """,
        unsafe_allow_html=True
    )

with col3:
    st.markdown(
        """
        <div class='card'>
            <h2>📈 Vendas</h2>
            <p>Visualize métricas de vendas e performance comercial.</p>
        </div>
        """,
        unsafe_allow_html=True
    )

st.write("")
st.write("")
st.write("")

# ---------------------------------
# BOTÃO PRINCIPAL
# ---------------------------------
st.markdown("<div class='section-title'>Entrar na Dashboard</div>", unsafe_allow_html=True)

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

# ---------------------------------
# RODAPÉ
# ---------------------------------
st.markdown(
    """
    <div style='text-align:center; color:white; padding:20px;'>
        Desenvolvido por Lucio Gomes © 2026
    </div>
    """,
    unsafe_allow_html=True
