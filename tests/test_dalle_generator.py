# tests/test_dalle_generator.py

import sys
import os

# Agregar el directorio 'multilingual_content_generator/services' al path
sys.path.append(os.path.join(os.path.dirname(__file__), "../multilingual_content_generator/services"))

from dalle_generator import generate_dalle_image
import pytest

def test_generate_dalle_image(monkeypatch):
    """
    Prueba unitaria para la función generate_dalle_image del archivo dalle_generator.py.
    Verifica que el pipeline de Hugging Face se llame correctamente con un mock.
    """

    # Mock para reemplazar el pipeline de transformers
    def mock_pipeline(task, model=None, use_auth_token=None):
        # Asegurarse de que el token de autenticación esté presente
        assert use_auth_token is not None, "El token de autenticación no fue proporcionado."

        class MockDallePipeline:
            def __call__(self, prompt, *args, **kwargs):
                # Simula la respuesta de la API de Hugging Face
                return [{"images": ["https://mocked.image.url"]}]

        return MockDallePipeline()

    # Aplicar el mock al pipeline
    monkeypatch.setattr("transformers.pipeline", mock_pipeline)

    # Texto de prueba para generar una imagen
    prompt = "Un robot programando en un portátil"

    # Ejecutar la función y verificar el resultado
    result = generate_dalle_image(prompt)
    assert result == "https://mocked.image.url", "La URL de la imagen generada no coincide con el mock."
