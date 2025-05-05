import requests
from bs4 import BeautifulSoup

def extract_url_data(url):
    """
    Extrae contenido de una página web usando requests + BeautifulSoup.
    """

    try:
        response = requests.get(url)
        response.raise_for_status()

        soup = BeautifulSoup(response.text, 'html.parser')

        # Titulo
        title = soup.title.string if soup.title else "Dato no disponible"

        # Meta descripción
        description_tag = soup.find("meta", attrs={"name": "description"})
        description = description_tag["content"] if description_tag else "Dato no disponible"

        # Texto del cuerpo
        paragraphs = soup.find_all('p')
        text = "\n".join([p.get_text() for p in paragraphs])

        return {
            "title": title.strip(),
            "authors": ["Dato no disponible"],
            "publish_date": "Dato no disponible",
            "text": text if text else "Dato no disponible"
        }

    except Exception as e:
        return {
            "title": "Error al extraer contenido",
            "authors": ["Error"],
            "publish_date": "Error",
            "text": f"No se pudo extraer contenido. Detalles: {e}"
        }
