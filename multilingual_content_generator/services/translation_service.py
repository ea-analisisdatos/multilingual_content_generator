# Archivo: multilingual_content_generator/services/translation_service.py

# Importamos las bibliotecas necesarias
from transformers import pipeline  # Para trabajar con modelos de traducción
from multilingual_content_generator.config import Config

# Verificamos si el paquete sentencepiece está instalado
try:
    import sentencepiece
except ImportError:
    raise ImportError("El paquete 'sentencepiece' es necesario para usar la traducción. Instálalo con 'pip install sentencepiece'.")

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
        # Inicializar el pipeline de traducción
        translator = pipeline("translation", model=f"Helsinki-NLP/opus-mt-{source_lang}-{target_lang}")
        # Traducir el texto
        translation = translator(text, max_length=512)
        # Devolver el texto traducido
        return translation[0]['translation_text']
    except Exception as e:
        raise ValueError(f"Error al traducir el texto: {e}")
