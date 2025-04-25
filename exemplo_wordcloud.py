from wordcloud import WordCloud
import matplotlib.pyplot as plt
from docx import Document

def extrair_texto(docx_path):
    doc = Document(docx_path)
    texto = ""
    for item in doc.paragraphs:
        texto += item.text + "\n"
    return texto

docx_path = 'teste_extracao.docx'

text = extrair_texto(docx_path)

nuvem = WordCloud(width=800, height=400, background_color='black').generate(text)

plt.figure(figsize=(10, 5))
plt.imshow(nuvem, interpolation = 'bilinear')
plt.axis("off")
plt.show()