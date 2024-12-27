import streamlit as st
from multilingual_content_generator.services.content_generator import generate_content
from multilingual_content_generator.services.image_retriever import fetch_image
from multilingual_content_generator.config import Config

# Título de la aplicación en la interfaz de usuario
st.title("Generador de Contenido Multilingüe")

# Menú desplegable para seleccionar la plataforma de destino
platform = st.selectbox("Selecciona la plataforma", ["Blog", "LinkedIn", "Twitter"])
# Menú desplegable para seleccionar el idioma
language = st.selectbox("Selecciona el idioma", Config.SUPPORTED_LANGUAGES)
# Entrada de texto para que el usuario proporcione el tema del contenido
topic = st.text_input("Tema del contenido")
# Menú desplegable para seleccionar el tono del contenido
tone = st.selectbox("Selecciona el tono", ["Profesional", "Casual", "Amistoso"])

# Botón para generar contenido
if st.button("Generar Contenido"):
    with st.spinner("Generando contenido..."):  # Mostrar un spinner mientras se genera el contenido
        # Crear un prompt basado en las entradas del usuario
        prompt = f"Escribe un artículo sobre {topic} en un tono {tone.lower()} para {platform} en {language}"
        # Generar el contenido utilizando el servicio correspondiente
        content = generate_content(prompt)
        # Mostrar el contenido generado en un cuadro de texto
        st.text_area("Contenido Generado", content, height=200)

        # Buscar una imagen relacionada con el tema
        image_url = fetch_image(topic)
        if image_url:
            # Mostrar la imagen encontrada con un pie de foto
            st.image(image_url, caption="Imagen sugerida")
        else:
            # Mostrar una advertencia si no se encuentra una imagen
            st.warning("No se encontró una imagen relacionada.")
