# Archivo: tests/test_content_generator.py
# Pruebas para el servicio content_generator.py

import pytest
from multilingual_content_generator.services.content_generator import generate_content

@pytest.mark.timeout(10)
def test_generate_text_content():
    """
    Prueba unitaria para la generación de contenido textual con generate_content.
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


@pytest.mark.timeout(10)
def test_generate_text_and_image_content(monkeypatch):
    """
    Prueba unitaria para la generación de contenido textual y visual con generate_content.
    """

    # Mock del BLIP
    def mock_blip_processor(*args, **kwargs):
        class MockProcessor:
            def __call__(self, prompt, return_tensors):
                return {"input_ids": [0], "attention_mask": [1]}

            def decode(self, output, skip_special_tokens):
                return "Texto generado de prueba con BLIP."

        return MockProcessor()

    def mock_blip_model(*args, **kwargs):
        class MockModel:
            def generate(self, **inputs):
                return [0]

        return MockModel()

    monkeypatch.setattr("transformers.BlipProcessor.from_pretrained", mock_blip_processor)
    monkeypatch.setattr("transformers.BlipForConditionalGeneration.from_pretrained", mock_blip_model)

    # Configuración del test
    prompt = "Describe un paisaje futurista."

    # Llamada a la función con el mock
    result = generate_content(prompt=prompt, generate_image=True)

    # Verificaciones
    assert isinstance(result, dict), "El resultado no es un diccionario."
    assert "text" in result, "El resultado no contiene texto generado."
    assert "image" in result, "El resultado no contiene información sobre imágenes generadas."
    assert result["text"] == "Texto generado de prueba con BLIP.", "El texto generado no es el esperado."
