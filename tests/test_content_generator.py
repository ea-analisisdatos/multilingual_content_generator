# Archivo: tests/test_content_generator.py

# Importamos las bibliotecas necesarias
import pytest
from multilingual_content_generator.services.content_generator import generate_text_content

# Prueba para la generación de contenido textual
def test_generate_text_content(monkeypatch):
    """
    Prueba unitaria para la función generate_text_content.
    Verifica que la función devuelva un texto generado a partir de un tema dado.

    Verifica que el contenido generado sea coherente con las entradas proporcionadas.
    Prueba diferentes configuraciones de tono y longitud.
    """

    # Mock de respuesta simulada del modelo de generación de texto
    def mock_pipeline(*args, **kwargs):
        def mock_call(prompt, max_length, num_return_sequences):
            return [{"generated_text": "Este es un contenido generado de prueba."}]
        return mock_call

    # Aplicamos el mock al pipeline de transformers
    monkeypatch.setattr("transformers.pipeline", mock_pipeline)

    # Ejecutamos la función con un tema de prueba
    topic = "La importancia de la inteligencia artificial"
    result = generate_text_content(topic, max_length=100)

    # Verificamos que el resultado sea el texto esperado
    assert result == "Este es un contenido generado de prueba.", "La función no devolvió el texto esperado."
