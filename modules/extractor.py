from lxml import html
import requests

def extract_url_data(url):
    try:
        response = requests.get(url)
        response.raise_for_status()

        tree = html.fromstring(response.content)

        # Extraer título de la página
        title = tree.findtext('.//title') or "Dato no disponible"

        # Extraer contenido de párrafos
        paragraphs = tree.xpath('//p/text()')

        # Extraer títulos importantes
        headers = tree.xpath('//h1/text() | //h2/text() | //h3/text()')

        # Extraer meta descripción
        meta_desc = tree.xpath('//meta[@name="description"]/@content')

        # Extraer textos alternativos de imágenes
        alt_texts = tree.xpath('//img/@alt')

        # Unir todo el contenido en un solo texto
        all_text = paragraphs + headers + meta_desc + alt_texts
        text = "\n".join([t.strip() for t in all_text if t.strip()])

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
