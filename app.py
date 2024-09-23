import streamlit as st
from PIL import Image

# Función para agregar fondo azul y cuadro blanco para el login
def add_background_image():
    st.markdown(
        """
        <style>
        .stApp {{
            background-color: #0066A2;  /* Fondo azul */
            height: 100vh;
            display: flex;
            justify-content: center;
            align-items: center;
        }}
        .login-container {{
            background-color: white;
            padding: 40px;
            border-radius: 10px;
            width: 350px;
            box-shadow: 0px 4px 15px rgba(0, 0, 0, 0.1);
            text-align: center;
        }}
        .login-container h2 {{
            color: #333;
            margin-bottom: 30px;
        }}
        .login-container img {{
            display: block;
            margin: 0 auto 20px auto;
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

# Agregamos los estilos
add_background_image()

# Creamos el contenedor que engloba todo el contenido del login
st.markdown('<div class="login-container">', unsafe_allow_html=True)

# Mostramos el logo
logo = Image.open("images/Logoo.png")  # Asegúrate de que esta sea la ruta correcta a tu imagen
st.image(logo, width=120)

# Título del sistema de login
st.markdown("<h2>Sistema de Login</h2>", unsafe_allow_html=True)

# Inputs de usuario y contraseña dentro del contenedor
usuario = st.text_input("Usuario", placeholder="admin", key="user", label_visibility="collapsed")
contrasena = st.text_input("Contraseña", type='password', placeholder="********", key="pass", label_visibility="collapsed")

# Botón de inicio de sesión
if st.button("Iniciar sesión"):
    st.success(f"Bienvenido {usuario}")

# Enlaces de ayuda para el usuario
st.markdown('<p>¿Olvidaste tu contraseña?</p>', unsafe_allow_html=True)
st.markdown('<p>¿No tienes una cuenta? <a href="#">Registrarte</a></p>', unsafe_allow_html=True)

# Cerrar el contenedor
st.markdown('</div>', unsafe_allow_html=True)
