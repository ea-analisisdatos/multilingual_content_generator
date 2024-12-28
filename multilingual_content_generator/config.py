# config.py

import sys
from pathlib import Path

# Añadir la ruta del proyecto al path
sys.path.append(str(Path(__file__).resolve().parent))


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
    # Claves recuperadas desde las variables de entorno
    
    # Acceder a las variables
    PIXABAY_API_KEY = os.getenv("PIXABAY_API_KEY")
    UNSPLASH_ACCESS_KEY = os.getenv("UNSPLASH_ACCESS_KEY")
    HUGGINGFACE_TOKEN = os.getenv("HUGGINGFACE_TOKEN")
    PYTHONPATH = os.getenv("PYTHONPATH")

    # Modelo predeterminado para generación de contenido
    DEFAULT_MODEL = "EleutherAI/gpt-neo-1.3B"
    # Idiomas soportados para la generación de contenido
    SUPPORTED_LANGUAGES = ["es", "en", "fr", "it"]
    # Longitud máxima permitida para el contenido generado
    MAX_LENGTH = 256
