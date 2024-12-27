# Archivo: multilingual_content_generator/services/multilingual_generation.py

from transformers import pipeline


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
    """
    # Pipeline para generación de contenido
    generator = pipeline("text-generation", model="gpt2")
    generated = generator(prompt, max_length=max_length, num_return_sequences=1)
    generated_text = generated[0]["generated_text"]

    # Pipeline para traducción
    translator = pipeline("translation", model=f"Helsinki-NLP/opus-mt-{source_lang}-{target_lang}")
    translated = translator(generated_text)
    translated_text = translated[0]["translation_text"]

    return translated_text
