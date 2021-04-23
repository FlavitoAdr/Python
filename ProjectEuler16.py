#Desafio 16#
numero = []
numero.append(1)
for i in range(0, 1000):
  tamanho = len(numero)
  for j in range(0, tamanho):
    numero[tamanho-j-1] *= 2
    if numero[tamanho-j-1] > 9:
      numero[tamanho-j-1] -= 10
      if j == 0:
        numero.append(1)
      else:
        numero[tamanho-j] += 1
print(sum(numero))

#Resultado 1366
