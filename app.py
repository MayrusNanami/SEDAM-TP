import streamlit as st
from PIL import Image
import base64

# Función para mostrar el fondo azul y el logo
def add_background_image(image_file):
    with open(image_file, "rb") as image:
        encoded_image = base64.b64encode(image.read()).decode()
st.markdown(
    """
    <style>
    body {
        background-color: #004080; /* Fondo azul */
    }
    .login-container {
        background-color: white;
        padding: 50px;
        border-radius: 10px;
        box-shadow: 0px 0px 10px rgba(0, 0, 0, 0.1);
        text-align: center;
        width: 350px;
        margin: 0 auto;
    }
    .login-container img {
        width: 150px;
        margin-bottom: 20px;
    }
    </style>
    """,
    unsafe_allow_html=True
)





# Colocar el contenido dentro de la caja blanca
with st.container():
    
    # Llamar a la función para añadir la imagen de fondo 
    # Añade el fondo del logo
    add_background_image("images/Logoo.png")
    
    # Logo de la empresa
    logo = Image.open("images/Logoo.png")  # Ajusta la ruta de tu imagen
    st.image(logo, width=200)
    
    st.markdown('<div class="login-container">', unsafe_allow_html=True)
    
    # Mostrar el logo
    st.image(logo, use_column_width=False)

    # Título de la página
    st.markdown("<h2>Sistema de Login</h2>", unsafe_allow_html=True)

    # Campos de usuario y contraseña
    usuario = st.text_input("Usuario", "admin", key="usuario")
    contrasena = st.text_input("Contraseña", type="password", key="contrasena")

    # Botón de inicio de sesión
    if st.button("Iniciar sesión"):
        st.success(f"Bienvenido {usuario}")

    # Opciones de contraseña olvidada y registro
    st.markdown('<a href="#">¿Olvidaste tu contraseña?</a>', unsafe_allow_html=True)
    st.markdown('<a href="#">¿No tienes una cuenta? <b>Registrarte</b></a>', unsafe_allow_html=True)
    
    st.markdown('</div>', unsafe_allow_html=True)
