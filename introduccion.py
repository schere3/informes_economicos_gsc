import streamlit as st

pg_intro =st.Page("intro.py", title="Introducción")

# Paginas 
pg1 = st.Page("seccion\intro1.py", title="Primeros pasos")
pg2 = st.Page("seccion\intro2.py", title="Segundos pasos")

navigation_env = st.navigation(
  {
    "": [pg_intro],
    "Intro 2": [pg1,pg2]
  }
)
navigation_env.run()
