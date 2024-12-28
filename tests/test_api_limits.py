# Archivo: tests/test_api_limits.py
# Pruebas unitarias para el archivo api_limits.py

from multilingual_content_generator.utils.api_limits import get_limit
import pytest


def test_get_limit_valid_api():
    """
    Prueba para una API válida.
    """
    limit = get_limit("unsplash")
    assert limit == {"requests_per_hour": 50}, "El límite para 'unsplash' no es el esperado."

def test_get_limit_invalid_api():
    """
    Prueba para una API inválida.
    """
    with pytest.raises(ValueError, match="No se encontraron límites para la API 'invalid_api'"):
        get_limit("invalid_api")
