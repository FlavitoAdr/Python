#Desafio 35#
max = 1000000
primos = [2]
for i in range(3, max, 2):
  nao = 0
  for j in range(0, len(primos)):
    if i % primos[j] == 0:
        nao = 1
  if nao == 0:
    primos.append(i)
primoc = 0
for i in primos:
  numero = i
  numerostr = str(numero)
  numerop = []
  contagem = 0
  for j in range(0, len(numerostr)):
    numerop.append([])
    numerop[j].append(numerostr[j:len(numerostr)])
    numerop[j].append(numerostr[0:j])
    numerop[j] = int(''.join(numerop[j]))
  for j in numerop:
    if primos.count(j) == 1:
      contagem += 1
  if contagem == len(numerop):
    primoc += 1
print(primoc)

#Resultado 55
