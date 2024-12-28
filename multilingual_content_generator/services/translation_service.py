# Archivo: multilingual_content_generator/services/translation_service.py
# Servicio para traducir texto utilizando modelos de Hugging Face.

# Importamos las bibliotecas necesarias
from transformers import pipeline  # Para trabajar con modelos de traducción
from multilingual_content_generator.config import Config

# Verificamos si el paquete sentencepiece está instalado
try:
    import sentencepiece
except ImportError:
    raise ImportError("El paquete 'sentencepiece' es necesario para usar la traducción. Instálalo con 'pip install sentencepiece'.")

# Idiomas soportados (puedes expandir esta lista según sea necesario)
SUPPORTED_LANGUAGES = {
    "en": "English",
    "es": "Spanish",
    "fr": "French",
    "de": "German",
    "it": "Italian",
    "pt": "Portuguese"
}

def translate_text(text, source_lang, target_lang):
    """
    Traduce texto entre dos idiomas usando el pipeline de Hugging Face.

    Args:
        text (str): El texto que se desea traducir.
        source_lang (str): Idioma de origen (por ejemplo, 'en' para inglés).
        target_lang (str): Idioma de destino (por ejemplo, 'es' para español).

    Returns:
        str: El texto traducido.

    Raises:
        ValueError: Si ocurre un error durante la traducción.
    """
    try:
        # Validar que los idiomas sean compatibles
        if source_lang not in SUPPORTED_LANGUAGES:
            raise ValueError(f"El idioma de origen '{source_lang}' no está soportado.")
        if target_lang not in SUPPORTED_LANGUAGES:
            raise ValueError(f"El idioma de destino '{target_lang}' no está soportado.")

        # Inicializar el pipeline de traducción
        translator = pipeline("translation", model=f"Helsinki-NLP/opus-mt-{source_lang}-{target_lang}")
        
        # Traducir el texto
        translation = translator(text, max_length=512)
        
        # Devolver el texto traducido
        return translation[0]['translation_text']
    except ValueError as e:
        raise e
    except KeyError:
        raise ValueError("El modelo de traducción devolvió un formato inesperado.")
    except Exception as e:
        raise ValueError(f"Error al traducir el texto: {e}")
