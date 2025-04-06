numero = int(input('numero'))
valor = 1
if numero > 0:
    for i in range(1,numero+1):
        valor = valor*i
    print(valor)
else:
    print('0')