# pages/2_Hospital.py

import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(
    page_title="Hospital",
    layout="wide"
)

st.title("🏥 Dashboard Hospitalar")

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
        "pages/3_Vendas.py",
        label="📈 Vendas",
        use_container_width=True
    )

st.divider()

# KPIs
c1, c2, c3 = st.columns(3)

with c1:
    st.metric("Pacientes", "320", "+20")

with c2:
    st.metric("Atendimentos", "1.250", "+15%")

with c3:
    st.metric("Leitos", "87%", "+4%")

st.divider()

# GRÁFICO
dados = pd.DataFrame(
    np.random.randn(30, 3),
    columns=["Pacientes", "Atendimentos", "Internações"]
)

st.area_chart(dados)
