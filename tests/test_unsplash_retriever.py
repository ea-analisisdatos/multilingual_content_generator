# Archivo: tests/test_unsplash_retriever.py
# Pruebas unitarias para el servicio Unsplash Retriever.

# Importamos las bibliotecas necesarias
import pytest
from multilingual_content_generator.services.unsplash_retriever import fetch_unsplash_images
from multilingual_content_generator.utils.api_limits import get_limit

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
        "https://unsplash.com/image1.jpg",
        "https://unsplash.com/image2.jpg"
    ]
    assert result == expected, f"Se esperaba {expected}, pero se obtuvo {result}"


def test_fetch_unsplash_images_limit_exceeded(monkeypatch):
    """
    Prueba unitaria para la función fetch_unsplash_images.
    Verifica que la función lance una excepción cuando se excede el límite de solicitudes.
    """
    # Mock para simular un límite bajo
    def mock_get_limit(api_name):
        print("Mock get_limit ejecutado")
        return {"requests_per_hour": 3}

    # Mock para requests.get (simula una respuesta adecuada)
    def mock_requests_get(url, headers, params):
        class MockResponse:
            def raise_for_status(self):
                raise ValueError("El límite de solicitudes por hora es 3.")  # Simula la excepción correcta

            def json(self):
                return {}

        return MockResponse()

    # Reemplazar los métodos con mocks
    monkeypatch.setattr(
        "multilingual_content_generator.utils.api_limits.get_limit",
        mock_get_limit
    )
    monkeypatch.setattr("requests.get", mock_requests_get)

    # Verifica que se lanza la excepción
    with pytest.raises(ValueError, match=r"El límite de solicitudes por hora es 3\."):
        fetch_unsplash_images("nature", num_results=5)
