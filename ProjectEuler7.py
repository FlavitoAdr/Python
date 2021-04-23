#Desafio 7#
primos = 2
numero = 1
while primos < 10002:
  naoprimo = 0
  divisor = 3
  numero += 2
  while divisor <= numero**(1/2):
    if numero % divisor == 0:
      naoprimo = 1
    divisor += 2
  if naoprimo == 0:
    primos += 1
print(numero)

#Resultado 104743
