#Desafio 20#
numero = []
numero.append(1)
for i in range(1, 101):
  tamanho = len(numero)
  for j in range(0, tamanho):
    numero[tamanho-j-1] *= i
    #print(numero, '   ', i)
    if numero[tamanho-j-1] > 9:
      if j == 0:
        numero.append(int(numero[tamanho-j-1]/10))
      else:
        numero[tamanho-j] +=  int(numero[tamanho-j-1]/10)
      conferir = numero[tamanho-j]
      conferirp = 1
      continuar = 1
      while conferir > 9:
        if tamanho-j+conferirp == len(numero):
          numero.append(int((numero[tamanho-j+conferirp-1])/10))
        else:
          numero[tamanho-j+conferirp] += int(numero[tamanho-j+conferirp-1]/10)
        numero[tamanho-j+conferirp-1] %= 10
        conferir = numero[tamanho-j+conferirp]
        conferirp += 1
      numero[tamanho-j-1] %= 10
print(sum(numero))

#Resultado 648
