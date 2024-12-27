# Archivo: app.py
# Importamos las bibliotecas necesarias
import streamlit as st
from multilingual_content_generator.services.image_retriever import fetch_images
from multilingual_content_generator.services.image_generator import generate_dalle_image

# Configuración de la aplicación
st.title("Generador de Contenido Multilingüe con Imágenes")
st.subheader("Busca imágenes o genera contenido visual usando IA")

# Selección de la fuente de imágenes
image_source = st.selectbox(
    "Selecciona la fuente de imágenes:",
    ["Pixabay", "DALL-E", "Stable Diffusion"]
)

# Entrada para el tema o descripción
image_query = st.text_input("Describe el tema o imagen que deseas:")

# Botón para obtener las imágenes
if st.button("Obtener Imágenes"):
    # Verificar la fuente seleccionada
    if image_source == "Pixabay":
        with st.spinner("Buscando imágenes en Pixabay..."):
            # Llamamos a la función fetch_images para buscar imágenes en Pixabay
            image_urls = fetch_images(image_query, num_results=5)
            if image_urls:
                st.subheader("Imágenes encontradas:")
                # Mostrar las imágenes obtenidas
                for idx, img_url in enumerate(image_urls):
                    st.image(img_url, caption=f"Imagen {idx+1}")
            else:
                st.warning("No se encontraron imágenes para la consulta.")
    
    elif image_source == "DALL-E":
        with st.spinner("Generando imágenes con DALL-E..."):
            # Llamamos a la función generate_dalle_image para generar una imagen
            image = generate_dalle_image(image_query)
            if image:
                st.image(image, caption="Imagen generada por DALL-E")
            else:
                st.warning("No se pudo generar la imagen. Verifica tu consulta.")
    
    elif image_source == "Stable Diffusion":
        st.info("La integración con Stable Diffusion está en desarrollo. ¡Próximamente!")
