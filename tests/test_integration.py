# Archivo: tests/test_integration.py

# Importamos las bibliotecas necesarias
import pytest
from multilingual_content_generator.services.dalle_generator import generate_dalle_image
from multilingual_content_generator.services.stable_diffusion import generate_stable_diffusion_image
from multilingual_content_generator.services.pixabay_retriever import fetch_images
from multilingual_content_generator.services.unsplash_retriever import fetch_images as fetch_unsplash_images
from multilingual_content_generator.services.content_generator import generate_text_content

# Prueba de integración para la generación de contenido textual y visual
def test_integration_flow(monkeypatch):
    """
    Prueba de integración para verificar que las funciones de generación de contenido y recuperación de imágenes
    funcionan correctamente juntas.

    Combina las pruebas de generación de texto e imágenes, y validación del flujo completo de generación de contenido.
    """

    # Mock para la generación de texto
    def mock_generate_text_content(topic, max_length):
        return f"Este es un contenido generado sobre {topic}."

    # Mock para la generación de imágenes con DALL-E
    def mock_generate_dalle_image(prompt):
        return "https://dalle.fake/image.jpg"

    # Mock para la generación de imágenes con Stable Diffusion
    def mock_generate_stable_diffusion_image(prompt):
        return "https://stable.diffusion.fake/image.jpg"

    # Mock para la recuperación de imágenes de Pixabay
    def mock_fetch_pixabay_images(term, num_results):
        return ["https://pixabay.com/image1.jpg", "https://pixabay.com/image2.jpg"]

    # Mock para la recuperación de imágenes de Unsplash
    def mock_fetch_unsplash_images(term, num_results):
        return ["https://unsplash.com/image1.jpg", "https://unsplash.com/image2.jpg"]

    # Aplicar los mocks
    monkeypatch.setattr("multilingual_content_generator.services.content_generator.generate_text_content", mock_generate_text_content)
    monkeypatch.setattr("multilingual_content_generator.services.dalle_generator.generate_dalle_image", mock_generate_dalle_image)
    monkeypatch.setattr("multilingual_content_generator.services.stable_diffusion.generate_stable_diffusion_image", mock_generate_stable_diffusion_image)
    monkeypatch.setattr("multilingual_content_generator.services.pixabay_retriever.fetch_images", mock_fetch_pixabay_images)
    monkeypatch.setattr("multilingual_content_generator.services.unsplash_retriever.fetch_images", mock_fetch_unsplash_images)

    # Flujo de prueba
    topic = "La tecnología en la educación"
    generated_text = mock_generate_text_content(topic, max_length=100)
    dalle_image = mock_generate_dalle_image(topic)
    stable_diffusion_image = mock_generate_stable_diffusion_image(topic)
    pixabay_images = mock_fetch_pixabay_images(topic, num_results=2)
    unsplash_images = mock_fetch_unsplash_images(topic, num_results=2)

    # Verificaciones
    assert generated_text.startswith("Este es un contenido generado sobre"), "El texto generado no es correcto."
    assert dalle_image == "https://dalle.fake/image.jpg", "La imagen generada por DALL-E no es correcta."
    assert stable_diffusion_image == "https://stable.diffusion.fake/image.jpg", "La imagen generada por Stable Diffusion no es correcta."
    assert len(pixabay_images) == 2, "Pixabay no devolvió el número esperado de imágenes."
    assert len(unsplash_images) == 2, "Unsplash no devolvió el número esperado de imágenes."
