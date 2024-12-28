# Archivo: multilingual_content_generator/services/stable_diffusion_service.py
# Servicio principal para interactuar con Stable Diffusion.

from diffusers import StableDiffusionPipeline
from PIL import Image
import torch
import os

def configure_pipeline(token):
    """
    Configura el pipeline de Stable Diffusion.

    Args:
        token (str): Token de autenticación de Hugging Face.

    Returns:
        StableDiffusionPipeline: Pipeline configurado y listo para usar.

    Raises:
        ValueError: Si ocurre un error al configurar el pipeline.
    """
    try:
        model_id = "CompVis/stable-diffusion-v1-4"
        pipe = StableDiffusionPipeline.from_pretrained(
            model_id,
            use_auth_token=token
        )
        return pipe.to("cuda" if torch.cuda.is_available() else "cpu")
    except Exception as e:
        raise ValueError(f"Error al configurar el pipeline de Stable Diffusion: {e}")

def generate_image(pipe, prompt):
    """
    Genera una imagen utilizando el pipeline de Stable Diffusion.

    Args:
        pipe (StableDiffusionPipeline): Pipeline configurado.
        prompt (str): Descripción de la imagen a generar.

    Returns:
        PIL.Image: Imagen generada.

    Raises:
        ValueError: Si ocurre un error durante la generación de la imagen.
    """
    try:
        result = pipe(prompt)
        if not hasattr(result, "images") or not isinstance(result.images[0], Image.Image):
            raise ValueError("La salida del pipeline no contiene una imagen válida.")
        return result.images[0]
    except Exception as e:
        raise ValueError(f"Error al generar la imagen con el prompt '{prompt}': {e}")

def save_image(image, output_path):
    """
    Guarda la imagen generada en el sistema de archivos.

    Args:
        image (PIL.Image): Imagen a guardar.
        output_path (str): Ruta donde se guardará la imagen.

    Raises:
        ValueError: Si ocurre un error al guardar la imagen.
    """
    try:
        image.save(output_path)
    except Exception as e:
        raise ValueError(f"Error al guardar la imagen en '{output_path}': {e}")

def generate_stable_diffusion_image(prompt, save_to_file=False, output_path="output_image.png"):
    """
    Genera una imagen utilizando Stable Diffusion.

    Args:
        prompt (str): Descripción de la imagen a generar.
        save_to_file (bool): Si True, guarda la imagen en un archivo local. Si False, devuelve el objeto de la imagen.
        output_path (str): Ruta donde se guardará la imagen si save_to_file es True.

    Returns:
        PIL.Image or str: Imagen generada (como objeto PIL) o ruta del archivo generado.

    Raises:
        ValueError: Si ocurre algún error al generar la imagen.
    """
    try:
        # Recuperar el token desde las variables de entorno
        HUGGINGFACE_TOKEN = os.getenv("HUGGINGFACE_TOKEN")
        if not HUGGINGFACE_TOKEN or not isinstance(HUGGINGFACE_TOKEN, str):
            raise ValueError("El token HUGGINGFACE_TOKEN es inválido o no está configurado.")

        # Configurar el pipeline
        pipe = configure_pipeline(HUGGINGFACE_TOKEN)

        # Generar la imagen
        image = generate_image(pipe, prompt)

        if save_to_file:
            save_image(image, output_path)
            return output_path
        else:
            return image

    except ValueError as e:
        raise e
    except Exception as e:
        raise ValueError(f"Error inesperado al generar la imagen: {e}")
