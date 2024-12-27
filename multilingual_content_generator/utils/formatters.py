def format_prompt(topic, platform, tone, language):
    """
    Formatea un prompt basado en los parámetros proporcionados por el usuario.

    Args:
        topic (str): Tema o asunto principal del contenido.
        platform (str): Plataforma de destino (Blog, LinkedIn, etc.).
        tone (str): Tono deseado para el contenido (Profesional, Casual, etc.).
        language (str): Idioma del contenido.

    Returns:
        str: Prompt formateado para la generación de contenido.
    """
    # Construir el prompt utilizando los parámetros del usuario
    return f"Escribe un artículo sobre {topic} en un tono {tone} para {platform} en {language}."
