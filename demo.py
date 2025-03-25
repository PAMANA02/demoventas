import pandas as pd
import streamlit as st
import plotly.express as px

# Lee el archivo Excel
try:
    df = pd.read_excel('SalidaFinal.xlsx')
    print(df.head())  # Muestra las primeras filas del DataFrame
    print(df.columns)  # Imprime los nombres de las columnas del DataFrame
except FileNotFoundError:
    print("Error: El archivo 'SalidaFinal.xlsx' no se encuentra.")
except Exception as e:
    print(f"Error al leer el archivo: {e}")
