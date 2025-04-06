n_par = []
n_impar = []
for i in range(1,11,1):
    numero = int(input())
    if numero % 2 == 0:
        n_par.append(numero)
    else:
        n_impar.append(numero)
print(f'Essa é a quantidade de numeros pares {len(n_par)}')
print(f'Essa é a quantidade de numeros impares {len(n_impar)}')