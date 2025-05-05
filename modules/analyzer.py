# modules/analyzer.py

def analyze_text(text):
    """
    Genera un análisis tipo One-Pager a partir de texto extraído.
    
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
    
    # Heurística básica para rellenar las secciones
    resumen = text[:500] + "..." if len(text) > 500 else text
    palabras = text.lower()

    return {
        "Resumen Ejecutivo": resumen,

        "Indicadores Clave": "Dato no disponible (requiere métricas explícitas en el sitio)",

        "Expansión Tecnológica": "Presencia de términos como IA, Machine Learning o automatización" if any(kw in palabras for kw in ["ia", "machine learning", "automated", "automatización"]) else "Dato no disponible",

        "Diferenciadores Clave": "Dato no disponible (necesario un análisis más profundo)",

        "Contexto del Ecosistema": "Dato no disponible (no se identifican alianzas, mercado o socios)",

        "Oportunidades Estratégicas": "Potencial si se alinea con tendencias tecnológicas." if "tecnología" in palabras or "solución" in palabras else "Dato no disponible",

        "Viabilidad de Compra o Integración": "Posible si se valida escalabilidad y compatibilidad." if "servicio" in palabras or "api" in palabras else "Dato no disponible",

        "Recomendación Ejecutiva": "Requiere más análisis o contacto directo." 
    }
