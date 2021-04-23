#Desafio 45#
t = []
p = []
h = []
qtd = 60000
for i in range(286, qtd+2):
  t.append(int(i*(i+1)/2))
  p.append(int(i*(3*i-1)/2))
  h.append(int(i*(2*i-1)))
for i in t:
  if p.count(i) == 1:
    if h.count(i) == 1:
      print(i)
      
#Resultado 1533776805
