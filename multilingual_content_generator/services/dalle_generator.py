# Archivo: services/dalle_generator.py

# Importamos las bibliotecas necesarias
from transformers import pipeline  # Para interactuar con modelos de Hugging Face
from dotenv import load_dotenv  # Para cargar las variables de entorno desde un archivo .env
import os  # Para manejar variables de entorno

# Cargar las variables de entorno desde el archivo .env
load_dotenv()

# Obtener el token de Hugging Face desde las variables de entorno
token = os.getenv("HUGGINGFACE_TOKEN")

if not token:
    raise ValueError("El token de Hugging Face no está configurado o no se pudo cargar desde el archivo .env.")

def generate_dalle_image(prompt):
    """
    Genera una imagen basada en texto usando un modelo DALL-E compatible.
    Args:
        prompt (str): Descripción de la imagen que se desea generar.
    Returns:
        str: URL de la imagen generada, o None si no se genera una imagen.
    """
    # Inicializamos el pipeline para el modelo "dalle-mega" con autenticación
    dalle = pipeline("text-to-image", model="dalle-mega", use_auth_token=token)

    # Generamos la imagen usando el prompt proporcionado
    result = dalle(prompt)

    # Verificamos si el resultado contiene imágenes y retornamos la primera imagen generada
    if result and "images" in result[0]:
        return result[0]["images"][0]
    
    # Si no se genera ninguna imagen, retornamos None
    return None
