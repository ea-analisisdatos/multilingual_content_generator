# Archivo: multilingual_content_generator/services/unsplash_retriever.py
# Servicio para interactuar con la API de Unsplash.

import requests  # Para realizar solicitudes HTTP
from multilingual_content_generator.utils.api_limits import get_limit  # Obtener límites de API
from multilingual_content_generator.config import Config  # Configuración del proyecto


def fetch_unsplash_images(query, num_results=5):
    """
    Busca imágenes en Unsplash según un término de búsqueda.

    Args:
        query (str): Término de búsqueda para imágenes.
        num_results (int): Número de resultados deseados (máximo 30).

    Returns:
        list: Lista de URLs de las imágenes encontradas.

    Raises:
        ValueError: Si el número de resultados excede el límite permitido.
        requests.HTTPError: Si la solicitud a la API de Unsplash falla.
    """
    try:
        # Validar el límite de solicitudes de la API
        limit = get_limit("unsplash")["requests_per_hour"]
        if num_results > limit:
            raise ValueError(f"El límite de solicitudes por hora es {limit}.")

        # Construir la solicitud a Unsplash
        url = "https://api.unsplash.com/search/photos"
        headers = {"Authorization": f"Client-ID {Config.UNSPLASH_ACCESS_KEY}"}
        params = {"query": query, "per_page": num_results}

        # Hacer la solicitud HTTP
        response = requests.get(url, headers=headers, params=params)
        response.raise_for_status()

        # Parsear y devolver resultados
        return [result["urls"]["regular"] for result in response.json().get("results", [])]

    except requests.HTTPError as http_err:
        raise requests.HTTPError(f"Error en la solicitud a Unsplash: {http_err}")

    except Exception as e:
        raise ValueError(f"Error inesperado al recuperar imágenes de Unsplash: {e}")
