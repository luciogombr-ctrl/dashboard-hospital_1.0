# pages/1_Financeiro.py

import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(
    page_title="Financeiro",
    layout="wide"
)

st.title("💰 Dashboard Financeira")

# MENU
col1, col2, col3 = st.columns(3)

with col1:
    st.page_link(
        "app.py",
        label="🏠 Início",
        use_container_width=True
    )

with col2:
    st.page_link(
        "pages/2_Hospital.py",
        label="🏥 Hospital",
        use_container_width=True
    )

with col3:
    st.page_link(
        "pages/3_Vendas.py",
        label="📈 Vendas",
        use_container_width=True
    )

st.divider()

# KPIs
c1, c2, c3 = st.columns(3)

with c1:
    st.metric("Receita", "R$ 1.576.000", "+18%")

with c2:
    st.metric("Despesas", "R$ 854.000", "-9%")

with c3:
    st.metric("Lucro", "R$ 722.000", "+26%")

st.divider()

# GRÁFICO
dados = pd.DataFrame(
    np.random.randn(20, 3),
    columns=["Receita", "Despesas", "Lucro"]
)

st.line_chart(dados)
