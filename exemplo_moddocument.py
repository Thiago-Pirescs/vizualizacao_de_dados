import fitz
from docx import Document

def pdf_to_docx(pdf, docx):
    pdf_document = fitz.open(pdf)
    doc = Document()

    for item in range(pdf_document.page_count):
        pagina = pdf_document.load_page(item)
        texto = pagina.get_text("text")
        doc.add_paragraph(texto)

    doc.save(docx)
    print(f"Arquivo .docx criado: {docx}")

pdf_to_docx("pdf_generico.pdf", "teste_extracao.docx")
