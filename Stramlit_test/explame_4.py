import streamlit as st

radio = st.radio("Tener en cuenta los Outliers:",
                 ("si", "no"))

if radio == "si":
    st.write("Eliminaremos los Outliers")
else:
    st.write("No eliminaremos los Outliers del Dataset")
    