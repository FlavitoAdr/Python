#Desafio 15#
tabela = []
for i in range(0, 21):
  tabela.append([1])
for i in range(0, 20):
  tabela[0].append(1)
for i in range(1, 21):
  for j in range(1, 21):
    tabela[j].append(tabela[j][i-1] + tabela[j-1][i])
print(tabela[20][20])

#Resultado 137846528820
