#Desafio 10#
primos = [2]
soma = 2;
for i in range(3, 2000000):
  nao = 0
  for j in range(0, len(primos)):
    if i % primos[j] == 0:
        nao = 1
  if nao == 0:
    primos.append(i)
    soma += i
print(soma)

#Resultado 142913828922
