# Archivo: multilingual_content_generator/services/dalle_generator.py
# Servicio para generar imágenes utilizando Stable Diffusion.

from diffusers import StableDiffusionPipeline
from multilingual_content_generator.config import Config
from multilingual_content_generator.utils.api_limits import get_limit

import torch

def generate_dalle_image(prompt):
    """
    Genera una imagen usando Stable Diffusion.
    
    Args:
        prompt (str): Descripción de la imagen a generar.
        
    Returns:
        str: Ruta local de la imagen generada.
        
    Raises:
        ValueError: Si no se configura el token de Hugging Face.
    """
    if not Config.HUGGINGFACE_TOKEN:
        raise ValueError("El token de HuggingFace no está configurado en Config.")

    # Validar límite de uso de Hugging Face (opcional según las configuraciones)
    limit = get_limit("huggingface").get("token_limits", None)
    if limit is not None and not validate_huggingface_limit(limit):
        raise ValueError("Límite de uso de Hugging Face excedido.")

    # Configurar el pipeline
    pipe = StableDiffusionPipeline.from_pretrained(
        "CompVis/stable-diffusion-v1-4", use_auth_token=Config.HUGGINGFACE_TOKEN
    )
    pipe.to("cuda" if torch.cuda.is_available() else "cpu")

    # Generar la imagen
    image = pipe(prompt).images[0]

    # Guardar la imagen generada
    output_path = "/tmp/generated_image.png"
    image.save(output_path)

    return output_path

def validate_huggingface_limit(limit):
    """
    Valida el límite de uso para la API de Hugging Face.
    (Implementar lógica según las métricas disponibles en Hugging Face).
    """
    return True  # Ejemplo simplificado
