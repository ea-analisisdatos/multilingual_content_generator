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
# Generador de Contenido Multilingüe con Imágenes

Este proyecto es una aplicación de Streamlit diseñada para generar contenido textual multilingüe y recuperar imágenes relacionadas utilizando la API de Pixabay. La aplicación permite a los usuarios seleccionar un tema, un idioma y un tono para generar contenido relevante junto con imágenes.

---

## **Estructura del Proyecto**

La estructura del proyecto sigue las mejores prácticas en ingeniería de software, con una clara separación de responsabilidades:

```plaintext
multilingual_content_generator/          # Carpeta raíz del proyecto
├── app.py                               # Archivo principal para la aplicación Streamlit
├── multilingual_content_generator/      # Código interno y módulos principales del proyecto
│   ├── __init__.py                      # Inicializador del paquete principal
│   ├── services/                        # Servicios principales del proyecto
│   │   ├── __init__.py                  # Inicializador del módulo de servicios
│   │   ├── content_generator.py         # Lógica para generación de contenido
│   │   ├── image_retriever.py           # Lógica para recuperar imágenes desde la API de Pixabay
│   │   └── translation_service.py       # Servicio opcional para traducción automática
│   ├── utils/                           # Funciones auxiliares reutilizables
│   │   ├── __init__.py                  # Inicializador del módulo de utilidades
│   │   ├── formatters.py                # Funciones para formatear datos
│   │   └── validators.py                # Validaciones de entrada y salida
├── tests/                               # Pruebas unitarias e integración
│   ├── __init__.py                      # Inicializador del módulo de pruebas
│   ├── test_content_generator.py        # Pruebas para el módulo content_generator.py
│   ├── test_image_retriever.py          # Pruebas para el módulo image_retriever.py
│   └── test_integration.py              # Pruebas de integración del proyecto
├── multilingual_content_generator.ipynb # Cuaderno Jupyter para documentación o pruebas
├── requirements.txt                     # Lista de dependencias necesarias para el proyecto
├── .env                                 # Configuración sensible como claves API
├── .env.example                         # Ejemplo de archivo .env
├── .gitignore                           # Archivos y carpetas ignoradas por Git
├── LICENSE                              # Licencia del proyecto
├── README.md                            # Documentación principal del proyecto
├── setup.py                             # Archivo opcional para instalar el proyecto como paquete

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


