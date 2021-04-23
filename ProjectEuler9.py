#Desafio 9#
for i in range(1, 1000):
  for j in range(i, 1000):
    if i + j + (i**2+j**2)**(1/2) == 1000:
      valor = int(i * j * (i**2+j**2)**(1/2))
print(valor)

#Resultado 31875000
