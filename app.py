import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import plotly.express as px

from Data_wrangling import Limpiador

def main():
    datos_raw = pd.read_csv('./vehicles_us.csv')
    limpiador = Limpiador('Limpiador',datos_raw)

    print(datos_raw.isna().sum())
    datos_clean = limpiador.clean()

    print(datos_clean.isna().sum())


    st.header('Vehicles Graphics')
    hist_button = st.button('Make a Histogram')
    disp_button = st.button('Make a Scatterplot')

    if hist_button:
        st.write('Histogram of vehicles_us')
        fig = px.histogram(datos_clean, x='odometer')
        st.plotly_chart(fig, use_container_width=True)
    
    if disp_button:
        st.write('Scatterplot of Vehicles_usd')
        fig01 = px.scatter(datos_clean, x='odometer')
        st.plotly_chart(fig01, use_container_width=True)

if __name__ == '__main__':
    main()