import pandas as pd
import plotly.express as px
import streamlit as st

st.header("PROYECTO 5")
car_data = pd.read_csv('vehicles_us.csv') # leer los datos

st.write("DataFrame Completo:")
st.dataframe(car_data)
