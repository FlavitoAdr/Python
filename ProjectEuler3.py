#Desafio 3#
numero = 600851475143
divisor = 1
mprimos = 1
resto = 1
while mprimos!= numero:
  divisor += 2
  resto = numero % divisor
  if resto == 0:
    mprimos *= divisor
print(divisor)

#Resultado 6857
