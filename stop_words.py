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

for linha in texto.splitlines():
    for word in linha.split():
        novas_palavras.append(word)

new_stopwords = stopwords.union(novas_palavras)

wordcloud = WordCloud(width=800, height=400, background_color = 'white', stopwords=new_stopwords).generate(texto)

plt.figure(figsize=(10, 5))
plt.imshow(wordcloud, interpolation= 'bilinear')
plt.axis("off")
plt.show()