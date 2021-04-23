#Desafio 21#
soma = 0
for valor in range(1, 10001):
  amigavel1 = 0
  for i in range(1,int(valor/2+1)):
    valorteste = int(valor/i)
    valorteste *= i
    if valorteste == valor:
      amigavel1 += i
  amigavel2 = 0
  for i in range(1,int(amigavel1/2+1)):
    valorteste = int(amigavel1/i)
    valorteste *= i
    if valorteste == amigavel1:
      amigavel2 += i
  if amigavel2 == valor:
    if valor != amigavel1:
      soma+=valor
print(soma)

#Resultado 31626
