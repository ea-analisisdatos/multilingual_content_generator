# Archivo: multilingual_content_generator/services/pixabay_retriever.py

# Importamos las bibliotecas necesarias
import requests  # Para realizar solicitudes HTTP
from multilingual_content_generator.config import Config  # Configuración del proyecto

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
    # Validar que la clave de API está configurada
    if not Config.PIXABAY_API_KEY:
        raise ValueError("La clave de API de Pixabay no está configurada en Config.")

    # Construir la URL de solicitud a la API de Pixabay
    url = f"https://pixabay.com/api/?key={Config.PIXABAY_API_KEY}&q={query}&image_type=photo&per_page={num_results}"
    
    try:
        # Realizar la solicitud HTTP
        response = requests.get(url)
        response.raise_for_status()  # Lanza una excepción si hay un error HTTP
        
        # Procesar la respuesta de la API
        data = response.json()
        if "hits" in data and data["hits"]:
            return [img["webformatURL"] for img in data["hits"]]
        else:
            return []  # Retornar lista vacía si no hay resultados
    
    except requests.exceptions.RequestException as e:
        raise ValueError(f"Error al conectarse con la API de Pixabay: {e}")
    except ValueError as e:
        raise ValueError(f"Error al procesar los datos de la API de Pixabay: {e}")
