
<!-- Título del Proyecto -->
<h1 align="center">Clasificador de Imágenes con Google Cloud Vision y Gradio</h1>

<!-- Descripción Breve -->
<p align="center">Una aplicación para clasificar imágenes en categorías usando Google Cloud Vision API y Gradio.</p>

<!-- Badges -->
<p align="center">
    <img src="https://img.shields.io/badge/Python-3.7%2B-blue">
    <img src="https://img.shields.io/badge/Gradio-2.0.0-green">
    <img src="https://img.shields.io/badge/Google%20Cloud%20Vision-API-yellow">
</p>

<!-- Tabla de Contenidos -->
## Tabla de Contenidos
- [Descripción](#descripción)
- [Demo](#demo)
- [Requisitos](#requisitos)
- [Instalación](#instalación)
- [Uso](#uso)
- [Estructura del Proyecto](#estructura-del-proyecto)
- [Contribución](#contribución)
- [Créditos](#créditos)
- [Licencia](#licencia)

<!-- Descripción -->
## Descripción
Este proyecto utiliza la API de Google Cloud Vision para clasificar imágenes en varias categorías como Anime, Memes, Screenshots de YouTube, o Educativo. Utiliza Gradio para crear una interfaz amigable donde los usuarios pueden cargar múltiples imágenes y obtener la clasificación junto con las etiquetas detectadas.

<!-- Demo -->
## Demo
Inserta una captura de pantalla o un gif animado que muestre la interfaz en acción.

<!-- Requisitos -->
## Requisitos
- Python 3.7 o superior
- Google Cloud SDK configurado con credenciales válidas para Cloud Vision API
- Instalación de las bibliotecas requeridas: `google-cloud-vision`, `gradio`

<!-- Instalación -->
## Instalación
1. Clona este repositorio.
2. Instala las dependencias necesarias:
   ```bash
   pip install -r requirements.txt
   ```
3. Configura las credenciales de Google Cloud Vision API según se describe en la sección [Configuración](#configuración).

<!-- Uso -->
## Uso
1. Ejecuta la aplicación:
   ```bash
   python app.py
   ```
2. Abre el navegador y navega a la URL proporcionada por Gradio.
3. Sube una o más imágenes para ver la clasificación automática.

<!-- Estructura del Proyecto -->
## Estructura del Proyecto
```
proyecto/
│
├── app.py            # Código principal de la aplicación
├── README.md         # Este archivo
├── requirements.txt  # Lista de dependencias del proyecto
└── ...
```

<!-- Contribución -->
## Contribución
Las contribuciones son bienvenidas. Para cambios importantes, abre primero un problema para discutir lo que te gustaría cambiar.

1. Fork el repositorio
2. Crea tu rama de características (`git checkout -b feature/AmazingFeature`)
3. Commit tus cambios (`git commit -am 'Add some AmazingFeature'`)
4. Push a la rama (`git push origin feature/AmazingFeature`)
5. Abre un Pull Request

<!-- Créditos -->
## Créditos
- Desarrollado por [Jesus Nahataen]
- Basado en la documentación de [Google Cloud Vision](https://cloud.google.com/vision)
- Utiliza [Gradio](https://gradio.app/) para la interfaz de usuario

<!-- Licencia -->
## Licencia
Open-source 

