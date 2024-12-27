# Archivo: tests/test_unsplash_retriever.py

# Importamos las bibliotecas necesarias
import pytest
from multilingual_content_generator.services.unsplash_retriever import fetch_unsplash_images

# Prueba para verificar la recuperación de imágenes desde Unsplash
def test_fetch_unsplash_images(monkeypatch):
    """
    Prueba unitaria para la función fetch_unsplash_images.
    Verifica que la función devuelva una lista de URLs cuando se proporciona un término de búsqueda.
    """
    # Mock de respuesta simulada de la API de Unsplash
    def mock_requests_get(url, params):
        class MockResponse:
            def json(self):
                return {
                    "results": [
                        {"urls": {"regular": "https://unsplash.com/image1.jpg"}},
                        {"urls": {"regular": "https://unsplash.com/image2.jpg"}}
                    ]
                }

        return MockResponse()

    # Aplicamos el mock al método requests.get
    monkeypatch.setattr("requests.get", mock_requests_get)

    # Ejecutamos la función con un término de búsqueda de prueba
    term = "tecnología"
    result = fetch_unsplash_images(term, num_results=2)

    # Verificamos que el resultado sea una lista con URLs de imágenes
    assert result == [
        "https://unsplash.com/image1.jpg",
        "https://unsplash.com/image2.jpg"
    ], "La función no devolvió las URLs esperadas."
