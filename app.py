import streamlit as st
from PIL import Image
import base64

# Función para mostrar la imagen de fondo
def add_background_image(image_file):
    with open(image_file, "rb") as image:
        encoded_image = base64.b64encode(image.read()).decode()
        st.markdown(
            f"""
            <style>
            .stApp {{
                background-image: url("data:image/png;base64,{encoded_image}");
                background-size: 80% auto;
                background-repeat: no-repeat;
                background-position: center;
                height: 100vh;
            }}
            </style>
            """,
            unsafe_allow_html=True
        )

# Llamar a la función para añadir la imagen de fondo
add_background_image("images/Iniciar Sesion.png")

# Contenido del formulario de inicio de sesión
st.markdown("<h2 style='text-align: center; color: white;'>Sistema de Login</h2>", unsafe_allow_html=True)

# Crear formulario de inicio de sesión
usuario = st.text_input("Usuario", "")
contrasena = st.text_input("Contraseña", type='password')

if st.button("Iniciar sesión"):
    st.success(f"Bienvenido {usuario}")
