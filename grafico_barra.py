from collections import Counter
import matplotlib.pyplot as plt
from wordcloud import STOPWORDS


texto = """
Python é uma linguagem de programação de alto nível amplamente utilizada para diversos tipos de aplicações, incluindo ciência de dados, aprendizado de máquina, desenvolvimento web, automação e análise de dados. Criada por Guido van Rossum e lançada pela primeira vez em 1991, Python ganhou popularidade devido à sua simplicidade e facilidade de aprendizado.

Com uma sintaxe clara e legível, Python permite que os desenvolvedores foquem mais na resolução de problemas do que na complexidade da linguagem em si. Além disso, a vasta biblioteca padrão e a enorme quantidade de bibliotecas de terceiros tornam Python extremamente versátil.
"""

palavras = texto.lower().replace(",", "").replace(".", "").split()
contagem = Counter(palavras)

palavras_mais_comuns = contagem.most_common(10)
palavras, frequencias = zip(*palavras_mais_comuns)

plt.figure(figsize=(10, 5))
plt.bar(palavras, frequencias, color="black")
plt.title("Frequência das palavras mais comuns", fontsize=16)
plt.xlabel("Palavras", fontsize=12)
plt.ylabel("Frequência", fontsize=12)
plt.xticks(rotation = 45)
plt.tight_layout()
plt.show()