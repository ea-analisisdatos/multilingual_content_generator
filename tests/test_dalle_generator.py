# Archivo: tests/test_dalle_generator.py
import pytest
from multilingual_content_generator.services.dalle_generator import generate_dalle_image

def test_generate_dalle_image(monkeypatch):
    """
    Prueba unitaria para la función generate_dalle_image.
    Verifica que Stable Diffusion genere una imagen correctamente.
    """

    # Mock para reemplazar el pipeline de Stable Diffusion
    def mock_pipeline(*args, **kwargs):
        class MockPipeline:
            def to(self, device):
                pass  # Simula mover el pipeline a un dispositivo (CPU/GPU)

            def __call__(self, prompt, *args, **kwargs):
                class MockImage:
                    def save(self, path):
                        assert path == "/tmp/generated_image.png"  # Verificar ruta de guardado

                return MockPipelineOutput([MockImage()])

        class MockPipelineOutput:
            def __init__(self, images):
                self.images = images

        return MockPipeline()

    # Aplicar el mock al método StableDiffusionPipeline
    monkeypatch.setattr("diffusers.StableDiffusionPipeline.from_pretrained", mock_pipeline)

    # Ejecutar la función con un prompt de prueba
    prompt = "Un robot programando en un portátil"
    result = generate_dalle_image(prompt)

    # Verificar que la ruta generada es válida
    assert result == "/tmp/generated_image.png", "La ruta de la imagen generada no es la esperada."
