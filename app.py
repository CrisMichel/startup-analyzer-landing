# app.py

import streamlit as st
from datetime import datetime
from modules.extractor import extract_url_data
from modules.analyzer import analyze_text
from modules.pdf_generator import generar_pdf
import os
import re

# Configurar página
st.set_page_config(page_title="Startup Analyzer", page_icon="🚀", layout="wide")

# Agregar estilos personalizados
st.markdown("""
<style>
body {
    background-color: #F5F5F5;
}

h1, h2, h3 {
    color: #0A66C2;
}

.card {
    background-color: #FFFFFF;
    padding: 20px;
    border-radius: 10px;
    box-shadow: 0 2px 8px rgba(0,0,0,0.05);
    margin-bottom: 20px;
}

hr {
    border-top: 1px solid #DDD;
}
</style>
""", unsafe_allow_html=True)

# Sidebar
with st.sidebar:
    st.header("📚 Menú")
    st.write("- Inicio")
    st.write("- Generar Análisis")
    st.write("- Catálogo (próximamente)")

st.markdown("<h1>🚀 Analizador de Startups</h1>", unsafe_allow_html=True)
st.write("Ingresa la URL de la startup para generar un análisis ejecutivo:")

# Inicializar session_state
if "url" not in st.session_state:
    st.session_state.url = ""
if "data" not in st.session_state:
    st.session_state.data = None
if "analysis" not in st.session_state:
    st.session_state.analysis = None

# Input de URL
url = st.text_input("URL de la startup", placeholder="https://ejemplo.com")

if st.button("🚦 Analizar Startup"):
    if url.strip() == "":
        st.warning("Por favor ingresa una URL válida.")
    else:
        st.session_state.url = url
        st.success("Análisis generado para: " + url)
        data = extract_url_data(url)
        analysis = analyze_text(data['text'])
        st.session_state.data = data
        st.session_state.analysis = analysis

# Mostrar análisis
if st.session_state.analysis:

    data = st.session_state.data
    analysis = st.session_state.analysis
    fecha = datetime.now().strftime('%d/%m/%Y')

    st.sidebar.title("🔎 Navegación rápida")
    seccion = st.sidebar.radio("Ir a sección", [
        "Resumen Ejecutivo",
        "Datos Generales",
        "Indicadores Clave",
        "Expansión Tecnológica",
        "Diferenciadores Clave",
        "Contexto del Ecosistema",
        "Oportunidades Estratégicas",
        "Viabilidad de Compra o Integración",
        "Fuentes"
    ])

    def card(titulo, contenido):
        st.markdown(f"""
        <div class='card'>
            <h3>{titulo}</h3>
            <p>{contenido}</p>
        </div>
        """, unsafe_allow_html=True)

    if seccion == "Resumen Ejecutivo":
        card("Resumen Ejecutivo", analysis["Resumen Ejecutivo"])

    elif seccion == "Datos Generales":
        st.markdown("<div class='card'><h3>Datos Generales</h3>", unsafe_allow_html=True)
        st.write(f"**Título:** {data['title']}")
        st.write(f"**Autores:** {', '.join(data['authors'])}")
        st.write(f"**Fecha de publicación:** {data['publish_date']}")
        st.markdown("</div>", unsafe_allow_html=True)

    elif seccion == "Indicadores Clave":
        card("Indicadores Clave", analysis["Indicadores Clave"])

    elif seccion == "Expansión Tecnológica":
        card("Expansión Tecnológica", analysis["Expansión Tecnológica"])

    elif seccion == "Diferenciadores Clave":
        card("Diferenciadores Clave", analysis["Diferenciadores Clave"])

    elif seccion == "Contexto del Ecosistema":
        card("Contexto del Ecosistema", analysis["Contexto del Ecosistema"])

    elif seccion == "Oportunidades Estratégicas":
        card("Oportunidades Estratégicas", analysis["Oportunidades Estratégicas"])

    elif seccion == "Viabilidad de Compra o Integración":
        card("Viabilidad de Compra o Integración", analysis["Viabilidad de Compra o Integración"])

    elif seccion == "Fuentes":
        card("Fuentes", f"{st.session_state.url} (consultado el {fecha})")

    # PDF
    datos_startup = {
        "title": data['title'],
        "authors": data['authors'],
        "publish_date": data['publish_date'],
        "fecha": fecha,
        "url": st.session_state.url
    }

    raw_filename = f"{data['title']}_OnePager.pdf".replace(" ", "_")
    nombre_pdf = re.sub(r'[\\/*?:\"<>|]', "", raw_filename)

    generar_pdf(nombre_pdf, datos_startup, analysis)

    with open(nombre_pdf, "rb") as file:
        st.download_button(
            label="📥 Descargar One-Pager en PDF",
            data=file,
            file_name=nombre_pdf,
            mime="application/pdf"
        )

    os.remove(nombre_pdf)