import streamlit as st

opciones = st.multiselect("Selecciona multiples opciones entre estos lenguajes: ",
                        ("Python","C++","Java","Go"))

st.write("Has elegido los siguientes lenguajes:", opciones)