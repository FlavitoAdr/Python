#Desafio 2#
soma = 0
fibonacci = 0
fi1 = 1
fi2 = 1
a = 1
while fibonacci < 4000000:
  fibonacci = fi1
  if fi2 > fi1:
    fibonacci = fi2
  if fibonacci % 2 == 0:
    soma += fibonacci
  if a % 2 == 0:
    fi1 = fi1+fi2
  else:
    fi2 = fi1+fi2
  a += 1
print(soma)

#Resultado 4613732
