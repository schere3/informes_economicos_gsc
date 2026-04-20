import streamlit as st
import pandas as pd
import plotly.express as px

# Asignación de páginas
pg_intro = st.Page("introduccion.py", title="Informes Económicos")   # Introducción
pg1 = st.Page("pred_electricidad.py", title="Predicción Gastos de Electricidad 2026")  # gastos electricidad
# seccion gastos electricidad
pg_1 = st.Page("seccion/pg1.py", title="Primeros Pasos")
pg_2 = st.Page("seccion/pg2.py", title="Segundo pasos")
pg2 = st.Page("materialesfungibles.py", title="Gestión de materiales fungibles")       # materiales fungibles
pg3 = st.Page("maquinas_vending.py", title="Máquinas Vending")                         # maquinas vending
pg4 = st.Page("suministro_agua.py", title="Concurso de Suministro de Agua")            # suministro de agua
pg5 = st.Page("datos_sinteticos.py", title="Generación de Datos Sintéticos")           # datos sinteticos

navigation_env = st.navigation(
    {
        "": [pg_intro],
        "Gastos de electricidad 2026" : [pg1],
        "Sección": [pg_1,pg_2],
        "Gestión de materiales fungibles": [pag2],
        "Máquinas Vending": [pag3],
        "Concurso de Suministro de Agua": [pag4],
        "Generación de Datos Sintéticos": [pag5]
    }
)
navigation_env.run()