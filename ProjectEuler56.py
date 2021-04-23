#Desafio 56#
max = 100
maior = 0
for i in range(1, max):
  for j in range(1, max):
    soma = 0
    resultado = i**j
    resultadostr = list(str(resultado))
    for k in resultadostr:
      soma += int(k)
    if soma > maior:
      maior = soma
print(maior)

#Resultado 972
