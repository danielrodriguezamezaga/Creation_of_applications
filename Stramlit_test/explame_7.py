import streamlit as st
from datetime import time

lenguajes = st.slider("¿Cuántos frameworks conoces de Python?", 0, 15, 0)

st.write("Conoces", lenguajes, "Frameworks de Python")

rango = st.slider("Seleciones un rango de valores", 0.0, 100.0, (25.0, 75.0))

st.write("Rango de alores: ", rango)

hora = st.slider("Hora reunión: ", value=(time(13, 30), time(15, 30)))

st.write("Tu reunión tendra lugar en este intervalo de horas: ", hora)