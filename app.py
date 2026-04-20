import streamlit as st
import pandas as pd
import plotly.express as px

def pagina_principal():
    st.title("Página Principal")
    st.write("Estamos antes la página principal de nuestro estudio")
    st.write("Usa el menú de la izquierda para navegar entre las páginas.")

st.sidebar.title("Navegación")