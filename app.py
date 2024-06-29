import pandas as pd
import plotly.express as px
import streamlit as st

st.header("PROYECTO 5")
car_data = pd.read_csv('vehicles_us.csv') # leer los datos

st.write("DataFrame Completo:")
st.dataframe(car_data)

hist_button = st.button('Construir histograma') # crear un botón

if hist_button: # al hacer clic en el botón
         # escribir un mensaje
        st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')
         # crear un histograma
        fig = px.histogram(car_data, x="odometer")
        # mostrar un gráfico Plotly interactivo
        st.plotly_chart(fig, use_container_width=True)

disp_button = st.button('Construir gráfico de dispersión') # crear un botón
