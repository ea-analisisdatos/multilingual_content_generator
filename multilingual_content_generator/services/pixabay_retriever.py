# Archivo: multilingual_content_generator/services/pixabay_retriever.py

import requests
from multilingual_content_generator.config import Config
from multilingual_content_generator.utils.api_limits import get_limit

import os

PIXABAY_API_KEY = os.getenv("PIXABAY_API_KEY")
if not PIXABAY_API_KEY:
    raise ValueError("La clave de Pixabay no está configurada.")

def fetch_pixabay_images(query, num_results=5):
    """
    Busca imágenes en Pixabay utilizando la API.
    
    Args:
        query (str): Término de búsqueda.
        num_results (int): Número de resultados deseados.
    
    Returns:
        list: Lista de URLs de imágenes.
    
    Raises:
        ValueError: Si no se encuentra la clave de API o ocurre un error en la solicitud.
    """
    # Validar límite de solicitudes
    limit = get_limit("pixabay").get("requests_per_hour", None)
    if limit is not None and num_results > limit:
        raise ValueError(f"El límite de solicitudes por hora es {limit}.")

    # Construir la URL de solicitud
    url = f"https://pixabay.com/api/?key={PIXABAY_API_KEY}&q={query}&per_page={num_results}"

    try:
        response = requests.get(url)
        response.raise_for_status()  # Lanza una excepción si hay error HTTP

        data = response.json()
        if "hits" in data and data["hits"]:
            return [img["webformatURL"] for img in data["hits"]]
        return []  # Lista vacía si no hay resultados

    except requests.exceptions.RequestException as e:
        raise ValueError(f"Error al conectarse con la API de Pixabay: {e}")
    except ValueError as e:
        raise ValueError(f"Error al procesar los datos de la API de Pixabay: {e}")
