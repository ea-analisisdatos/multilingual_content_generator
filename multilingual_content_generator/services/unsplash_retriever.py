# Archivo: services/unsplash_retriever.py

import requests  # Para realizar solicitudes HTTP
from multilingual_content_generator.config import Config  # Configuración del proyecto

def fetch_unsplash_images(query, num_results=5):
    """
    Busca imágenes en Unsplash.
    Args:
        query (str): Término de búsqueda.
        num_results (int): Número de resultados deseados.
    Returns:
        list: Lista de URLs de imágenes.
    Raises:
        ValueError: Si no se encuentra la clave de API o si ocurre un error al conectarse a la API.
    """
    # Validar que la clave de API está configurada
    if not hasattr(Config, "UNSPLASH_API_KEY") or not Config.UNSPLASH_API_KEY:
        raise ValueError("La clave de API de Unsplash no está configurada en Config.")

    # Construir la URL de la solicitud a la API de Unsplash
    url = f"https://api.unsplash.com/search/photos?query={query}&per_page={num_results}&client_id={Config.UNSPLASH_API_KEY}"

    try:
        # Realizar la solicitud GET a la API
        response = requests.get(url)
        response.raise_for_status()  # Lanzar una excepción para errores HTTP

        # Extraer resultados de la respuesta JSON
        data = response.json()
        if "results" in data:
            # Devolver una lista de URLs de las imágenes encontradas
            return [img["urls"]["regular"] for img in data["results"]]
        else:
            return []  # Si no hay resultados, retornar una lista vacía

    except requests.exceptions.RequestException as e:
        raise ValueError(f"Error al conectarse con la API de Unsplash: {e}")
    except ValueError as e:
        raise ValueError(f"Error al procesar los datos de la API de Unsplash: {e}")
