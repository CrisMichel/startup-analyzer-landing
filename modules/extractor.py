from lxml import html
import requests

def extract_url_data(url):
    try:
        response = requests.get(url)
        response.raise_for_status()

        tree = html.fromstring(response.content)

        title = tree.findtext('.//title') or "Dato no disponible"

        paragraphs = tree.xpath('//p/text()')
        text = "\n".join(paragraphs)

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
