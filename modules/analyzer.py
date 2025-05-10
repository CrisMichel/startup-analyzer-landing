# modules/analyzer.py
import os
from huggingface_hub import InferenceClient
from huggingface_hub import login

token = os.getenv("HUGGINGFACE_TOKEN")
client = InferenceClient(
    model="HuggingFaceH4/zephyr-7b-beta",
    token=token,
    provider="hf-inference"  # proveedor seguro y soportado
)

CAMPOS_ONE_PAGER = [
    "Resumen Ejecutivo",
    "Indicadores Clave",
    "Expansión Tecnológica",
    "Diferenciadores Clave",
    "Contexto del Ecosistema",
    "Oportunidades Estratégicas",
    "Viabilidad de Compra o Integración",
    "Recomendación Ejecutiva"
]

def analyze_text(text):
    """
    Genera un análisis tipo One-Pager usando Hugging Face Inference API.
    
    Args:
        text (str): Texto extraído de la página web.

    Returns:
        dict: Contiene cada sección del One-Pager con su contenido.
    """

    if not text or text.strip() == "":
        return {
            "Resumen Ejecutivo": "Dato no disponible",
            "Indicadores Clave": "Dato no disponible",
            "Expansión Tecnológica": "Dato no disponible",
            "Diferenciadores Clave": "Dato no disponible",
            "Contexto del Ecosistema": "Dato no disponible",
            "Oportunidades Estratégicas": "Dato no disponible",
            "Viabilidad de Compra o Integración": "Dato no disponible",
            "Recomendación Ejecutiva": "Dato no disponible",
        }

    prompt = f"""
Eres un analista ejecutivo experto en startups.

A partir del siguiente texto de un sitio web:

{text}

Genera un reporte ejecutivo tipo One-Pager en este formato:

Resumen Ejecutivo:
[Texto claro y profesional]

Indicadores Clave:
[Lista o texto]

Expansión Tecnológica:
[Texto]

Diferenciadores Clave:
[Texto]

Contexto del Ecosistema:
[Texto]

Oportunidades Estratégicas:
[Texto]

Viabilidad de Compra o Integración:
[Texto]

Recomendación Ejecutiva:
[Texto]

Si no hay información para una sección, escribe "Dato no disponible". Queda estrictamente prohibido usar textos genéricos como "nombre de la empresa", "empresa XYZ" o "inserte aquí", si no cuentas con el nombre solo usa 'la empresa'.
Comienza ahora:
"""

    try:
        response = client.text_generation(prompt, max_new_tokens=800, temperature=0.2)
    except Exception as e:
        print(f"❌ Error en inferencia Hugging Face: {e}")
        return {clave: f"Error durante el análisis: {str(e)}" for clave in CAMPOS_ONE_PAGER}


    # Procesar salida
    secciones = {}
    seccion_actual = None

    for linea in response.split("\n"):
        if linea.strip().endswith(":"):
            seccion_actual = linea.strip().replace(":", "")
            secciones[seccion_actual] = ""
        elif seccion_actual:
            secciones[seccion_actual] += linea.strip() + "\n"

    return {clave: secciones.get(clave, "Dato no disponible").strip() for clave in CAMPOS_ONE_PAGER}
