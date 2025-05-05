# app.py

import streamlit as st
from datetime import datetime
from modules.extractor import extract_url_data
from modules.analyzer import analyze_text
# from modules.pdf_generator import generar_pdf
import os

import re

def clean_filename(filename):
    return re.sub(r'[\\/*?:"<>|]', "", filename)


# Configuración inicial de la página
st.set_page_config(page_title="Startup Analyzer", page_icon="🚀", layout="centered")

st.title("🚀 Analiza una Startup Tecnológica")
st.write("ACTUALIZACIÓN PEQUEÑA SOLO PARA FORZAR REDEPLOY")
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

# Botón para generar análisis
if st.button("Generar Análisis"):
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

    st.header("📄 One-Pager Ejecutivo")
    
    st.markdown(f"""
    ## 📌 Startup: {data['title']}
    **Fecha de análisis:** {fecha}
    ---
    """)

    # Función para mostrar cada sección como tarjeta
    def mostrar_seccion(titulo, contenido):
        with st.container():
            st.markdown(f"### {titulo}")
            st.write(contenido)
            st.markdown("---")

    mostrar_seccion("Resumen Ejecutivo", analysis["Resumen Ejecutivo"])

    st.markdown("### Datos Generales")
    st.write(f"**Título:** {data['title']}")
    st.write(f"**Autores:** {', '.join(data['authors'])}")
    st.write(f"**Fecha de publicación:** {data['publish_date']}")
    st.markdown("---")

    mostrar_seccion("Indicadores Clave", analysis["Indicadores Clave"])
    mostrar_seccion("Expansión Tecnológica", analysis["Expansión Tecnológica"])
    mostrar_seccion("Diferenciadores Clave", analysis["Diferenciadores Clave"])
    mostrar_seccion("Contexto del Ecosistema", analysis["Contexto del Ecosistema"])
    mostrar_seccion("Oportunidades Estratégicas", analysis["Oportunidades Estratégicas"])
    mostrar_seccion("Viabilidad de Compra o Integración", analysis["Viabilidad de Compra o Integración"])

    st.markdown("### Fuentes")
    st.write(f"{st.session_state.url} (consultado el {fecha})")
    st.markdown("---")

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

    # generar_pdf(nombre_pdf, datos_startup, analysis)

    # with open(nombre_pdf, "rb") as file:
    #     st.download_button(
    #         label="📥 Descargar One-Pager en PDF",
    #         data=file,
    #         file_name=nombre_pdf,
    #         mime="application/pdf"
    #     )

    # os.remove(nombre_pdf)
