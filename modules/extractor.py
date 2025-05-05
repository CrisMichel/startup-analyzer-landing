# modules/extractor.py

from newspaper import Article

def extract_url_data(url):
    """
    Extrae contenido de una página web utilizando newspaper3k.
    
    Args:
        url (str): URL de la página.
    
    Returns:
        dict: Contiene título, autores, fecha, texto principal.
    """
    try:
        article = Article(url)
        article.download()
        article.parse()
        
        return {
            "title": article.title or "Dato no disponible",
            "authors": article.authors if article.authors else ["Dato no disponible"],
            "publish_date": article.publish_date.strftime("%d/%m/%Y") if article.publish_date else "Dato no disponible",
            "text": article.text if article.text else "Dato no disponible"
        }
    
    except Exception as e:
        return {
            "title": "Error al extraer contenido",
            "authors": ["Error"],
            "publish_date": "Error",
            "text": f"No se pudo extraer contenido. Detalles: {e}"
        }
