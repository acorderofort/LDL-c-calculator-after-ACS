import streamlit as st
import numpy as np

# Coeficientes del modelo logístico
b0 = -0.0457
b_ldl = -0.0131
b_estat = 0.0433
b_interact = -0.0067

st.set_page_config(page_title="Calculadora de Riesgo LDL < 55")
st.title("Probability of LDL-c < 55 mg/dL after an ACS")

st.markdown("Slide to mark LDL-C (mg/dl) determined in the ACS")

# Entrada del usuario
ldl = st.slider("LDL (mg/dL)", min_value=50, max_value=200, value=100)
estatinas = st.radio("¿On-treatment with statins?", [0, 1], format_func=lambda x: "Sí" if x else "No")

# Cálculo
interaction = ldl * estatinas
logit = b0 + b_ldl * ldl + b_estat * estatinas + b_interact * interaction
prob = 1 / (1 + np.exp(-logit))

# Resultado
st.subheader("Probability with standard theraphy")
st.metric("Probabilidad estimada de LDL < 55", f"{prob*100:.1f}%")
