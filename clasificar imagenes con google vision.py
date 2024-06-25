import os
import io
import shutil
from google.cloud import vision
import gradio as gr

# Autenticación con Google Cloud Vision API
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] ="ruta del json descargado en la pagina donde se crea la api de google vision xd"
client = vision.ImageAnnotatorClient()

# Función para crear carpetas si no existen
def create_folders():
    categories = ["Anime", "Memes", "Screenshots de YouTube", "Educativo", "No se pudo clasificar"]
    for category in categories:
        if not os.path.exists(category):
            os.makedirs(category)

def classify_image(image_path):
    # Leer la imagen desde la ruta del archivo
    with io.open(image_path, 'rb') as image_file:
        content = image_file.read()
    image = vision.Image(content=content)

    # Realizar la detección de etiquetas en la imagen
    response = client.label_detection(image=image)
    labels = response.label_annotations

    # Inicializar variables de clasificación
    categories = {
        "Anime": False,
        "Memes": False,
        "Screenshots de YouTube": False,
        "Educativo": False
    }

    # Analizar las etiquetas
    detected_labels = []
    for label in labels:
        detected_labels.append(f"{label.description} (Confianza: {label.score:.2f})")
        description_lower = label.description.lower()
        
        # Criterios específicos para cada categoría
        if 'anime' in description_lower or 'fanart' in description_lower or 'artwork' in description_lower or 'drawing' in description_lower or 'cartoon' in description_lower or 'hairstyle' in description_lower or 'hair' in description_lower:
            categories["Anime"] = True
        if 'meme' in description_lower or 'funny' in description_lower or 'caption' in description_lower or 'text' in description_lower:
            categories["Memes"] = True
        if 'screenshot' in description_lower or 'youtube' in description_lower or 'app' in description_lower or 'video' in description_lower and 'Multimedia' in description_lower:
            categories["Screenshots de YouTube"] = True
        if 'infographic' in description_lower or 'diagram' in description_lower or 'educational' in description_lower or 'chart' in description_lower:
            categories["Educativo"] = True

    # Clasificar la imagen basada en las categorías detectadas
    if categories["Anime"]:
        classification = "Anime"
    elif categories["Memes"] and not categories["Anime"]:
        classification = "Memes"
    elif categories["Screenshots de YouTube"]:
        classification = "Screenshots de YouTube"
    elif categories["Educativo"]:
        classification = "Educativo"
    else:
        classification = "No se pudo clasificar"

    return classification, detected_labels

# Crear interfaz de Gradio
def gradio_interface(images):
    create_folders()
    classifications = []
    labels_detected = []
    for image in images:
        classification, detected_labels = classify_image(image.name)
        detected_labels_str = "\n".join(detected_labels)
        
        # Mover imagen a la carpeta correspondiente
        destination_folder = os.path.join(classification, os.path.basename(image.name))
        shutil.move(image.name, destination_folder)
        
        classifications.append(f"Imagen: {os.path.basename(image.name)}\nClasificación: {classification}")
        labels_detected.append(f"Imagen: {os.path.basename(image.name)}\nEtiquetas Detectadas:\n{detected_labels_str}")

    # Formatear resultados para Gradio
    classifications_str = "\n\n".join(classifications)
    labels_detected_str = "\n\n".join(labels_detected)

    return classifications_str, labels_detected_str

# Definir interfaz usando gradio.Blocks
with gr.Blocks() as interface:
    gr.Markdown("## Clasificador de Imágenes")
    gr.Markdown("Sube imágenes y serán clasificadas en una de las siguientes categorías: Anime, Memes, Screenshots de YouTube o Educativo.")
    with gr.Row():
        with gr.Column():
            image_input = gr.File(file_count="multiple", label="Sube imágenes")
            classify_button = gr.Button("Clasificar")
        with gr.Column():
            classification_output = gr.Textbox(label="Clasificación", lines=15)
            labels_output = gr.Textbox(label="Etiquetas Detectadas", lines=15)
    classify_button.click(gradio_interface, inputs=image_input, outputs=[classification_output, labels_output])

# Ejecutar la interfaz
if __name__ == "__main__":
    interface.launch()
