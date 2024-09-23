from PIL import Image
import streamlit as st

# Cargar imagen desde la carpeta correcta
imagen_inicio_sesion = Image.open('images/Iniciar Sesion.png')

# Mostrar la imagen en pantalla completa
st.image(imagen_inicio_sesion, use_column_width=True)

