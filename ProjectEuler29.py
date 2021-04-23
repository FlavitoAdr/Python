#Desafio 29#
c = 100
lista = []
for a in range(2, c+1):
  for b in range(2, c+1):
    v = a**b
    if lista.count(v) == 0:
      lista.append(v)
print(len(lista))

#Resultado 9183
