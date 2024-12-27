import requests
from multilingual_content_generator.config import Config

def fetch_image(query):
    """
    Busca una imagen relevante en Pixabay utilizando una consulta textual.

    Args:
        query (str): Palabra clave o tema para buscar imágenes.

    Returns:
        str: URL de la imagen más relevante encontrada o None si no hay resultados.
    """
    # Construir la URL de la API con el query proporcionado y la clave de Pixabay
    url = f"https://pixabay.com/api/?key={Config.PIXABAY_API_KEY}&q={query}&image_type=photo"
    # Realizar una solicitud GET a la API
    response = requests.get(url)
    if response.status_code == 200:  # Verificar si la solicitud fue exitosa
        # Extraer los resultados del JSON de respuesta
        results = response.json().get("hits", [])
        if results:  # Si hay imágenes disponibles, retornar la primera URL
            return results[0]["webformatURL"]
    # Retornar None si no hay resultados
    return None
