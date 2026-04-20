import streamlit as st
import pandas as pd
import plotly.express as px

st.title("Predicción Gastos de Electricidad 2026")
st.write("El presente estudio se centrará en el análisis del gasto de electricidad 2024-2025 correspondientes a la empresa pública SUC.")
st.write("El objetivo es realizar un análisis de series temporales utilizando técnicas de Machine Learning (ML) a partir de los datos de gasto de electricidad correspondientes a los años 2024 y 2025, con el fin de modelar su comportamiento y realizar posibles predicciones.")

# Cargado de datos
st.header("⚡ Estudio de Gastos de Electricidad")
st.title("Visualización de Datos")
st.write("Carga un archivo CSV para visualizar los datos.")
archivo_cargado = st.file_uploader("Elige un archivo CSV", type="csv")
if archivo_cargado is not None:
    df = pd.read_csv(archivo_cargado)
    st.write("Datos del archivo csv:")
    st.write(df)
    st.write("Estadísticas descriptivas")
    st.write(df.describe())

# Sub-navegación mediante Pestañas (Tabs)
tab1, tab2, tab3 = st.tabs(["📊 Vista General", "📈 Tendencias", "💰 Análisis de Costes"])

with tab1:
    st.subheader("Resumen del Conjunto de Datos")
    st.dataframe(df, use_container_width=True)
    st.metric("Consumo Total", f"{df['Consumo_kWh'].sum()} kWh")

with tab2:
    st.subheader("Evolución del Consumo")
    fig = px.line(df, x='Mes', y='Consumo_kWh', markers=True)
    st.plotly_chart(fig)

with tab3:
    st.subheader("Desglose Financiero")
    fig = px.bar(df, x='Mes', y='Coste', color='Mes')
    st.plotly_chart(fig)