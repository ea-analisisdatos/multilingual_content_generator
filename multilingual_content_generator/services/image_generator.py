# Archivo: services/image_generator.py
from diffusers import StableDiffusionPipeline

def generate_stable_diffusion_image(prompt):
    """
    Genera una imagen usando Stable Diffusion.
    Args:
        prompt (str): Descripción de la imagen a generar.
    Returns:
        PIL.Image: Imagen generada.
    """
    model_id = "CompVis/stable-diffusion-v1-4"
    pipeline = StableDiffusionPipeline.from_pretrained(model_id)
    pipeline.to("cuda")  # Usar GPU si está disponible
    image = pipeline(prompt).images[0]
    return image

 #def generate_dalle_image(prompt):
#    """
#   Genera una imagen basada en texto usando un modelo IA como DALL-E.
#    Actualmente, esta función es un marcador de posición.
#    """
#    # TODO: Integra la generación de imágenes con DALL-E o Stable Diffusion aquí
#    return None # Actualiza esta función para integrar el modelo

def generate_dalle_image(prompt):
    """
    Genera una imagen basada en texto usando un modelo IA como DALL-E..
    """
    dalle = pipeline("text-to-image", model="dalle-mini")

    return dalle(prompt)[0]["image"]

# Agrega funciones similares para Stable Diffusion y Unsplash