import streamlit as st
from PIL import Image
import base64

# Función para mostrar el fondo azul y el logo
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
            .login-container {{
                display: flex;
                flex-direction: column;
                align-items: center;
                justify-content: center;
                height: 100vh;
                text-align: center;
            }}
            .logo-img {{
                margin-bottom: 20px;
                width: 150px;
            }}
            .btn {{
                background-color: #007BFF;
                color: white;
                padding: 10px;
                font-size: 16px;
                border-radius: 5px;
                margin-top: 10px;
            }}
            </style>
            """,
            unsafe_allow_html=True
        )

# Llamar a la función para añadir la imagen de fondo (si es necesario)
# Añade el fondo del logo, por ejemplo "images/Iniciar Sesion.png"
add_background_image("images/Iniciar Sesion.png")

# Logo de la empresa
logo = Image.open("images/Iniciar Sesion.png")  # Ajusta la ruta de tu imagen
st.image(logo, width=200)

# Contenido del formulario de inicio de sesión
st.markdown("<h2 style='color: white;'>Sistema de Login</h2>", unsafe_allow_html=True)

# Crear formulario de inicio de sesión
usuario = st.text_input("Usuario", placeholder="admin")
contrasena = st.text_input("Contraseña", type='password', placeholder="********")

# Botón de inicio de sesión
if st.button("Iniciar sesión", key="login"):
    st.success(f"Bienvenido {usuario}")

# Enlaces adicionales
st.markdown('<p style="color: white;">¿Olvidaste tu contraseña?</p>', unsafe_allow_html=True)
st.markdown('<p style="color: white;">¿No tienes una cuenta? <a href="#" style="color: #007BFF;">Registrarte</a></p>', unsafe_allow_html=True)
