# Archivo: multilingual_content_generator/services/content_generator.py

from transformers import pipeline
from multilingual_content_generator.config import Config

# Función modificada para facilitar pruebas
def generate_content(prompt, model_name=None, max_length=None, pipeline_function=None):
    """
    Genera contenido textual utilizando un modelo preentrenado.
    
    Args:
        prompt (str): Texto inicial para generar contenido.
        model_name (str, opcional): Nombre del modelo a utilizar.
        max_length (int, opcional): Longitud máxima del contenido generado.
        pipeline_function (callable, opcional): Función personalizada para reemplazar el pipeline (para pruebas).
    
    Returns:
        str: Contenido generado.
    
    Raises:
        ValueError: Si ocurre algún error durante la generación de contenido.
    """
    model_name = model_name or Config.DEFAULT_MODEL
    max_length = max_length or Config.MAX_LENGTH

    try:
        # Usamos el pipeline proporcionado (si está disponible) o creamos uno nuevo
        generator = pipeline_function or pipeline("text-generation", model=model_name)
    except Exception as e:
        raise ValueError(f"Error al inicializar el modelo '{model_name}': {e}")

    try:
        # Generar contenido
        content = generator(prompt, max_length=max_length, num_return_sequences=1)
        return content[0]["generated_text"]
    except Exception as e:
        raise ValueError(f"Error al generar contenido con el modelo '{model_name}': {e}")
