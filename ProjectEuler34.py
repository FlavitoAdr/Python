#Desafio 34#
fmax = 9
fatorial = []
fatorial.append(1)
for i in range(0, fmax):
  fatorial.append(fatorial[i]*(i+1))
soma1 = 0
for i in range(3, 50000):
  soma2 = 0
  numstr = list(str(i))
  for j in numstr:
    soma2 += fatorial[int(j)]
  if soma2 == i:
    soma1 += soma2
print(soma1)

#Resultado 40730
