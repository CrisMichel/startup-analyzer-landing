# app.py

import streamlit as st
from datetime import datetime
from modules.extractor import extract_url_data
from modules.analyzer import analyze_text
from modules.pdf_generator import generar_pdf
import os
import re

def clean_filename(filename):
    return re.sub(r'[\\/*?:"<>|]', "", filename)

# Configuracion de la pagina
st.set_page_config(page_title="Startup Analyzer", page_icon="🚀", layout="wide")

# Estilos personalizados
st.markdown("""
<style>
body {
    background-color: #f5f5f5;
}
.sidebar .sidebar-content {
    background-color: #ffffff;
    padding: 20px;
}
h1, h2, h3 {
    color: #0A66C2;
}
.card {
    background-color: #ffffff;
    padding: 20px;
    border-radius: 10px;
    box-shadow: 0 2px 5px rgba(0,0,0,0.1);
    margin-bottom: 20px;
}
</style>
""", unsafe_allow_html=True)

# Sidebar de navegación
with st.sidebar:
    st.title("📚 Menú")
    st.info("Ingresa una URL para analizar")

# Título principal
st.markdown("<h1>🚀 Analizador de Startups Tecnológicas</h1>", unsafe_allow_html=True)

# Input de URL
url = st.text_input("URL de la startup", placeholder="https://ejemplo.com")

# Inicializar session_state
if "url" not in st.session_state:
    st.session_state.url = ""
if "data" not in st.session_state:
    st.session_state.data = None
if "analysis" not in st.session_state:
    st.session_state.analysis = None

# Botón para generar análisis
if st.button("🚦 Analizar Startup"):
    if url.strip() == "":
        st.warning("Por favor ingresa una URL válida.")
    else:
        st.session_state.url = url
        st.success("Análisis generado para: " + url)

        # Extraer datos y analizar
        data = extract_url_data(url)
        analysis = analyze_text(data['text'])

        # Guardar en session_state
        st.session_state.data = data
        st.session_state.analysis = analysis

# Mostrar análisis si ya está generado
if st.session_state.analysis:
    data = st.session_state.data
    analysis = st.session_state.analysis
    fecha = datetime.now().strftime('%d/%m/%Y')

    # Función para mostrar secciones con estilo de tarjeta
    def card(titulo, contenido):
        st.markdown(f"""
        <div class='card'>
        <h3>{titulo}</h3>
        <p>{contenido}</p>
        </div>
        """, unsafe_allow_html=True)

    # Mostrar tarjetas
    card("Resumen Ejecutivo", analysis["Resumen Ejecutivo"])

    card("Datos Generales", f"**Título:** {data['title']}<br>**Autores:** {', '.join(data['authors'])}<br>**Fecha de publicación:** {data['publish_date']}")

    card("Indicadores Clave", analysis["Indicadores Clave"])
    card("Expansión Tecnológica", analysis["Expansión Tecnológica"])
    card("Diferenciadores Clave", analysis["Diferenciadores Clave"])
    card("Contexto del Ecosistema", analysis["Contexto del Ecosistema"])
    card("Oportunidades Estratégicas", analysis["Oportunidades Estratégicas"])
    card("Viabilidad de Compra o Integración", analysis["Viabilidad de Compra o Integración"])

    # Fuentes
    st.markdown("<h2 style='margin-top:30px;'>Fuentes</h2>", unsafe_allow_html=True)
    st.write(f"{st.session_state.url} (consultado el {fecha})")

    # Datos para el PDF
    datos_startup = {
        "title": data['title'],
        "authors": data['authors'],
        "publish_date": data['publish_date'],
        "fecha": fecha,
        "url": st.session_state.url
    }

    # Generar PDF
    raw_filename = f"{data['title']}_OnePager.pdf".replace(" ", "_")
    nombre_pdf = clean_filename(raw_filename)

    generar_pdf(nombre_pdf, datos_startup, analysis)

    with open(nombre_pdf, "rb") as file:
        st.download_button(
            label="📥 Descargar One-Pager en PDF",
            data=file,
            file_name=nombre_pdf,
            mime="application/pdf"
        )

    os.remove(nombre_pdf)
