# Archivo: tests/test_dalle_generator.py

# Importamos las bibliotecas necesarias
import pytest
from multilingual_content_generator.services.dalle_generator import generate_dalle_image

# Prueba para verificar la generación de imágenes con DALL-E
def test_generate_dalle_image(monkeypatch):
    """
    Prueba unitaria para la función generate_dalle_image.
    Verifica que la función devuelva una imagen válida cuando se le proporciona un prompt.
    """
    # Mock de respuesta simulada de la función
    def mock_pipeline(prompt):
        return [{"images": ["fake_image_url"]}]

    # Aplicamos el mock al pipeline
    monkeypatch.setattr("transformers.pipeline", lambda *args, **kwargs: mock_pipeline)

    # Ejecutamos la función con un prompt de prueba
    prompt = "Un robot programando en un portátil"
    result = generate_dalle_image(prompt)

    # Verificamos que el resultado no sea None y sea una URL de imagen válida
    assert result == "fake_image_url", "La función no devolvió la imagen esperada."
