#Desafio 55#
max = 10000
nlychrel = 0
for i in range(1, max+1):
  palindromo = 0
  valor = i
  for i in range(0, 50):
    valori = int(str(valor)[::-1])
    soma = valor + valori
    if str(soma) == str(soma)[::-1]:
      palindromo = 1
    valor = soma
  if palindromo == 0:
    nlychrel += 1
print(nlychrel)

#Resultado 249
