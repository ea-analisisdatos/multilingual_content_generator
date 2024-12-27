# Archivo: tests/test_stable_diffusion.py

# Importamos las bibliotecas necesarias
import pytest
from multilingual_content_generator.services.stable_diffusion import generate_stable_diffusion_image
from PIL import Image

# Prueba para la generación de imágenes con Stable Diffusion
def test_generate_stable_diffusion_image(monkeypatch):
    """
    Prueba unitaria para la función generate_stable_diffusion_image.
    Verifica que la función devuelva una imagen generada como objeto PIL.Image.
    """

    # Mock de respuesta simulada del pipeline de Stable Diffusion
    def mock_pipeline(*args, **kwargs):
        def mock_call(prompt):
            return {"images": [Image.new("RGB", (512, 512), "blue")]}
        return mock_call

    # Aplicamos el mock al pipeline de diffusers
    monkeypatch.setattr("diffusers.StableDiffusionPipeline.from_pretrained", mock_pipeline)

    # Ejecutamos la función con un prompt de prueba
    prompt = "Un bosque mágico iluminado por la luna"
    result = generate_stable_diffusion_image(prompt)

    # Verificamos que el resultado sea una instancia de PIL.Image
    assert isinstance(result, Image.Image), "La función no devolvió un objeto PIL.Image."
