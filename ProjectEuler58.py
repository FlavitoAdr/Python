#Desafio 58#
diagonais = [1]
valor = 1
lado = 1
contagem = 0
while valor > 0.1:
  lado += 2
  nl = int((lado - 1) / 2) - 1
  diagonais.append(diagonais[nl * 4] + (nl + 1) * 2)
  diagonais.append(diagonais[nl * 4 + 1] + (nl + 1) * 2)
  diagonais.append(diagonais[nl * 4 + 2] + (nl + 1) * 2)
  diagonais.append(diagonais[nl * 4 + 3] + (nl + 1) * 2)
  for i in range(1, 5):
    maximo = diagonais[int(((lado - 1) / 2 - 1)) * 4 + i]
    divisivel = 0
    j = 1
    while divisivel == 0 and j < maximo**(1/2):
      j += 2
      if maximo % j == 0:
        divisivel = 1
    if divisivel == 0:
      contagem += 1
  valor = contagem / (lado * 2 - 1)
print(lado)

#Resultado 26241
