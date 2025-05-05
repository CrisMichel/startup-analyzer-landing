# modules/pdf_generator.py

import pdfkit

config = pdfkit.configuration(wkhtmltopdf=r'C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe')

def generar_pdf(nombre_archivo, datos_startup, analisis):
    """
    Genera un PDF del One-Pager a partir de los datos y análisis.

    Args:
        nombre_archivo (str): Nombre del archivo de salida.
        datos_startup (dict): Datos generales de la startup.
        analisis (dict): Análisis tipo One-Pager.
    """

    # Crear el contenido HTML para el PDF
    html = f"""
    <h1>One-Pager Ejecutivo - {datos_startup['title']}</h1>
    <p><b>Fecha de análisis:</b> {datos_startup['fecha']}</p>
    <hr>
    <h2>Resumen Ejecutivo</h2>
    <p>{analisis['Resumen Ejecutivo']}</p>

    <h2>Datos Generales</h2>
    <p><b>Título:</b> {datos_startup['title']}</p>
    <p><b>Autores:</b> {', '.join(datos_startup['authors'])}</p>
    <p><b>Fecha de publicación:</b> {datos_startup['publish_date']}</p>

    <h2>Indicadores Clave</h2>
    <p>{analisis['Indicadores Clave']}</p>

    <h2>Expansión Tecnológica</h2>
    <p>{analisis['Expansión Tecnológica']}</p>

    <h2>Diferenciadores Clave</h2>
    <p>{analisis['Diferenciadores Clave']}</p>

    <h2>Contexto del Ecosistema</h2>
    <p>{analisis['Contexto del Ecosistema']}</p>

    <h2>Oportunidades Estratégicas</h2>
    <p>{analisis['Oportunidades Estratégicas']}</p>

    <h2>Viabilidad de Compra o Integración</h2>
    <p>{analisis['Viabilidad de Compra o Integración']}</p>

    <h2>Fuentes</h2>
    <p>{datos_startup['url']} (consultado el {datos_startup['fecha']})</p>
    """

    # Generar el PDF
    pdfkit.from_string(html, nombre_archivo, configuration=config)

    return nombre_archivo
