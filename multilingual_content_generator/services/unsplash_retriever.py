# Archivo: multilingual_content_generator/services/unsplash_retriever.py

# Importamos las bibliotecas necesarias
import requests  # Para realizar solicitudes HTTP
from multilingual_content_generator.config import Config  # Configuración del proyecto

def fetch_unsplash_images(query, num_results=5):
    """
    Busca imágenes en Unsplash utilizando la API.
    Args:
        query (str): Término de búsqueda.
        num_results (int): Número de resultados deseados.
    Returns:
        list: Lista de URLs de imágenes.
    Raises:
        ValueError: Si no se encuentra la clave de API o ocurre un error en la solicitud.
    """
    # Validar que la clave de API está configurada
    if not Config.UNSPLASH_API_KEY:
        raise ValueError("La clave de API de Unsplash no está configurada en Config.")

    # Construir la URL de solicitud a la API de Unsplash
    url = f"https://api.unsplash.com/search/photos?query={query}&per_page={num_results}&client_id={Config.UNSPLASH_API_KEY}"
    
    try:
        # Realizar la solicitud HTTP
        response = requests.get(url)
        response.raise_for_status()  # Lanza una excepción si hay un error HTTP
        
        # Procesar la respuesta de la API
        data = response.json()
        if "results" in data:
            return [img["urls"]["regular"] for img in data["results"]]
        else:
            return []  # Retornar lista vacía si no hay resultados
    
    except requests.exceptions.RequestException as e:
        raise ValueError(f"Error al conectarse con la API de Unsplash: {e}")
    except ValueError as e:
        raise ValueError(f"Error al procesar los datos de la API de Unsplash: {e}")
