# pages/3_Vendas.py

import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(
    page_title="Vendas",
    layout="wide"
)

st.title("📈 Dashboard de Vendas")

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
        "pages/1_Financeiro.py",
        label="💰 Financeiro",
        use_container_width=True
    )

with col3:
    st.page_link(
        "pages/2_Hospital.py",
        label="🏥 Hospital",
        use_container_width=True
    )

st.divider()

# KPIs
c1, c2, c3 = st.columns(3)

with c1:
    st.metric("Vendas", "4.520", "+14%")

with c2:
    st.metric("Clientes", "1.230", "+9%")

with c3:
    st.metric("Conversão", "28%", "+4%")

st.divider()

# GRÁFICO
dados = pd.DataFrame(
    np.random.randn(25, 3),
    columns=["Vendas", "Clientes", "Conversão"]
)

st.bar_chart(dados)
