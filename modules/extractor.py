import requests
from bs4 import BeautifulSoup
import re

def is_relevant(text):
    return text and text.strip() and len(text.strip()) > 3

def clean_text(text):
    return re.sub(r'\s+', ' ', text).strip()

def preprocess_text(text):
    """
    Limpia el texto eliminando repeticiones y contenido poco informativo.
    También elimina oraciones repetidas inteligentes.
    """
    # Dividir en oraciones básicas
    sentences = re.split(r'(?<=[.!?])\s+', text)

    cleaned_sentences = []
    seen = set()

    for sentence in sentences:
        sentence_clean = sentence.strip()

        if not sentence_clean:
            continue

        # Ignorar menús o palabras clave poco informativas
        skip_keywords = ["resources", "about", "more", "book a demo", "get started", "menu", "quicklinks", "legal", "privacy policy", "contact"]
        if any(kw in sentence_clean.lower() for kw in skip_keywords):
            continue

        # Normalizar para comparación
        normalized = re.sub(r'\W+', '', sentence_clean).lower()

        if normalized in seen:
            continue

        seen.add(normalized)
        cleaned_sentences.append(sentence_clean)

    return "\n".join(cleaned_sentences)


def extract_url_data(url):
    try:
        response = requests.get(url, timeout=20)
        response.raise_for_status()

        soup = BeautifulSoup(response.content, "html.parser")

        title = soup.title.string.strip() if soup.title else "Dato no disponible"

        tags = soup.find_all(["h1", "h2", "h3", "h4", "h5", "h6", "p", "span", "li", "button", "div"])

        aria_texts = [tag.get("aria-label") for tag in soup.find_all(attrs={"aria-label": True})]
        alt_texts = [tag.get("alt") for tag in soup.find_all(attrs={"alt": True})]
        title_texts = [tag.get("title") for tag in soup.find_all(attrs={"title": True})]

        all_texts = []

        for tag in tags:
            text = tag.get_text(separator=" ", strip=True)
            if is_relevant(text):
                all_texts.append(clean_text(text))

        for attr_list in [aria_texts, alt_texts, title_texts]:
            for text in attr_list:
                if is_relevant(text):
                    all_texts.append(clean_text(text))

        # Preprocesar para limpiar
        full_text = preprocess_text("\n".join(all_texts)) if all_texts else "Dato no disponible"

        return {
            "title": title,
            "authors": ["Dato no disponible"],
            "publish_date": "Dato no disponible",
            "text": full_text
        }

    except Exception as e:
        return {
            "title": "Error al extraer contenido",
            "authors": ["Error"],
            "publish_date": "Error",
            "text": f"No se pudo extraer contenido. Detalles: {e}"
        }
