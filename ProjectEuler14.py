#Desafio 14#
maior = 0
for i in range(2, 1000001):
  num = i
  contagem = 0
  while num != 1:
    contagem += 1
    if num % 2 == 0:
      num /= 2
    else:
      num = num*3+1
  if contagem > maior:
    memoria = i
    maior = contagem
print(memoria)

#Resultado 837799
