#Desafio 79#
senhas = '319, 680, 180, 690, 129, 620, 762, 689, 762, 318, 368, 710, 720, 710, 629, 168, 160, 689, 716, 731, 736, 729, 316, 729, 729, 710, 769, 290, 719, 680, 318, 389, 162, 289, 162, 718, 729, 319, 790, 680, 890, 362, 319, 760, 316, 729, 380, 319, 728, 716'
listanumeros = []
for i in range(0, 10):
  if senhas.count(str(i)) > 0:
    listanumeros.append(i)
senhas = senhas.split(', ')
listad = []
for i in listanumeros:
  listad.append([])
for i in senhas:
  p = i[0]
  for j in range(0, len(listanumeros)):
    if str(listanumeros[j]) == p:
      n = j
  if listad[n].count(i[1]) == 0:
    listad[n].append(i[1])
  if listad[n].count(i[2]) == 0:
    listad[n].append(i[2])
  p = i[1]
  for j in range(0, len(listanumeros)):
    if str(listanumeros[j]) == p:
      n = j
  if listad[n].count(i[2]) == 0:
    listad[n].append(i[2])
listaordem = []
listaordemp = []
for i in range(0, len(listad)):
  maiort = 0
  for j in range(0, len(listad)):
    if len(listad[j]) >= maiort and listaordemp.count(j) == 0:
      maior = listanumeros[j]
      maiort = len(listad[j])
      maiorp = j
  listaordem.append(str(maior))
  listaordemp.append(maiorp)
print(''.join(listaordem))

#Resultado 73162890
