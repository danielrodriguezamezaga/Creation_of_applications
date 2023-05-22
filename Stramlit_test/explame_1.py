import streamlit as st
import pandas as pd

st.title("Primera aplicacion con Stramlit")
st.title("Podemos escribir lo que queramos, text, en esta ocación")

st.title("Incluso un dataframe como este:")

df = pd.DataFrame({"a": [10,30,20,40,20],
                   "b": [40,10,20,50,60]})

st.write(df)

