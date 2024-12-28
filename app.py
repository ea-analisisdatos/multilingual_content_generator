    # Archivo: app.py

# Importamos las bibliotecas necesarias
import streamlit as st  # Para crear la interfaz gráfica
from multilingual_content_generator.services.pixabay_retriever import fetch_pixabay_images  # Para buscar imágenes en Pixabay
from multilingual_content_generator.services.unsplash_retriever import fetch_unsplash_images  # Para buscar imágenes en Unsplash
from multilingual_content_generator.services.dalle_generator import generate_dalle_image  # Para generar imágenes con DALL-E
from multilingual_content_generator.services.stable_diffusion import generate_stable_diffusion_image  # Para generar imágenes con Stable Diffusion
from multilingual_content_generator.config import Config  # Configuración del proyecto

# Configuración de la aplicación
st.title("Generador de Contenido Multilingüe con Imágenes")
st.subheader("Busca imágenes o genera contenido visual usando IA")

# Selección de la fuente de imágenes
image_source = st.selectbox(
    "Selecciona la fuente de imágenes:",
    ["Pixabay", "Unsplash", "DALL-E", "Stable Diffusion"]
)

# Entrada para el tema o descripción
image_query = st.text_input("Describe el tema o imagen que deseas:")

# Botón para obtener las imágenes
if st.button("Obtener Imágenes"):
    # Verificar la fuente seleccionada
    if image_source == "Pixabay":
        with st.spinner("Buscando imágenes en Pixabay..."):
            image_urls = fetch_pixabay_images(image_query, num_results=5)
            if image_urls:
                st.subheader("Imágenes encontradas:")
                for idx, img_url in enumerate(image_urls):
                    st.image(img_url, caption=f"Imagen {idx+1}")
            else:
                st.warning("No se encontraron imágenes para la consulta.")
    
    elif image_source == "Unsplash":
        with st.spinner("Buscando imágenes en Unsplash..."):
            image_urls = fetch_unsplash_images(image_query, num_results=5)
            if image_urls:
                st.subheader("Imágenes encontradas:")
                for idx, img_url in enumerate(image_urls):
                    st.image(img_url, caption=f"Imagen {idx+1}")
            else:
                st.warning("No se encontraron imágenes para la consulta.")
    
    elif image_source == "DALL-E":
        with st.spinner("Generando imágenes con DALL-E..."):
            image = generate_dalle_image(image_query)
            if image:
                st.image(image, caption="Imagen generada por DALL-E")
            else:
                st.warning("No se pudo generar la imagen. Verifica tu consulta.")
    
    elif image_source == "Stable Diffusion":
        with st.spinner("Generando imágenes con Stable Diffusion..."):
            image = generate_stable_diffusion_image(image_query)
            if image:
                st.image(image, caption="Imagen generada por Stable Diffusion")
            else:
                st.warning("No se pudo generar la imagen. Verifica tu consulta.")
