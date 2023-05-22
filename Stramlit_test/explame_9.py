import streamlit as st
import quandl

st.title("Grafica con Streamlit para finanzas")

empresas = ("GOOGL", "MSFT", "TSLA", "NFLX", "AAPL")

opcion = st.selectbox("Selecciona una de estas empresas:",
                      empresas)

st.write("Has elegido: ", opcion)

años = st.slider("Número de años que quieres plotear:", 1, 5, 1)
st.write("Has elegido: ", años, "años")

año_final = 2015 + años
st.write("año final:", año_final)

data = quandl.get(f"WIKI/{opcion}",
                  start_date="2015-1-1",
                  end_date=f"{año_final}-12-31")

st.write("Vamos a imprimir los primeros 5 valores de Dataset")
st.write(data.head())

st.write("Vamos a imprimir los ultimos 5 valores de Dataset")
st.write(data.tail())


st.write("Vamos a seleccionar solamente la columna close")
colum = data[["Close"]]

st.write(colum)

st.write("Vamos a plotear el grafico seleccionado")
st.write("GRAFICO")
st.write("Año inicial: 2015, año final: ", año_final)

st.line_chart(colum)