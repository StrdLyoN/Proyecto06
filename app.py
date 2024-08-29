import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import plotly.express as px

import Data_wrangling

def main():
    datos = pd.read_csv('./vehicles_us.csv')
    datos = Data_wrangling.clean(datos)

    st.header('Vehicles Graphics')
    hist_button = st.button('Make a Histogram')
    disp_button = st.button('Make a Scatterplot')

    if hist_button:
        st.write('Histogram of vehicles_us')
        fig = px.histogram(datos, x='odometer', y='price')
        st.plotly_chart(fig, use_container_width=True)
    
    if disp_button:
        st.write('Scatterplot of Vehicles_usd')
        fig01 = px.scatter(datos, x='odometer', y='price')
        st.plotly_chart(fig01, use_container_width=True)

if __name__ == '__main__':
    main()