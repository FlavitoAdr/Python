#Desafio 43#
totalnumeros = 10
nprimos = [2, 3, 5, 7, 11, 13, 17]
sequencia = []
for i in range(0, totalnumeros):
  sequencia.append(i)
soma = 0
fatorial = []
fatorial.append(1)
for i in range(0, totalnumeros):
  fatorial.append(fatorial[i]*(i+1))
valor = []
for i in range(1, fatorial[totalnumeros]+1):
  encontrado = 0
  for j in range(0, totalnumeros):
    if i % fatorial[totalnumeros-j] == 0 and encontrado == 0:
      valor.append(j-1)
      encontrado = 1
seqgravada = []
for i in range(0, fatorial[totalnumeros]):
  seqgravada.append([j for j in sequencia])
  v1 = sequencia[valor[i]]
  v2 = sequencia[valor[i]+1]
  sequencia[valor[i]] = v2
  sequencia[valor[i]+1] = v1
  if valor[i] < totalnumeros - 3:
    for j in range(0, int((totalnumeros-(valor[i]+2))/2)):
      v1 = sequencia[valor[i]+2+2*j]
      v2 = sequencia[valor[i]+3+2*j]
      sequencia[valor[i]+2+2*j] = v2
      sequencia[valor[i]+3+2*j] = v1
seqgravada.sort()
for i in seqgravada:
  a = 1
  m = 0
  if i[0] != 0:
    for j in range(0, 7):
      valor = 0
      for k in range(0, 3):
        valor += int(i[a+k]*10**(2-k))
      if valor % nprimos[a-1] == 0:
        m += 1
      a += 1
    if m == 7:
      numero = 0
      for k in range(0, 10):
        numero += int(i[k]*10**(9-k))
      soma += numero
print(soma)

#Resultado 16695334890
