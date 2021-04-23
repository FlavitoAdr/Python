#Desafio 92#
max = 10000000
i = 2
processo = []
contagem = 0
for i in range(1, max):
  ci = i
  while ci != 1 and ci != 89:
    listai = str(ci)
    ci = 0
    for j in listai:
      ci += int(j)**2
  if ci == 89:
    contagem += 1
print(contagem)

#Resultado 8581146
