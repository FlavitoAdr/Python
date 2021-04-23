#Desafio 30#
soma1 = 0
for i in range(2, 200000):
  soma2 = 0
  numstr = list(str(i))
  for j in numstr:
    soma2 += int(j)**5
  if soma2 == i:
    soma1 += soma2
print(soma1)

#Resultado 443839
