#Desafio 48#
max = 1000
soma = 0
for i in range(1, max+1):
  soma += i**i
somastr = str(soma)
print(''.join(list(somastr)[len(somastr)-10:len(somastr)]))

#Resultado 9110846700
