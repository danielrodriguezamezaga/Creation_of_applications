import streamlit as st

entrada_texto = st.text_input("Inserte un texto: ")
st.write("Texto del text_input", entrada_texto)

entrada_numero = st.number_input("Inserte el número: ")
st.write("El número insertado es: ", entrada_numero)

