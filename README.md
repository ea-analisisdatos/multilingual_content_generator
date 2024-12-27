# multilingual_content_generator
 Generador de Contenido Multilingüe

## **Objetivos del Proyecto**

-   Crear un generador de contenido que funcione para múltiples plataformas (Blog, LinkedIn, Twitter, etc.).
-   Soportar varios idiomas (Español, Inglés, Francés, Italiano).
-   Integrar imágenes relevantes usando APIs gratuitas.
-   Implementar una interfaz gráfica para facilitar la interacción.

In [ ]:

## **Tecnologías a Utilizar**

-   **Frontend:**  Streamlit (interfaz gráfica).
-   **Backend/Procesamiento:**
    -   Hugging Face Transformers (modelos gratuitos como GPT-Neo o Falcon).
    -   Sentence Transformers (mejora del entendimiento contextual).
    -   Pillow (procesamiento de imágenes).
-   **APIs Gratuitas:**
    -   **Pixabay API:**  Para buscar imágenes relacionadas.
-   **Lenguaje de Programación:**  Python.

## **Estructura del Proyecto**

### **Directorios y Archivos**
```
multilingual_content_generator/
├── multilingual_content_generator/
│   ├── __init__.py
│   ├── app.py
│   ├── config.py
│   ├── services/
│   │   ├── __init__.py
│   │   ├── content_generator.py
│   │   ├── image_retriever.py
│   │   ├── translation_service.py
│   └── utils/
│       ├── __init__.py
│       ├── formatters.py
│       └── validators.py
├── tests/
│   ├── __init__.py
│   ├── test_content_generator.py
│   ├── test_image_retriever.py
│   └── test_integration.py
├── requirements.txt
├── .env.example
├── .gitignore
├── Dockerfile
├── README.md
└── setup.py

```

Escrito por [Erika Alvares](https://www.erikaalvares.es/).
