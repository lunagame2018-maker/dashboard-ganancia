import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

st.title("Modelo interactivo de ganancia empresarial")

precio = st.slider("Precio por proyecto ($)", 20000, 40000, 30000, step=1000)
costo_fijo = st.slider("Costo fijo ($)", 15000000, 30000000, 20000000, step=1000000)
costo_variable = st.slider("Costo variable ($)", 10000, 30000, 20000, step=1000)
factor_tecnologico = st.slider("Factor tecnológico", 1000000, 4000000, 2000000, step=100000)

x = np.linspace(100, 3000, 100)

ingreso = precio * x
costo = costo_fijo + costo_variable * x + factor_tecnologico / x
ganancia = ingreso - costo

fig, ax = plt.subplots()
ax.plot(x, ingreso, label="Ingreso")
ax.plot(x, costo, label="Costo")
ax.plot(x, ganancia, label="Ganancia")

ax.set_xlabel("Número de proyectos")
ax.set_ylabel("Monto ($)")
ax.set_title("Ingreso, costo y ganancia en función del número de proyectos")
ax.legend()
ax.grid(True)

st.pyplot(fig)