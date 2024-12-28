# Archivo: multilingual_content_generator/services/stable_diffusion.py

# Importamos las bibliotecas necesarias
from diffusers import StableDiffusionPipeline  # Para interactuar con el modelo de Stable Diffusion
from multilingual_content_generator.config import Config  # Configuración del proyecto
import torch
import os

def generate_stable_diffusion_image(prompt):
    """
    Genera una imagen utilizando Stable Diffusion.
    Args:
        prompt (str): Descripción de la imagen a generar.
    Returns:
        PIL.Image: Imagen generada.
    """
    # Recuperar el token de autenticación desde las variables de entorno
    HUGGINGFACE_TOKEN = os.getenv('HUGGINGFACE_TOKEN')
    if not HUGGINGFACE_TOKEN:
        raise ValueError("El token HUGGINGFACE_TOKEN no está configurado en el archivo .env.")

    # Configuración del modelo de Stable Diffusion
    model_id = "CompVis/stable-diffusion-v1-4"
    pipeline = StableDiffusionPipeline.from_pretrained(
        model_id,
        use_auth_token=HUGGINGFACE_TOKEN
    )

    # Asignar el pipeline a la GPU si está disponible
    device = "cuda" if torch.cuda.is_available() else "cpu"
    pipeline.to(device)

    # Generar la imagen
    result = pipeline(prompt).images[0]
    return result
