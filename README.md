# Startup Analyzer Landing Page 🚀

Landing page desarrollada como solución al reto de selección propuesto.

## 📌 Descripción
Startup Analyzer es una landing page interactiva desarrollada con Streamlit que permite a los usuarios ingresar la URL de una startup tecnológica y recibir automáticamente un análisis ejecutivo tipo one-pager.
Este análisis está orientado a inversionistas, CEO, CTOs y otros tomadores de decisiones estratégicas.

Se puede visualizar en pantalla o descargar en formato PDF para compartir.

## 🎯 Funcionalidad
- Ingreso de URL de startups tecnológicas.
- Extracción de contenido público.
- Análisis automático tipo One-Pager.
- Visualización en pantalla.
- Exportación a PDF para descargar.

## 🚧 Tecnologías
- Streamlit
- Python
- LXML (extracción)
- ReportLab (PDF)

## 📦 Estructura del proyecto
````
startup-analyzer-landing
├── app.py
├── .streamlit/
│   └── config.toml
├── modules/
│   ├── extractor.py
│   ├── analyzer.py
│   └── pdf_generator.py
└── requirements.txt
````

## 🌐 Despliegue actual
Enlace a Streamlit Cloud:
[https://startup-analyzer-landing.streamlit.app/](https://startup-analyzer-landing.streamlit.app/)

## 📊 Ejemplo de análisis
Enlace al PDF generado:
[https://drive.google.com/file/d/1jFf0MZ4WJPQ6sO90geeMfMatI5xIwLZR/view?usp=sharing](https://drive.google.com/file/d/1jFf0MZ4WJPQ6sO90geeMfMatI5xIwLZR/view?usp=sharing)

## 🚀 Instrucciones para la instalación local
### Clona el repositorio:
````
git clone https://github.com/tu_usuario/startup-analyzer-landing.git
cd startup-analyzer-landing
````

### Instala las dependencias:
````
pip install -r requirements.txt
````

### Ejecuta la aplicación:
````
streamlit run app.py
````

### Accede a la aplicación en tu navegador, normalmente en:
````
http://localhost:8501
````

### Despliegue en la nube
Se recomienda utilizar servicios gratuitos como:

- Streamlit Community Cloud
- Vercel
- Netlify

Solo sube tu proyecto o conecta tu repositorio para que esté disponible públicamente.

## 📝 Notas
- En algunos sitios, el contenido es limitado debido a políticas de diseño web.
- Se filtró el contenido para eliminar estilos y scripts, priorizando texto informativo.
