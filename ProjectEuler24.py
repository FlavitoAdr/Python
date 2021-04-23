#Desafio 24#
totalnumeros = 10
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
resultado = []
for i in seqgravada[999999]:
  resultado.append(str(i))
resultado = ''.join(resultado)
print(int(resultado))

#Resultado 2783915460
