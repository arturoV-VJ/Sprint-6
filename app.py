import pandas as pd
import plotly.express as px
import streamlit as st

car_data = pd.read_csv('vehicles_us.csv')
st.header('análisis de anuncios de vehículos')
hist_button = st.button('construir histograma')
if hist_button:
    st.write('histograma para el conjunto de datos de anuncios de venta de coches')
    fig = px.histogram(car_data, x='odometer')
    st.plotly_chart(fig, use_container_width=True)
scatter_button = st.button('construir diagrama de dispersión')
if scatter_button:
    st.write('gráfico de dispersion entre km y precio')
    fig = px.scatter(car_data, x='odometer', y='price')
    st.plotly_chart(fig, use_container_width=True)
    
