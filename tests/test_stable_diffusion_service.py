# Archivo: tests/test_stable_diffusion_service.py
# Pruebas para el servicio stable_diffusion_service.py

# Importamos las bibliotecas necesarias
import pytest
from multilingual_content_generator.services.stable_diffusion_service import (
    configure_pipeline,
    generate_image,
    save_image,
    generate_stable_diffusion_image,
)
from PIL import Image
from pathlib import Path

def test_configure_pipeline(monkeypatch):
    """
    Prueba unitaria para configurar el pipeline.
    """
    def mock_from_pretrained(*args, **kwargs):
        class MockPipeline:
            def to(self, device):
                return self
        return MockPipeline()

    # Mock del método from_pretrained del pipeline
    monkeypatch.setattr("diffusers.StableDiffusionPipeline.from_pretrained", mock_from_pretrained)

    token = "mock_token"
    pipe = configure_pipeline(token)
    assert pipe is not None, "El pipeline no se configuró correctamente."

def test_generate_image(monkeypatch):
    """
    Prueba unitaria para la generación de imágenes.
    """
    class MockPipeline:
        def __call__(self, prompt):
            class MockResult:
                images = [Image.new("RGB", (512, 512), "blue")]
            return MockResult()

    # Crear una instancia del mock del pipeline
    pipe = MockPipeline()
    prompt = "Un bosque mágico"
    image = generate_image(pipe, prompt)
    assert isinstance(image, Image.Image), "La imagen generada no es del tipo esperado."

def test_save_image(tmp_path):
    """
    Prueba unitaria para guardar imágenes en el sistema de archivos.
    """
    image = Image.new("RGB", (512, 512), "blue")
    output_path = tmp_path / "output_image.png"
    save_image(image, output_path)
    assert output_path.exists(), "La imagen no se guardó correctamente."

def test_generate_stable_diffusion_image(monkeypatch, tmp_path):
    """
    Prueba de integración para generar y guardar una imagen.
    """
    def mock_configure_pipeline(token):
        class MockPipeline:
            def to(self, device):
                return self

            def __call__(self, prompt):
                class MockResult:
                    images = [Image.new("RGB", (512, 512), "blue")]
                return MockResult()
        return MockPipeline()

    # Mock de configure_pipeline
    monkeypatch.setattr(
        "multilingual_content_generator.services.stable_diffusion_service.configure_pipeline",
        mock_configure_pipeline
    )

    prompt = "Un bosque mágico"
    output_path = tmp_path / "output_image.png"

    # Prueba de generación en memoria
    image = generate_stable_diffusion_image(prompt, save_to_file=False)
    assert isinstance(image, Image.Image), "La imagen generada en memoria no es del tipo esperado."

    # Prueba de guardado en archivo
    path = generate_stable_diffusion_image(prompt, save_to_file=True, output_path=str(output_path))
    assert str(path) == str(output_path), "La ruta devuelta no es correcta."
    assert output_path.exists(), "El archivo de imagen no se guardó correctamente."
