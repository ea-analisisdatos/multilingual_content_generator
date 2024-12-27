# Archivo: tests/test_multilingual_generation.py

import pytest
from multilingual_content_generator.services.multilingual_generator import generate_and_translate

@pytest.mark.timeout(10)
def test_multilingual_content(monkeypatch):
    """
    Prueba de integración para verificar la generación y traducción de contenido.
    """

    # Mock de generación de contenido
    class MockContentGenerator:
        def __call__(self, prompt, max_length, num_return_sequences):
            return [{"generated_text": "This is a generated text."}]

    # Mock de traducción
    class MockTranslator:
        def __call__(self, text, **kwargs):
            return [{"translation_text": "Este es un texto generado."}]

    def mock_pipeline(task, *args, **kwargs):
        print(f"Mock pipeline invoked with task: {task}")  # Depuración
        if task == "text-generation":
            return MockContentGenerator()
        elif task == "translation":
            return MockTranslator()

    # Reemplazar los pipelines con mocks
    monkeypatch.setattr("multilingual_content_generator.services.multilingual_generator.pipeline", mock_pipeline)

    # Prueba: Generación y traducción
    result = generate_and_translate("Test prompt", source_lang="en", target_lang="es", max_length=50)

    # Verificación
    assert result == "Este es un texto generado.", "El resultado traducido no es el esperado."
