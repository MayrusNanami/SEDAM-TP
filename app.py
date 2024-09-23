import streamlit as st
from PIL import Image
import base64

# Función para agregar la imagen de fondo
def set_background(png_file):
    with open(png_file, "rb") as f:
        data = f.read()
        b64 = base64.b64encode(data).decode()
        st.markdown(
            f"""
            <style>
            .stApp {{
                background-image: url("data:image/Fondo dos.png;base64,{b64}");
                background-size: cover;
                background-position: center;
                height: 100vh;
            }}
            .login-container {{
                background-color: rgba(255, 255, 255, 0.9);  /* Fondo blanco con transparencia */
                padding: 40px;
                border-radius: 10px;
                width: 350px;
                box-shadow: 0px 4px 15px rgba(0, 0, 0, 0.1);
                text-align: center;
                margin: auto;
                display: flex;
                flex-direction: column;
                align-items: center;
            }}
            .login-container h2 {{
                color: #333;
                margin-bottom: 30px;
            }}
            .login-container img {{
                display: block;
                margin-bottom: 20px;
            }}
            .login-container .stButton button {{
                width: 100%;
                background-color: #007BFF;
                color: white;
                border-radius: 5px;
                padding: 10px;
                font-size: 16px;
            }}
            .login-container .input-field {{
                width: 100%;
                margin-bottom: 10px;
            }}
            .login-container p {{
                color: #555;
            }}
            .login-container a {{
                color: #007BFF;
                text-decoration: none;
            }}
            </style>
            """,
            unsafe_allow_html=True
        )

# Llamar a la función para establecer la imagen de fondo
set_background("images/Fondo dos.png")

# Contenedor de login
st.markdown('<div class="login-container">', unsafe_allow_html=True)

# Logo de la empresa
logo = Image.open("images/Logoo.png")  # Asegúrate de que esta sea la ruta correcta a tu imagen
st.image(logo, width=120)

# Título del sistema de login
st.markdown("<h2>Sistema de Login</h2>", unsafe_allow_html=True)

# Inputs de usuario y contraseña
usuario = st.text_input("Usuario", placeholder="admin", key="user", label_visibility="collapsed")
contrasena = st.text_input("Contraseña", type='password', placeholder="********", key="pass", label_visibility="collapsed")

# Botón de inicio de sesión
if st.button("Iniciar sesión"):
    st.success(f"Bienvenido {usuario}")

# Enlaces adicionales
st.markdown('<p>¿Olvidaste tu contraseña?</p>', unsafe_allow_html=True)
st.markdown('<p>¿No tienes una cuenta? <a href="#">Registrarte</a></p>', unsafe_allow_html=True)

# Cerrar el contenedor
st.markdown('</div>', unsafe_allow_html=True)
