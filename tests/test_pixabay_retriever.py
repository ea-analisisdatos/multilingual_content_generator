# Archivo: tests/test_pixabay_retriever.py

import pytest
import requests  # Asegúrate de importar requests
from multilingual_content_generator.services.pixabay_retriever import fetch_pixabay_images

def test_fetch_pixabay_images_success(monkeypatch):
    """
    Prueba unitaria para la función fetch_pixabay_images.
    Verifica que la función devuelve una lista de URLs en caso de éxito.
    """
    def mock_requests_get(url):
        class MockResponse:
            def json(self):
                return {
                    "hits": [
                        {"webformatURL": "https://pixabay.com/image1.jpg"},
                        {"webformatURL": "https://pixabay.com/image2.jpg"}
                    ]
                }
            def raise_for_status(self):
                pass  # Simula respuesta HTTP exitosa

        return MockResponse()

    monkeypatch.setattr("requests.get", mock_requests_get)

    images = fetch_pixabay_images("flowers", 2)
    assert len(images) == 2
    assert images == ["https://pixabay.com/image1.jpg", "https://pixabay.com/image2.jpg"]

def test_fetch_pixabay_images_error(monkeypatch):
    """
    Prueba unitaria para manejar errores en fetch_pixabay_images.
    Verifica que la función maneje excepciones correctamente.
    """
    def mock_requests_get(url):
        class MockResponse:
            def raise_for_status(self):
                raise requests.exceptions.HTTPError("Error HTTP simulado.")  # Ahora funciona correctamente

        return MockResponse()

    monkeypatch.setattr("requests.get", mock_requests_get)

    with pytest.raises(ValueError, match="Error al conectarse con la API de Pixabay"):
        fetch_pixabay_images("flowers", 2)

def test_fetch_pixabay_images_empty(monkeypatch):
    """
    Prueba unitaria para manejar respuestas vacías de la API de Pixabay.
    """
    def mock_requests_get(url):
        class MockResponse:
            def json(self):
                return {"hits": []}
            def raise_for_status(self):
                pass  # Simula respuesta HTTP exitosa

        return MockResponse()

    monkeypatch.setattr("requests.get", mock_requests_get)

    images = fetch_pixabay_images("flowers", 2)
    assert images == []  # Lista vacía si no hay resultados
