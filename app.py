import streamlit as st
from PIL import Image
import base64

# Función para agregar el fondo azul y el contenedor blanco
def add_background_image():
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-color: #0066A2;  /* Color de fondo azul */
            height: 100vh;
            display: flex;
            justify-content: center;
            align-items: center;
        }}
        .login-container {{
            background-color: white;
            padding: 30px;
            border-radius: 15px;
            box-shadow: 0px 4px 12px rgba(0, 0, 0, 0.1);
            width: 350px;
            text-align: center;
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
        }}
        .login-container img {{
            width: 150px;
            margin-bottom: 20px;
        }}
        .login-container h2 {{
            color: #333333;
            margin-bottom: 20px;
        }}
        .login-container input {{
            margin-bottom: 10px;
            width: 100%;
            padding: 10px;
            font-size: 16px;
            border-radius: 5px;
            border: 1px solid #ddd;
        }}
        .login-container button {{
            background-color: #007BFF;
            color: white;
            padding: 10px;
            width: 100%;
            border: none;
            border-radius: 5px;
            cursor: pointer;
            font-size: 16px;
        }}
        .login-container p {{
            color: #333333;
            margin-top: 10px;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

# Aplicar el estilo
add_background_image()

# Crear el contenedor del login
st.markdown('<div class="login-container">', unsafe_allow_html=True)

# Mostrar el logo dentro del contenedor blanco
logo = Image.open("images/Logoo.png")  # Ajusta la ruta de tu imagen
st.image(logo)

# Título del login
st.markdown("<h2>Sistema de Login</h2>", unsafe_allow_html=True)

# Campos de usuario y contraseña
usuario = st.text_input("Usuario", placeholder="admin")
contrasena = st.text_input("Contraseña", type='password', placeholder="********")

# Botón de inicio de sesión
if st.button("Iniciar sesión", key="login"):
    st.success(f"Bienvenido {usuario}")

# Enlaces de ayuda dentro del contenedor
st.markdown('<p>¿Olvidaste tu contraseña?</p>', unsafe_allow_html=True)
st.markdown('<p>¿No tienes una cuenta? <a href="#" style="color: #007BFF;">Registrarte</a></p>', unsafe_allow_html=True)

# Cerrar el contenedor
st.markdown('</div>', unsafe_allow_html=True)
