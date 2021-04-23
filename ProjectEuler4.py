#Desafio 4#
palindromo = 0
for i in range(1, 1000):
  for j in range(1, 1000):
    multiplicacao = i * j
    if str(multiplicacao) == str(multiplicacao)[::-1]:
      if multiplicacao > palindromo:
        palindromo = multiplicacao
print(palindromo)
          
#Resultado 906609
