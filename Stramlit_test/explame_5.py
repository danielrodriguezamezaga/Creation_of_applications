import streamlit as st

opcion = st.selectbox("Tu lenguaje de Programación favorito es: ",
                      ("Pyhon","C++","Go"))

st.write("Seleccionaste: ", opcion)