#Desafio 63#
import math
e = 0
contagem = 0
contageminicial = 0
contagemfinal = 1
while contageminicial != contagemfinal:
  e += 1
  contageminicial = contagem
  for i in range(1, 10):
    valor = i**e
    tamanho = int(math.log10(valor)) + 1
    if  e == tamanho:
      contagem += 1
  contagemfinal = contagem
print(contagem)

#Resultado 49
