#Desafio 53#
fmax = 100
fatorial = []
fatorial.append(1)
for i in range(0, fmax):
  fatorial.append(fatorial[i]*(i+1))
contagem = 0
for i in range(0, fmax+1):
  for j in range(0, i):
    if fatorial[i] / (fatorial[j] * fatorial[(i - j)]) > 1000000:
      contagem += 1
print(contagem)

#Resultado 4075
