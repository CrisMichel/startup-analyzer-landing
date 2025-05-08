# modules/analyzer.py

from huggingface_hub import InferenceClient

# Cliente de HuggingFace → solo necesitas tu token (puedes usar login o ponerlo aquí)
client = InferenceClient(model="HuggingFaceH4/zephyr-7b-beta")

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

Si no hay información para una sección, escribe "Dato no disponible".
Comienza ahora:
"""

    response = client.text_generation(prompt, max_new_tokens=1024, temperature=0.2)

    # Procesar salida
    secciones = {}
    seccion_actual = None

    for linea in response.split("\n"):
        if linea.strip().endswith(":"):
            seccion_actual = linea.strip().replace(":", "")
            secciones[seccion_actual] = ""
        elif seccion_actual:
            secciones[seccion_actual] += linea.strip() + "\n"

    return {
        "Resumen Ejecutivo": secciones.get("Resumen Ejecutivo", "Dato no disponible").strip(),
        "Indicadores Clave": secciones.get("Indicadores Clave", "Dato no disponible").strip(),
        "Expansión Tecnológica": secciones.get("Expansión Tecnológica", "Dato no disponible").strip(),
        "Diferenciadores Clave": secciones.get("Diferenciadores Clave", "Dato no disponible").strip(),
        "Contexto del Ecosistema": secciones.get("Contexto del Ecosistema", "Dato no disponible").strip(),
        "Oportunidades Estratégicas": secciones.get("Oportunidades Estratégicas", "Dato no disponible").strip(),
        "Viabilidad de Compra o Integración": secciones.get("Viabilidad de Compra o Integración", "Dato no disponible").strip(),
        "Recomendación Ejecutiva": secciones.get("Recomendación Ejecutiva", "Dato no disponible").strip(),
    }
