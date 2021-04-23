#Desafio 25#
import math

fibonacci = 0
fi1 = 1
fi2 = 1
a = 1
tamanho = 0
while tamanho < 999:
  fibonacci = fi1
  if fi2 > fi1:
    fibonacci = fi2
  if a % 2 == 0:
    fi1 = fi1+fi2
  else:
    fi2 = fi1+fi2
  a += 1
  tamanho = math.log10(fibonacci)
print(a)

#Resultado 4782
