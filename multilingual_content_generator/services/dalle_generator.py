# Archivo: dalle_generator.py
from transformers import pipeline
from dotenv import load_dotenv
import os

# Cargar las variables de entorno desde el archivo .env
load_dotenv()

# Recuperar el token de autenticación de Hugging Face
HUGGINGFACE_TOKEN = os.getenv("HUGGINGFACE_TOKEN")
if not HUGGINGFACE_TOKEN:
    raise ValueError("El token HUGGINGFACE_TOKEN no está configurado en el archivo .env.")

def generate_dalle_image(prompt):
    """
    Genera una imagen a partir de un texto utilizando el pipeline de Hugging Face.

    Args:
        prompt (str): Texto para generar la imagen.

    Returns:
        str: URL de la imagen generada.
    """
    # Configuración del pipeline para generación de imágenes
    dalle = pipeline(
        "text-to-image",
        model="CompVis/stable-diffusion-v1-4",  # Cambiar al modelo válido
        use_auth_token=HUGGINGFACE_TOKEN
    )

    # Generar la imagen a partir del texto proporcionado
    result = dalle(prompt)
    if not result or "images" not in result[0]:
        raise RuntimeError("No se pudo generar la imagen.")

    # Retornar la URL de la imagen generada
    return result[0]["images"][0]
