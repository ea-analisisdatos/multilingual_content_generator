from multilingual_content_generator.services.content_generator import generate_content

def test_generate_content():
    """
    Prueba que la función de generación de contenido devuelva un texto válido.
    """
    # Crear un prompt de prueba para verificar la generación
    prompt = "Escribe un artículo sobre Inteligencia Artificial."
    # Llamar a la función de generación de contenido
    content = generate_content(prompt)
    # Verificar que el contenido es una cadena no vacía
    assert isinstance(content, str)
    assert len(content) > 0
