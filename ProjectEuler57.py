#Desafio 57#
import math 
a = 3
b = 2
max = 1000
contagem = 0
for i in range(1, max+1):
  b = a + b
  a = 2 * b - a
  if int(math.log10(a)) > int(math.log10(b)):
    contagem += 1
print(contagem)

#Resultado 153
