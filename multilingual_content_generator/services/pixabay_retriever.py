# Archivo: services/pixabay_retriever.py

# Importamos las bibliotecas necesarias
import requests  # Para realizar solicitudes HTTP
from multilingual_content_generator.config import Config  # Configuración del proyecto

def fetch_pixabay_images(query, num_results=5):
    """
    Busca imágenes en Pixabay.
    Args:
        query (str): Término de búsqueda.
        num_results (int): Número de resultados deseados.
    Returns:
        list: Lista de URLs de imágenes o un mensaje de error.
    Raises:
        ValueError: Si no se encuentra la clave de API o la respuesta tiene un error.
    """
    if not Config.PIXABAY_API_KEY:
        raise ValueError("La clave de API de Pixabay no está configurada en Config.")

    # Construir la URL de la solicitud a la API de Pixabay
    url = f"https://pixabay.com/api/?key={Config.PIXABAY_API_KEY}&q={query}&image_type=photo&per_page={num_results}"
    
    try:
        # Realizar la solicitud GET a la API
        response = requests.get(url)
        response.raise_for_status()  # Lanza una excepción si hay un error HTTP
        
        # Extraer resultados de la respuesta JSON
        data = response.json()
        if "hits" in data and data["hits"]:
            # Devolver una lista de URLs de las imágenes encontradas
            return [img["webformatURL"] for img in data["hits"]]
        else:
            return []  # Si no hay resultados, retornar lista vacía
    
    except requests.exceptions.RequestException as e:
        raise ValueError(f"Error al conectarse con la API de Pixabay: {e}")
    except ValueError as e:
        raise ValueError(f"Error al procesar los datos de la API de Pixabay: {e}")
