numero = int(input('Qual o numero que deseja saber se é primo'))
raiz = numero**(1/2)
primo = True
primeiro_numero_divisivel = []
for i in range(2,int(raiz)+1):
    if numero%i == 0:
        primeiro_numero_divisivel.append(i)
        primeiro_numero_divisivel.append(int(numero/i))
        primo = False
if primo:
    print('é primo')
else:
    print('Esse numero não é primo')
    print(f'Numeros Divisivel são {primeiro_numero_divisivel}')
