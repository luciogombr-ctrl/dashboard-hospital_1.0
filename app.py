import streamlit as st

# -----------------------------------
# CONFIGURAÇÃO DA PÁGINA
# -----------------------------------
st.set_page_config(
    page_title="Dashboard Hospitalar",
    page_icon="🏥",
    layout="wide"
)

# -----------------------------------
# ESTILO DA PÁGINA
# -----------------------------------
st.markdown(
    """
    <style>

    .stApp {
        background-color: #0f5132;
    }

    h1, h2, h3, h4, h5, h6 {
        color: white;
    }

    p {
        color: white;
        font-size: 18px;
    }

    .titulo {
        text-align: center;
        font-size: 60px;
        font-weight: bold;
        color: white;
        margin-top: 40px;
    }

    .subtitulo {
        text-align: center;
        font-size: 24px;
        color: #d9fdd3;
        margin-bottom: 40px;
    }

    .caixa {
        background-color: #146c43;
        padding: 30px;
        border-radius: 15px;
        margin-top: 20px;
        box-shadow: 0px 0px 10px rgba(0,0,0,0.3);
    }

    .stButton>button {
        width: 100%;
        height: 60px;
        border-radius: 12px;
        border: none;
        background-color: #198754;
        color: white;
        font-size: 20px;
        font-weight: bold;
        transition: 0.3s;
    }

    .stButton>button:hover {
        background-color: #20c997;
        color: black;
    }

    </style>
    """,
    unsafe_allow_html=True
)

# -----------------------------------
# TÍTULO
# -----------------------------------
st.markdown(
    """
    <div class="titulo">
        Plataforma Completa de Gestão
    </div>
    """,
    unsafe_allow_html=True
)

# -----------------------------------
# SUBTÍTULO
# -----------------------------------
st.markdown(
    """
    <div class="subtitulo">
        Dashboard moderno para controle financeiro, hospitalar e vendas
    </div>
    """,
    unsafe_allow_html=True
)

# -----------------------------------
# IMAGEM
# -----------------------------------
st.image(
    "https://images.unsplash.com/photo-1516321318423-f06f85e504b3",
    use_container_width=True
)

# -----------------------------------
# BOTÃO PRINCIPAL
# -----------------------------------
st.markdown("<br>", unsafe_allow_html=True)

if st.button("ENTRAR NA DASHBOARD"):
    st.success("Dashboard carregada com sucesso!")

# -----------------------------------
# CARDS
# -----------------------------------
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown(
        """
        <div class="caixa">
            <h2>💰 Financeiro</h2>
            <p>
            Controle completo de receitas, despesas,
            faturamento e relatórios financeiros.
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.button("Acessar Financeiro")

with col2:
    st.markdown(
        """
        <div class="caixa">
            <h2>🏥 Hospital</h2>
            <p>
            Gestão hospitalar com pacientes,
            consultas, exames e indicadores.
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.button("Acessar Hospital")

with col3:
    st.markdown(
        """
        <div class="caixa">
            <h2>📈 Vendas</h2>
            <p>
            Dashboard de vendas com metas,
            produtos e desempenho comercial.
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.button("Acessar Vendas")

# -----------------------------------
# RODAPÉ
# -----------------------------------
st.markdown("<br><br>", unsafe_allow_html=True)

st.markdown(
    """
    <center>
        <p style='color:white;'>
            Desenvolvido por Lucio gomes de Oliveira
        </p>
    </center>
    """,
    unsafe_allow_html=True
)
