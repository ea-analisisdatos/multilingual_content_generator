# Archivo: services/image_retriever.py
import requests
from multilingual_content_generator.config import Config

def fetch_images(query, num_results=5):
    """
    Busca imágenes relevantes en Pixabay utilizando una consulta textual.

    Args:
        query (str): Palabra clave o tema para buscar imágenes.
        num_results (int): Número máximo de resultados a devolver.

    Returns:
        list: Lista de URLs de imágenes encontradas.
    """
    # Construir la URL de la solicitud a la API de Pixabay
    url = f"https://pixabay.com/api/?key={Config.PIXABAY_API_KEY}&q={query}&image_type=photo&per_page={num_results}"
    
    # Realizar la solicitud GET a la API
    response = requests.get(url)
    
    # Verificar si la solicitud fue exitosa
    if response.status_code == 200:
        # Extraer resultados de la respuesta JSON
        data = response.json()
        if "hits" in data:
            # Devolver una lista de URLs de las imágenes encontradas
            return [img["webformatURL"] for img in data["hits"]]
    
    # Si la solicitud falla o no hay resultados, retornar una lista vacía
    return []
