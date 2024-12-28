# Archivo: multilingual_content_generator/services/dalle_generator.py

# Importamos las bibliotecas necesarias
from transformers import pipeline  # Para interactuar con el modelo de Hugging Face
from multilingual_content_generator.config import Config  # Configuración del proyecto
import os

def generate_dalle_image(prompt):
    """
    Genera una imagen a partir de un texto utilizando el pipeline de Hugging Face.
    Args:
        prompt (str): Descripción de la imagen a generar.
    Returns:
        str: URL de la imagen generada.
    """
    # Recuperar el token de autenticación de Hugging Face desde las variables de entorno
    HUGGINGFACE_TOKEN = os.getenv('HUGGINGFACE_TOKEN')
    if not HUGGINGFACE_TOKEN:
        raise ValueError("El token HUGGINGFACE_TOKEN no está configurado en el archivo .env.")

    # Configuración del pipeline para generación de imágenes
    dalle = pipeline(
        "text-to-image",
        model="CompVis/stable-diffusion-v1-4",
        use_auth_token=HUGGINGFACE_TOKEN
    )

    # Generar la imagen
    result = dalle(prompt)
    if not result or "images" not in result[0]:
        raise ValueError("No se pudo generar la imagen.")
    
    return result[0]["images"]
