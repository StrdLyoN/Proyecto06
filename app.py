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

    if hist_button:
        fig = px.histogram(datos, x='odometer', y='price')
        st.plotly_chart(fig)

if __name__ == '__main__':
    main()