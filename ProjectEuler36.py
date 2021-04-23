#Desafio 36#
soma = 0
for i in range(1, 1000001):
  decimal = str(i)
  decimali = decimal[::-1]
  binario = str(bin(i))
  binario = binario.split("0b")
  binario = ''.join(binario)
  binarioi = binario[::-1]
  if decimal == decimali:
    if binario == binarioi:
      soma +=i
print(soma)

#Resultado 872187
