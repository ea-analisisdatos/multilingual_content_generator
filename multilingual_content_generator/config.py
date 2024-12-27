import os
from dotenv import load_dotenv

# Cargar variables de entorno desde el archivo .env
load_dotenv()

class Config:
    """
    Clase que almacena la configuración global del proyecto.
    Nota: Si alguna clave no está presente en .env, la aplicación 
    usará el valor por defecto especificado en el código.
    """
    # Clave de la API de Pixabay (recuperada desde las variables de entorno)
    PIXABAY_API_KEY = os.getenv("PIXABAY_API_KEY", "tu_clave_pixabay")
    # Modelo predeterminado para generación de contenido
    DEFAULT_MODEL = "EleutherAI/gpt-neo-1.3B"
    # Idiomas soportados para la generación de contenido
    SUPPORTED_LANGUAGES = ["es", "en", "fr", "it"]
    # Longitud máxima permitida para el contenido generado
    MAX_LENGTH = 256
