import streamlit as st
import pandas as pd
import plotly.express as px

# --- FUNCIONES DE CARGA DE DATOS ---
def pagina_principal():
    st.title("Página Principal")
    st.write("Estamos antes la página principal de nuestro estudio")
    st.write("Usa el menú de la izquierda para navegar entre las páginas.")
    # Todo el contenido Markdown debe ir entre comillas triples dentro de st.markdown
    st.write("Usa el menú de la izquierda para navegar entre las páginas.")
    
    # Todo el contenido Markdown debe ir entre comillas triples dentro de st.markdown
    st.markdown("""
    ## Índice
    1. [Introducción](#introducción)
    2. [Requisitos Previos](#requisitos-previos)
    3. [Instalación y Configuración](#instalación-y-configuración)
    4. [Ir a Visualización de Datos](otra-pagina.md#requisitos-previos)
    ---
    ## Introducción
    Aquí va tu texto de introducción...
    
    ## Requisitos Previos
    Aquí los requisitos...
    
    ## Instalación y Configuración
    Pasos de instalación...
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
pagina1 = st.sidebar.selectbox("Selecciona una página", ["Página Principal", 
                                                        "Visualización de Datos",
                                                        "Gráficos Interactivos"])
if pagina1 == "Página Principal":
    pagina_principal()
elif pagina1 == "Visualización de Datos":
    visualizar_datos()
elif pagina1 == "Gráficos Interactivos":
    graficos_interactivos()

#-------------------------------------------------------------------------------------------------
# --- FUNCIONES DE CARGA DE DATOS ---
def cargar_datos_electricidad():
    # Aquí cargarías tu CSV real
    return pd.DataFrame({
        'Mes': ['Ene', 'Feb', 'Mar'],
        'Consumo_kWh': [450, 520, 480],
        'Coste': [120, 145, 130]
    })
def cargar_datos_materiales():
    return pd.DataFrame({
        'Material': ['Acero', 'Aluminio', 'Cobre'],
        'Stock': [100, 50, 30],
        'Precio_Kg': [15, 25, 40]
    })
    
# --- MÓDULO: ESTUDIO DE ELECTRICIDAD ---
def modulo_electricidad():
    st.header("⚡ Estudio de Gastos de Electricidad")
    df = cargar_datos_electricidad()

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

# --- MÓDULO: ESTUDIO DE MATERIALES ---
def modulo_materiales():
    st.header("🏗️ Estudio de Materiales")
    df = cargar_datos_materiales()

    tab1, tab2 = st.tabs(["📦 Inventario", "⚖️ Valoración"])

    with tab1:
        st.subheader("Estado del Stock")
        st.table(df)
    
    with tab2:
        st.subheader("Valoración de Mercado")
        df['Valor_Total'] = df['Stock'] * df['Precio_Kg']
        fig = px.pie(df, values='Valor_Total', names='Material', hole=0.4)
        st.plotly_chart(fig)

# --- NAVEGACIÓN PRINCIPAL (SIDEBAR) ---
st.sidebar.title("Informes")
pagina2 = st.sidebar.selectbox("Selecciona el Área de Estudio:", ["Inicio",
                                                        "Electricidad", 
                                                        "Materiales"])
if pagina2 == "Inicio":
    st.title("🚀 Panel de Control Multifuncional")
    st.write("Selecciona un área en el menú de la izquierda para comenzar el análisis detallado.")
    
elif pagina2 == "Electricidad":
    modulo_electricidad()

elif pagina2 == "Materiales":
    modulo_materiales()
