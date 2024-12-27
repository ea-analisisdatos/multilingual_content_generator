# Archivo: tests/test_pixabay_retriever.py

# Importamos las bibliotecas necesarias
import pytest
from multilingual_content_generator.services.pixabay_retriever import fetch_pixabay_images

# Prueba para verificar la recuperación de imágenes desde Pixabay
def test_fetch_pixabay_images(monkeypatch):
    """
    Prueba unitaria para la función fetch_pixabay_images.
    Verifica que la función devuelva una lista de URLs cuando se proporciona un término de búsqueda.
    """
    # Mock de respuesta simulada de la API de Pixabay
    def mock_requests_get(url, params=None):
        class MockResponse:
            def json(self):
                return {
                    "hits": [
                        {"webformatURL": "https://pixabay.com/image1.jpg"},
                        {"webformatURL": "https://pixabay.com/image2.jpg"}
                    ]
                }

            def raise_for_status(self):
                pass  # Simula una respuesta HTTP exitosa

        return MockResponse()

    # Aplicamos el mock al método requests.get
    monkeypatch.setattr("requests.get", mock_requests_get)

    # Ejecutamos la función con un término de búsqueda de prueba
    term = "paisaje"
    result = fetch_pixabay_images(term, num_results=2)

    # Verificamos que el resultado sea una lista con URLs de imágenes
    assert result == [
        "https://pixabay.com/image1.jpg",
        "https://pixabay.com/image2.jpg"
    ], "La función no devolvió las URLs esperadas."
