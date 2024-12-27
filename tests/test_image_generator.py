# Test temporal para verificar el módulo image_generator
try:
    from multilingual_content_generator.services.image_generator import generate_dalle_image
    print("El módulo image_generator se ha importado correctamente.")
except ImportError as e:
    print(f"Error al importar el módulo: {e}")
