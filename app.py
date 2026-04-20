import streamlit as st
import pandas as pd
import plotly.express as px

pg_intro = st.Page("introduccion.py", title="Introduccion")

# Paginas EDA
pg1 = st.Page("seccion/pg1.py", title="Primeros Pasos")
pg2 = st.Page("seccion/pg2.py", title="Segundo pasos")

navigation_env = st.navigation(
    {
        "": [pg_intro],
        "seccion" : [pg1,pg2]
    }
)

navigation_env.run()