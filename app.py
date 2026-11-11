import streamlit as st
import pandas as pd

st.set_page_config(page_title="Buscador de Terminales GETNET", layout="wide")

st.title("🔍 Buscador de Locales y Terminales GETNET")

@st.cache_data
def cargar_datos():
    # Cargar y limpiar columnas vacías
    df = pd.read_excel("Terminal Code Locales GETNET.xlsx")
    df = df.dropna(how='all', axis=1)
    return df

df = cargar_datos()

# Buscador global
busqueda = st.text_input("Ingrese ID, Nombre del Local, Serial POS o Código de Terminal:")

if busqueda:
    # Filtrar en todas las columnas
    mask = df.astype(str).apply(lambda row: row.str.contains(busqueda, case=False, na=False)).any(axis=1)
    resultado = df[mask]
    st.write(f"Se encontraron {len(resultado)} resultados:")
    st.dataframe(resultado, use_container_width=True)
else:
    st.dataframe(df, use_container_width=True)