# Archivo: tests/test_translation_service.py

# Importamos las bibliotecas necesarias
import pytest
from multilingual_content_generator.services.translation_service import translate_text

# Prueba para el servicio de traducción
def test_translate_text(monkeypatch):
    """
    Prueba unitaria para la función translate_text.
    Verifica que la función traduzca un texto correctamente.
    
    Asegura que los textos sean traducidos al idioma deseado correctamente.
    """

    # Mock de respuesta simulada del servicio de traducción
    def mock_pipeline(*args, **kwargs):
        def mock_call(text, **kwargs):
            return [{"translation_text": "Este es un texto traducido de prueba."}]
        return mock_call

    # Aplicamos el mock al pipeline de transformers
    monkeypatch.setattr("transformers.pipeline", mock_pipeline)

    # Ejecutamos la función con un texto de prueba
    text = "This is a test text."
    result = translate_text(text, target_language="es")

    # Verificamos que el resultado sea el texto traducido esperado
    assert result == "Este es un texto traducido de prueba.", "La traducción no es correcta."
