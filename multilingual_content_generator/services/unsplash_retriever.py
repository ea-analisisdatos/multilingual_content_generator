# Archivo: services/unsplash_retriever.py

# Importamos las bibliotecas necesarias
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
    """
    # Construir la URL de la solicitud a la API de Unsplash
    url = f"https://api.unsplash.com/search/photos?query={query}&per_page={num_results}&client_id={Config.UNSPLASH_API_KEY}"
    
    # Realizar la solicitud GET a la API
    response = requests.get(url)
    
    # Verificar si la solicitud fue exitosa
    if response.status_code == 200:
        # Extraer resultados de la respuesta JSON
        data = response.json()
        if "results" in data:
            # Devolver una lista de URLs de las imágenes encontradas
            return [img["urls"]["regular"] for img in data["results"]]
    
    # Si la solicitud falla o no hay resultados, retornar una lista vacía
    return []
