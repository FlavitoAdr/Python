#Desafio 28#
lado = 1001
matriz = []
for i in range(0, lado):
  matriz.append([])
  for j in range(0, lado):
    matriz[i].append(0)
meio = int((lado-1)/2)
p1 = meio+1
p2 = meio
a1 = meio+1
a2 = meio+1
for i in range(1, lado**2+1):
  d1 = p1-a1
  d2 = p2-a2
  a1 = p1
  a2 = p2
  if matriz[p1+d2][p2-d1] == 0:
    p1 += d2
    p2 -= d1
    matriz[p1][p2] = i
  else:
    p1 += d1
    p2 += d2
    matriz[p1][p2] = i
soma = 0
for i in range(0, lado):
  soma += matriz[i][i]
  soma += matriz[lado-(i+1)][i]
soma -= 1
print(soma)

#Resultado 669171001
