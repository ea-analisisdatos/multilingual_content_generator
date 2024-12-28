# Archivo: tests/test_translation_service.py
# Pruebas para el servicio translation_service.py

# Importamos las bibliotecas necesarias
import pytest
from multilingual_content_generator.services.translation_service import translate_text

def test_translate_text(monkeypatch):
    """
    Prueba unitaria para la función translate_text.
    Verifica que la función traduzca un texto correctamente.
    """
    # Mock de respuesta simulada del servicio de traducción
    class MockPipeline:
        def __call__(self, text, **kwargs):
            # Devuelve una traducción simulada
            return [{"translation_text": "Este es un texto de prueba."}]
    
    # Reemplazamos el pipeline de transformers con el mock
    monkeypatch.setattr("transformers.pipeline", lambda *args, **kwargs: MockPipeline())
    
    # Texto de entrada para la prueba
    input_text = "This is a test text."
    
    # Resultado esperado
    expected_translation = "Este es un texto de prueba."
    
    # Llamada a la función con mock aplicado
    result = translate_text(input_text, source_lang="en", target_lang="es")
    
    # Comprobación de igualdad exacta
    assert result == expected_translation, f"Texto traducido inesperado: {result}"
