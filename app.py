import streamlit as st
from datetime import datetime
from modules.extractor import extract_url_data

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

        st.header("📄 One-Pager Ejecutivo")

        st.subheader("1️⃣ Resumen Ejecutivo")
        st.write("Dato no disponible")  # Esto se llenará en el Módulo 3

        st.subheader("2️⃣ Datos Generales")
        st.write(f"**Título:** {data['title']}")
        st.write(f"**Autores:** {', '.join(data['authors'])}")
        st.write(f"**Fecha de publicación:** {data['publish_date']}")

        st.subheader("3️⃣ Indicadores Clave")
        st.write("Dato no disponible")

        st.subheader("4️⃣ Expansión Tecnológica")
        st.write("Dato no disponible")

        st.subheader("5️⃣ Diferenciadores Clave")
        st.write("Dato no disponible")

        st.subheader("6️⃣ Contexto del Ecosistema")
        st.write("Dato no disponible")

        st.subheader("7️⃣ Oportunidades Estratégicas")
        st.write("Dato no disponible")

        st.subheader("8️⃣ Viabilidad de Compra o Integración")
        st.write("Dato no disponible")

        st.subheader("9️⃣ Recomendación Ejecutiva")
        st.write("Dato no disponible")

        st.subheader("🔗 Fuentes")
        st.write(f"{url} (consultado el {datetime.now().strftime('%d/%m/%Y')})")
