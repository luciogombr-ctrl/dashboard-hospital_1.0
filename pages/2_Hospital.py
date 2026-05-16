import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Hospital",
    page_icon="🏥",
    layout="wide"
)

# BOTÃO HOME
st.page_link(
    "app.py",
    label="⬅️ Voltar para Home",
    icon="🏠"
)

st.title("🏥 Dashboard Hospitalar")

st.markdown("---")

# MÉTRICAS
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("Pacientes", "1.250", "+10%")

with col2:
    st.metric("Médicos", "85", "+2")

with col3:
    st.metric("Leitos Ocupados", "72%", "+5%")

with col4:
    st.metric("Cirurgias", "210", "+12")

st.markdown("---")

# DADOS
hospital = pd.DataFrame({
    "Setor": ["UTI", "Emergência", "Clínica", "Pediatria"],
    "Pacientes": [35, 60, 45, 25]
})

# GRÁFICOS
col1, col2 = st.columns(2)

with col1:
    st.subheader("🏥 Pacientes por Setor")
    st.bar_chart(hospital.set_index("Setor"))

with col2:
    st.subheader("📊 Distribuição de Pacientes")
    st.dataframe(hospital, use_container_width=True)

st.markdown("---")

st.info("Hospital operando normalmente.")