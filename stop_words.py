from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt
from docx import Document

def extrair_texto(docx_path):
    doc = Document(docx_path)
    texto = ""
    for item in doc.paragraphs:
        texto += item.text + "\n"
    return texto

docx_path = 'teste_extracao.docx'

texto = extrair_texto(docx_path)

stopwords = set(STOPWORDS)

novas_palavras = []

with open("teste_extracao.docx", 'r', encoding='UTF8',) as item:

    [novas_palavras.append(word) for linha in item for word in linha.split()]

new_stopwords = stopwords.union(novas_palavras)

wordcloud = WordCloud(width=800, height=400, background_color = 'white').generate(texto)

plt.figure(figsize=(10, 5))
plt.imshow(wordcloud, interpolarion= 'bilinear')
plt.axis("off")
plt.show()