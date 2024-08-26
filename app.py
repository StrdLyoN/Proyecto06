import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import plotly.express as px

datos = pd.read_csv('./vehicles_us.csv')

print(datos.head())

fig = px.histogram(datos, x='odometer', y='price')

fig.show()