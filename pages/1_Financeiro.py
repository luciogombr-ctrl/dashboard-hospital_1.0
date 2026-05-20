import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(page_title="Financeiro", layout="wide")

st.title("💰 Dashboard Financeira")

# MENU
col1, col2, col3 = st.columns(3)

with col1:
    st.page_link("app.py", label="🏠 Início", use_container_width=True)

with col2:
    st.page_link("pages/2_Hospital.py", label="🏥 Hospital", use_container_width=True)

with col3:
    st.page_link("pages/3_Vendas.py", label="📈 Vendas", use_container_width=True)

st.divider()

# KPIS
col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Receita", "R$ 120.000", "+12%")

with col2:
    st.metric("Despesas", "R$ 45.000", "-5%")

with col3:
    st.metric("Lucro", "R$ 75.000", "+18%")

st.divider()

# GRÁFICO
chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=['Receitas', 'Despesas', 'Lucro']
)

st.line_chart(chart_data)
