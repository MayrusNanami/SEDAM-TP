import streamlit as st
from PIL import Image
import base64

# Función para agregar la imagen de fondo y ajustarla al 100% de la pantalla
def set_background(png_file):
    with open(png_file, "rb") as f:
        data = f.read()
        b64 = base64.b64encode(data).decode()
        st.markdown(
            f"""
            <style>
            .stApp {{
                background-image: url("data:image/png;base64,{b64}");
                background-size: 100% 100%;  /* Ajustar la imagen al 100% de la pantalla */
                background-repeat: no-repeat;
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
            .btn-exit {{
                position: absolute;
                bottom: 20px;
                left: 20px;
                background-color: #FF5555;
                color: white;
                padding: 10px;
                border-radius: 5px;
                font-size: 14px;
            }}
            </style>
            """,
            unsafe_allow_html=True
        )

# Llamar a la función para establecer la imagen de fondo
def login():
    set_background("images/Fondo cuatro.png")

    # Contenedor de login
    st.markdown('<div class="login-container">', unsafe_allow_html=True)

    # Logo de la empresa
    logo = Image.open("images/Logoo.png")
    st.image(logo, width=240)

    # Título del sistema de login
    st.markdown("<h2>Sistema de Login</h2>", unsafe_allow_html=True)

    # Inputs de usuario y contraseña
    usuario = st.text_input("Usuario", placeholder="admin", key="user", label_visibility="collapsed")
    contrasena = st.text_input("Contraseña", type='password', placeholder="********", key="pass", label_visibility="collapsed")

    # Botón de inicio de sesión
    if st.button("Iniciar sesión"):
        if usuario == "admin" and contrasena == "admin":  # Simple check for this example
            st.session_state['logged_in'] = True
        else:
            st.error("Usuario o contraseña incorrectos")

    # Enlaces adicionales
    st.markdown('<p>¿Olvidaste tu contraseña?</p>', unsafe_allow_html=True)
    st.markdown('<p>¿No tienes una cuenta? <a href="#">Registrarte</a></p>', unsafe_allow_html=True)

    # Cerrar el contenedor
    st.markdown('</div>', unsafe_allow_html=True)


def inicio():
    set_background("images/Inicio.png")  # Aquí ajustamos la imagen de fondo a Inicio.png

    # Mostrar opciones de navegación o contenido del inicio
    st.markdown('<h2>Bienvenido al sistema</h2>', unsafe_allow_html=True)

    # Botón de salir
    if st.button("Salir"):
        st.session_state['logged_in'] = False


# Estado inicial
if 'logged_in' not in st.session_state:
    st.session_state['logged_in'] = False

# Verificación de si el usuario está logeado
if st.session_state['logged_in']:
    inicio()
else:
    login()
