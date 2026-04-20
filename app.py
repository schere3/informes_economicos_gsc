import streamlit as st
import pandas as pd
import plotly.express as px

pg_intro = st.Page("introduccion.py", title="Introduccion")

# Paginas EDA
pg_eda_intro = st.Page("seccion_eda/intro_eda.py", title="Primeros Pasos")
pg_eda_basica = st.Page("seccion_eda/estadisticos_basicos.py", title="Segundo pasos")


navigation_env.run()