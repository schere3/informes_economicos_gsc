import streamlit as st
import pandas as pd
import plotly.express as px


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