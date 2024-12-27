from transformers import pipeline
from multilingual_content_generator.config import Config

def generate_content(prompt, model_name=Config.DEFAULT_MODEL, max_length=Config.MAX_LENGTH):
    """
    Genera contenido textual utilizando un modelo preentrenado.

    Args:
        prompt (str): Texto inicial que guía la generación del modelo.
        model_name (str): Nombre del modelo de lenguaje a utilizar.
        max_length (int): Longitud máxima del contenido generado.

    Returns:
        str: El texto generado por el modelo.
    """
    # Inicializar el pipeline de generación de texto con el modelo especificado
    generator = pipeline("text-generation", model=model_name)
    # Generar contenido basado en el prompt proporcionado
    content = generator(prompt, max_length=max_length, num_return_sequences=1)
    # Retornar el texto generado por el modelo
    return content[0]["generated_text"]
