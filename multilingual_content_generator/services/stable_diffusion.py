# Archivo: services/stable_diffusion.py

# Importamos las bibliotecas necesarias
from diffusers import StableDiffusionPipeline  # Para generar imágenes con Stable Diffusion
from dotenv import load_dotenv  # Para cargar las variables de entorno desde un archivo .env
import os  # Para manejar variables de entorno

# Cargar las variables de entorno desde el archivo .env
load_dotenv()

def generate_stable_diffusion_image(prompt):
    """
    Genera una imagen usando Stable Diffusion.
    Args:
        prompt (str): Descripción de la imagen a generar.
    Returns:
        PIL.Image: Imagen generada.
    """
    # Identificador del modelo de Stable Diffusion
    model_id = "CompVis/stable-diffusion-v1-4"

    # Cargamos el pipeline del modelo
    pipeline = StableDiffusionPipeline.from_pretrained(model_id)
    
    # Movemos el pipeline a la GPU si está disponible
    pipeline.to("cuda")
    
    # Generamos la imagen con el prompt proporcionado
    image = pipeline(prompt).images[0]
    
    return image
