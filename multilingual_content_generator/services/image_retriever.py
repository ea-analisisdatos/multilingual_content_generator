# Archivo: services/image_retriever.py
import requests
from multilingual_content_generator.config import Config

def fetch_images(query, num_results=5):
    """
    Busca imágenes en Pixabay.
    Args:
        query (str): Término de búsqueda.
        num_results (int): Número de resultados deseados.
    Returns:
        list: Lista de URLs de imágenes.
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
