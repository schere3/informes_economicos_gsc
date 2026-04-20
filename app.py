import streamlit as st
import pandas as pd
import plotly.express as px

def pagina_principal():
    st.title("Página Principal")
    st.write("Estamos antes la página principal de nuestro estudio")
    st.write("Usa el menú de la izquierda para navegar entre las páginas.")
    # Todo el contenido Markdown debe ir entre comillas triples dentro de st.markdown
    st.markdown("""
    ## Índice
    1. [Introducción](#introducción)
    Comenzamos realizando un analisis de...
    2. [Requisitos Previos](#requisitos-previos)
    Por ende el requisito previo...
    3. [Instalación y Configuración](#instalación-y-configuración)
    4. [Ir a Requisitos](otra-pagina.md#requisitos-previos)
    A veces, no basta solo con realizar ...
    """)


def visualizar_datos():
    st.title("Visualización de Datos")
    st.write("Carga un archivo CSV para visualizar los datos.")
    archivo_cargado = st.file_uploader("Elige un archivo CSV", type="csv")

    if archivo_cargado is not None:
        df = pd.read_csv(archivo_cargado)
        st.write("Datos del archivo csv:")
        st.write(df)
        st.write("Estadísticas descriptivas")
        st.write(df.describe())

def graficos_interactivos():
    st.title("Gráficos Interactivos")
    st.write("Carga un archivo CSV para crear gráficos interactivos.")
    archivo_cargado = st.file_uploader("Elige un archivo CSV", type="csv", key="2")
    
    if archivo_cargado is not None:
        df = pd.read_csv(archivo_cargado)
        st.write("Elige una columna para el eje X:")
        eje_x = st.selectbox("Eje X", df.columns)
        st.write("Elige una columna para el eje Y:")
        eje_y = st.selectbox("Eje Y", df.columns)
        if st.button("Crear Gráfico"):
            fig = px.bar(df, x=eje_x, y=eje_y, title=f"{eje_y} por {eje_x}")
            st.plotly_chart(fig)

st.sidebar.title("Navegación")
pagina = st.sidebar.selectbox("Selecciona una página", ["Página Principal", 
                                                        "Visualización de Datos",
                                                        "Gráficos Interactivos"])
if pagina == "Página Principal":
    pagina_principal()
elif pagina == "Visualización de Datos":
    visualizar_datos()
elif pagina == "Gráficos Interactivos":
    graficos_interactivos()
