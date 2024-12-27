# Multilingual Content Generator
Generador de Contenido Multilingüe


## **Objetivos del Proyecto**

- Crear un generador de contenido que funcione para múltiples plataformas (Blog, LinkedIn, Twitter, etc.).
- Soportar varios idiomas (Español, Inglés, Francés, Italiano).
- Integrar imágenes relevantes usando APIs gratuitas.
- Implementar una interfaz gráfica para facilitar la interacción.

---

## **Tecnologías Utilizadas**

### **Frontend**
- **Streamlit:** Herramienta para crear la interfaz gráfica de la aplicación.

### **Backend/Procesamiento**
- **Hugging Face Transformers:** Uso de modelos gratuitos como GPT-Neo o Falcon.
- **Sentence Transformers:** Mejora del entendimiento contextual.
- **Pillow:** Procesamiento y manipulación de imágenes.

### **APIs**
- **Pixabay API:** Para buscar imágenes relacionadas de manera gratuita.

### **Lenguaje de Programación**
- **Python.**

---

## **Estructura del Proyecto**

El proyecto está organizado según las mejores prácticas en ingeniería de software, lo que facilita la escalabilidad y el mantenimiento. La estructura es la siguiente:

```
multilingual_content_generator/
├── app.py                               # Archivo principal que ejecuta la aplicación con Streamlit
├── multilingual_content_generator/      # Código principal y módulos internos del proyecto
│   ├── __init__.py                      # Inicializador del paquete principal
│   ├── config.py                        # Configuración del proyecto (claves API, variables globales, etc.)
│   ├── services/                        # Servicios principales del proyecto
│   │   ├── __init__.py                  # Inicializador del módulo de servicios
│   │   ├── content_generator.py         # Lógica para generar contenido textual multilingüe
│   │   ├── image_retriever.py           # Funciones para recuperar imágenes desde APIs externas (Pixabay, Unsplash)
│   │   ├── image_generator.py           # Funciones para generar imágenes con IA (Stable Diffusion, DALL-E)
│   │   └── translation_service.py       # Servicio opcional para traducción automática de texto
│   ├── utils/                           # Funciones auxiliares reutilizables
│   │   ├── __init__.py                  # Inicializador del módulo de utilidades
│   │   ├── formatters.py                # Funciones para formatear texto y datos
│   │   └── validators.py                # Validaciones para entradas y salidas
├── tests/                               # Pruebas unitarias e integración
│   ├── __init__.py                      # Inicializador del módulo de pruebas
│   ├── test_content_generator.py        # Pruebas para el módulo content_generator.py
│   ├── test_image_retriever.py          # Pruebas para el módulo image_retriever.py
│   └── test_integration.py              # Pruebas de integración del proyecto
├── .env                                 # Archivo de configuración sensible (claves API, etc.)
├── .env.example                         # Ejemplo de configuración del archivo .env
├── .gitignore                           # Lista de archivos y carpetas ignorados por Git
├── Dockerfile                           # Configuración para contenedores Docker (opcional)
├── LICENSE                              # Licencia del proyecto
├── multilingual_content_generator.ipynb # Cuaderno Jupyter para pruebas o documentación (opcional)
├── README.md                            # Documentación principal del proyecto
├── requirements.txt                     # Lista de dependencias necesarias para ejecutar el proyecto
├── setup.py                             # Archivo opcional para instalar el proyecto como paquete

```

### Diferencias Clave
```
| Aspecto              | `image_retriever.py`                      | `image_generator.py`                    |
|-----------------------|-------------------------------------------|-----------------------------------------|
| **Funcionalidad**     | Recupera imágenes existentes.             | Genera imágenes nuevas desde cero.      |
| **Fuente de Imágenes**| APIs de terceros (Pixabay, Unsplash).     | Modelos de IA (Stable Diffusion, DALL-E). |
| **Entrada**           | Palabras clave para búsqueda.             | Texto descriptivo para generación.      |
| **Salida**            | URLs de imágenes existentes.              | Una imagen generada como objeto.        |
| **Dependencias**      | `requests` y configuración de API Keys.   | Bibliotecas de IA como `diffusers`.     |

```

## **Cómo Ejecutar el Proyecto**

### **1. Clonar el Repositorio**
```bash
git clone https://github.com/tu_usuario/multilingual_content_generator.git
cd multilingual_content_generator

```

### **2. Crear un Entorno Virtual (Opcional pero Recomendado)**

```bash
python -m venv venv
source venv/bin/activate  # En Linux/Mac
venv\Scripts\activate     # En Windows

```

### **3. Instalar las Dependencias**

```bash
pip install -r requirements.txt

```

### **4. Configurar las Variables de Entorno**

Crea un archivo `.env` en la raíz del proyecto con el siguiente contenido:

```plaintext
PIXABAY_API_KEY=tu_clave_pixabay

```

### **5. Ejecutar la Aplicación**

```bash
streamlit run app.py

```

### **6. Acceder a la Aplicación**

Abre el navegador en el enlace generado por Streamlit, normalmente:

```
http://localhost:8501

```

----------

## **Pruebas**

Las pruebas unitarias e integración se encuentran en la carpeta `tests/`. Para ejecutarlas, usa:

```bash
pytest tests/

```

----------

## **Contribuciones**

¡Las contribuciones son bienvenidas! Si deseas colaborar, abre un pull request o contacta al autor.

----------

## **Licencia**

Este proyecto está licenciado bajo la Licencia MIT. Consulta el archivo [LICENSE](https://chatgpt.com/c/LICENSE) para más información.

----------

Escrito por [Erika Alvares](https://www.erikaalvares.es/).


