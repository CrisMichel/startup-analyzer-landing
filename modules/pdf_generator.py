from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

def generar_pdf(nombre_archivo, datos_startup, analisis):
    c = canvas.Canvas(nombre_archivo, pagesize=letter)
    width, height = letter

    y = height - 50

    c.setFont("Helvetica-Bold", 16)
    c.drawString(50, y, f"One-Pager Ejecutivo - {datos_startup['title']}")
    y -= 30

    c.setFont("Helvetica", 12)
    c.drawString(50, y, f"Fecha de análisis: {datos_startup['fecha']}")
    y -= 40

    def agregar_linea(titulo, contenido):
        nonlocal y
        c.setFont("Helvetica-Bold", 12)
        c.drawString(50, y, titulo)
        y -= 20
        c.setFont("Helvetica", 10)
        for line in contenido.split("\n"):
            c.drawString(60, y, line)
            y -= 15
            if y < 50:
                c.showPage()
                y = height - 50
        y -= 10

    agregar_linea("Resumen Ejecutivo", analisis["Resumen Ejecutivo"])
    agregar_linea("Datos Generales", f"Título: {datos_startup['title']}\nAutores: {', '.join(datos_startup['authors'])}\nFecha de publicación: {datos_startup['publish_date']}")
    agregar_linea("Indicadores Clave", analisis["Indicadores Clave"])
    agregar_linea("Expansión Tecnológica", analisis["Expansión Tecnológica"])
    agregar_linea("Diferenciadores Clave", analisis["Diferenciadores Clave"])
    agregar_linea("Contexto del Ecosistema", analisis["Contexto del Ecosistema"])
    agregar_linea("Oportunidades Estratégicas", analisis["Oportunidades Estratégicas"])
    agregar_linea("Viabilidad de Compra o Integración", analisis["Viabilidad de Compra o Integración"])
    agregar_linea("Fuentes", f"{datos_startup['url']} (consultado el {datos_startup['fecha']})")

    c.save()

    return nombre_archivo
