# Archivo: tests/test_unsplash_retriever.py
# Pruebas unitarias para el servicio Unsplash Retriever.

# Importamos las bibliotecas necesarias
import pytest
from multilingual_content_generator.services.unsplash_retriever import fetch_unsplash_images

def test_fetch_unsplash_images(monkeypatch):
    """
    Prueba unitaria para la función fetch_unsplash_images.
    Verifica que la función devuelva una lista de URLs de imágenes al proporcionar un término de búsqueda.
    """
    # Mock para simular la respuesta de la API de Unsplash
    def mock_requests_get(url, headers, params):
        class MockResponse:
            def raise_for_status(self):
                pass  # Simula una respuesta exitosa sin errores

            def json(self):
                return {
                    "results": [
                        {"urls": {"regular": "https://unsplash.com/image1.jpg"}},
                        {"urls": {"regular": "https://unsplash.com/image2.jpg"}}
                    ]
                }

        return MockResponse()

    # Reemplazamos el método requests.get con el mock
    monkeypatch.setattr("requests.get", mock_requests_get)

    # Ejecutamos la función con un término de búsqueda de prueba
    query = "nature"
    result = fetch_unsplash_images(query, num_results=2)

    # Verificamos que el resultado sea una lista con URLs de imágenes
    expected = [
        {"urls": {"regular": "https://unsplash.com/image1.jpg"}},
        {"urls": {"regular": "https://unsplash.com/image2.jpg"}}
    ]
    assert result == expected, f"Se esperaba {expected}, pero se obtuvo {result}"


def test_fetch_unsplash_images_limit_exceeded(monkeypatch):
    """
    Prueba unitaria para la función fetch_unsplash_images.
    Verifica que la función lance una excepción cuando se excede el límite de solicitudes.
    """
    # Mock para simular el límite de la API
    def mock_get_limit(api_name):
        return {"requests_per_hour": 3}

    # Reemplazamos el método get_limit con el mock
    monkeypatch.setattr("api_limits.get_limit", mock_get_limit)

    # Ejecutamos la función con un número de solicitudes que excede el límite
    query = "nature"
    num_results = 5
    with pytest.raises(ValueError, match="El límite de solicitudes por hora es 3."):
        fetch_unsplash_images(query, num_results=num_results)
