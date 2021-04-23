#Desafio 39#
lista = []
p = 1000
max = 0
maxe = 0
maxen = 1
for i in range(1, p+1):
  max = 0
  for j in range(1, i):
    for k in range(1, i):
      vc = (j**2+k**2)**(1/2)
      vci = int(vc)
      if vci/vc == 1:
        vc = int(vc)
      if type(vc) == int:
        if j+k+vc == i:
          max += 1
          lista.append([j,k,vc])
  if max > maxe:
    maxen = i
    maxe = max
print(maxen)

#Resultado 840
