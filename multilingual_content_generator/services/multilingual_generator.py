# Archivo: multilingual_content_generator/services/multilingual_generator.py

from transformers import pipeline
from multilingual_content_generator.config import Config


def generate_and_translate(prompt, source_lang="en", target_lang="es", max_length=50):
    """
    Genera contenido en un idioma y lo traduce a otro.
    
    Args:
        prompt (str): Texto de entrada para la generación.
        source_lang (str): Idioma de origen para la traducción.
        target_lang (str): Idioma de destino para la traducción.
        max_length (int): Longitud máxima del texto generado.

    Returns:
        str: Texto traducido.

    Raises:
        ValueError: Si alguna entrada es inválida.
        Exception: Para errores en los pipelines.
    """
    # Validar entradas
    if not prompt:
        raise ValueError("El prompt no puede estar vacío.")
    if not source_lang or not target_lang:
        raise ValueError("Los idiomas no pueden estar vacíos.")

    try:
        # Pipeline para generación de contenido
        generator = pipeline("text-generation", model="gpt2")
        generated = generator(prompt, max_length=max_length, num_return_sequences=1)
        generated_text = generated[0]["generated_text"]

        # Pipeline para traducción
        translator = pipeline("translation", model=f"Helsinki-NLP/opus-mt-{source_lang}-{target_lang}")
        translated = translator(generated_text)
        translated_text = translated[0]["translation_text"]

        return translated_text

    except Exception as e:
        raise Exception(f"Error en la generación o traducción de contenido: {e}")
