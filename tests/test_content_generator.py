# Archivo: tests/test_content_generator.py

import pytest
from multilingual_content_generator.services.content_generator import generate_content

@pytest.mark.timeout(10)
def test_generate_content():
    """
    Prueba unitaria para la función generate_content.
    Verifica que la función devuelva un texto generado basado en un tema dado.
    """

    # Mock del pipeline
    def mock_pipeline(prompt, max_length, num_return_sequences):
        return [{"generated_text": "Este es un contenido generado de prueba."}]

    # Configuración del test
    topic = "La importancia de la inteligencia artificial"
    max_length = 100

    # Llamada a la función con el mock
    result = generate_content(prompt=topic, max_length=max_length, pipeline_function=mock_pipeline)

    # Verificaciones
    assert isinstance(result, str), "El resultado no es una cadena de texto."
    assert result == "Este es un contenido generado de prueba.", "La función no devolvió el texto esperado."
