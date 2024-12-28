# Archivo: api_limits.py
# Este archivo define los límites de uso para las diferentes APIs utilizadas en el proyecto.

# Definición de los límites de las APIs
API_LIMITS = {
    "unsplash": {"requests_per_hour": 50},  # Límite de solicitudes por hora para Unsplash
    "pixabay": {"requests_per_hour": 500},  # Límite de solicitudes por hora para Pixabay
    "huggingface": {"token_limits": "Depende del modelo y configuración de la cuenta"},  # Límite variable según Hugging Face
}

def get_limit(api_name):
    """
    Devuelve los límites para una API específica.

    Args:
        api_name (str): Nombre de la API (e.g., 'unsplash', 'pixabay', 'huggingface').

    Returns:
        dict: Diccionario con los límites definidos para la API.

    Raises:
        ValueError: Si la API solicitada no está definida.
    """
    limit = API_LIMITS.get(api_name)
    if not limit:
        raise ValueError(f"No se encontraron límites para la API '{api_name}'. Asegúrate de que esté definida en API_LIMITS.")
    return limit
