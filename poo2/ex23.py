def primo(numero):
    raiz = numero ** (1 / 2)
    primo = True
    primeiro_numero_divisivel = []
    for i in range(2, int(raiz) + 1):
        if numero % i == 0:
            primeiro_numero_divisivel.append(i)
            primeiro_numero_divisivel.append(int(numero / i))
            primo = False
    if primo:
        print('é primo')
    else:
        print('Esse numero não é primo')
        print(f'Numeros Divisivel são {primeiro_numero_divisivel}')
    return numero,primo,int(raiz+1)

intervalo = int(input('Qual o intervalo ?'))
primos = []
for i in range(2,intervalo+1,1):
    n_teste = primo(i)
    if n_teste[1] == True:
        primos.append(n_teste)

print(primos)
