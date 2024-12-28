# Archivo: multilingual_content_generator/services/content_generator.py
# Servicio para generar contenido textual y visual utilizando BLIP.

from transformers import BlipProcessor, BlipForConditionalGeneration
from multilingual_content_generator.config import Config

def generate_content(prompt, model_name=None, max_length=None, pipeline_function=None, generate_image=False):
    """
    Genera contenido textual o texto con imágenes utilizando BLIP.

    Args:
        prompt (str): Texto inicial para generar contenido.
        model_name (str, opcional): Nombre del modelo para generación de texto (si se usa texto únicamente).
        max_length (int, opcional): Longitud máxima del contenido generado.
        pipeline_function (callable, opcional): Función personalizada para pruebas de generación de texto.
        generate_image (bool, opcional): Indica si se debe generar contenido visual utilizando BLIP.

    Returns:
        str o dict: Contenido generado. Puede incluir texto e imágenes dependiendo de los argumentos.

    Raises:
        ValueError: Si ocurre algún error durante la generación de contenido.
    """
    # Caso 1: Generación de imágenes y texto utilizando BLIP
    if generate_image:
        try:
            # Inicializar el procesador y el modelo de BLIP
            processor = BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-base")
            model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-base")

            # Preparar entradas para el modelo
            inputs = processor(prompt, return_tensors="pt")
            outputs = model.generate(**inputs)

            # Decodificar y devolver el texto generado
            return {
                "text": processor.decode(outputs[0], skip_special_tokens=True),
                "image": "Generación de imagen asociada al texto (BLIP no genera imágenes directamente)"
            }
        except Exception as e:
            raise ValueError(f"Error al generar contenido con BLIP: {e}")

    # Caso 2: Generación de contenido textual (pipeline estándar de Hugging Face)
    else:
        model_name = model_name or Config.DEFAULT_MODEL
        max_length = max_length or Config.MAX_LENGTH

        try:
            # Usamos el pipeline proporcionado (si está disponible) o creamos uno nuevo
            generator = pipeline_function or pipeline("text-generation", model=model_name)
        except Exception as e:
            raise ValueError(f"Error al inicializar el modelo '{model_name}': {e}")

        try:
            # Generar contenido textual
            content = generator(prompt, max_length=max_length, num_return_sequences=1)
            return content[0]["generated_text"]
        except Exception as e:
            raise ValueError(f"Error al generar contenido con el modelo '{model_name}': {e}")
