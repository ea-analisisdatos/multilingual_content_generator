# Archivo: app.py
import streamlit as st
from multilingual_content_generator.services.image_retriever import fetch_images

# Título de la aplicación
st.title("Generador de Contenido Multilingüe con Imágenes")

# Entrada para la búsqueda de imágenes
image_query = st.text_input("Introduce un tema para buscar imágenes:")

# Botón para buscar imágenes
if st.button("Buscar Imágenes"):
    with st.spinner("Buscando imágenes..."):
        # Llamar a la función fetch_images para buscar imágenes relacionadas
        image_urls = fetch_images(image_query, num_results=5)
        
        if image_urls:
            st.subheader("Imágenes encontradas:")
            # Mostrar las imágenes encontradas
            for idx, img_url in enumerate(image_urls):
                st.image(img_url, caption=f"Imagen {idx+1}")
        else:
            st.warning("No se encontraron imágenes relacionadas con la búsqueda.")
