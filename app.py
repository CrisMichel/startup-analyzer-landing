import streamlit as st
from datetime import datetime

from modules.extractor import extract_url_data
from modules.analyzer import analyze_text
from modules.pdf_generator import generar_pdf

import os

st.set_page_config(page_title="Startup Analyzer", page_icon="🚀", layout="centered")

st.title("🚀 Analiza una Startup Tecnológica")
st.write("Ingresa la URL de la startup para generar un análisis ejecutivo:")

url = st.text_input("URL de la startup", placeholder="https://ejemplo.com")

if st.button("Generar Análisis"):
    if url.strip() == "":
        st.warning("Por favor ingresa una URL válida.")
    else:
        st.success("Análisis generado para: " + url)

        # Extraer datos de la URL
        data = extract_url_data(url)

        # Generar análisis
        analysis = analyze_text(data['text'])

        fecha = datetime.now().strftime('%d/%m/%Y')


        # st.header("📄 One-Pager Ejecutivo")

        # st.subheader("1️⃣ Resumen Ejecutivo")
        # st.write(analysis["Resumen Ejecutivo"])

        # st.subheader("2️⃣ Datos Generales")
        # st.write(f"**Título:** {data['title']}")
        # st.write(f"**Autores:** {', '.join(data['authors'])}")
        # st.write(f"**Fecha de publicación:** {data['publish_date']}")

        # st.subheader("3️⃣ Indicadores Clave")
        # st.write(analysis["Indicadores Clave"])

        # st.subheader("4️⃣ Expansión Tecnológica")
        # st.write(analysis["Expansión Tecnológica"])

        # st.subheader("5️⃣ Diferenciadores Clave")
        # st.write(analysis["Diferenciadores Clave"])

        # st.subheader("6️⃣ Contexto del Ecosistema")
        # st.write(analysis["Contexto del Ecosistema"])

        # st.subheader("7️⃣ Oportunidades Estratégicas")
        # st.write(analysis["Oportunidades Estratégicas"])

        # st.subheader("8️⃣ Viabilidad de Compra o Integración")
        # st.write(analysis["Viabilidad de Compra o Integración"])

        # st.subheader("9️⃣ Recomendación Ejecutiva")
        # st.write(analysis["Recomendación Ejecutiva"])

        # st.subheader("🔗 Fuentes")
        # st.write(f"{url} (consultado el {datetime.now().strftime('%d/%m/%Y')})")

    
        # Encabezado del análisis
        st.markdown(f"""
        ## 📄 One-Pager Ejecutivo
        **Startup:** {data['title']}
        
        **Fecha de análisis:** {fecha}
        
        ---
        """)

        # Función para mostrar cada sección como tarjeta
        def mostrar_seccion(titulo, contenido):
            with st.container():
                st.markdown(f"### {titulo}")
                st.write(contenido)
                st.markdown("---")

        # Mostrar cada sección en tarjeta
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
        st.write(f"{url} (consultado el {fecha})")

        # Crear nombre de archivo PDF
        nombre_pdf = f"{data['title']}_OnePager.pdf".replace(" ", "_")

        if st.button("📥 Descargar One-Pager en PDF"):
            datos_startup = {
                "title": data['title'],
                "authors": data['authors'],
                "publish_date": data['publish_date'],
                "fecha": fecha,
                "url": url
            }

            generar_pdf(nombre_pdf, datos_startup, analysis)

            with open(nombre_pdf, "rb") as file:
                btn = st.download_button(
                    label="Descargar PDF",
                    data=file,
                    file_name=nombre_pdf,
                    mime="application/pdf"
                )
            
            # Limpiar archivo temporal
            os.remove(nombre_pdf)
