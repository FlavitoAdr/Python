#Desafio 46#
max = 5800
primos = [2]
for i in range(3, max, 2):
  nao = 0
  for j in range(0, len(primos)):
    if i % primos[j] == 0:
        nao = 1
  if nao == 0:
    primos.append(i)
compostos = []
for i in range(3, max, 2):
  if primos.count(i) == 0:
    compostos.append(i)
for i in compostos:
  teste = 0
  soma = 0
  for j in primos:
    if j < i:
      valor = ((i - j) * 2)**(1/2)
      valorint = int(valor)
      if valor == valorint:
        soma = 1
  if soma == 0:
    print(i)

#Resultado 5777
