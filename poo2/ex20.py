while True:
    numero = int(input('numero'))
    valor = 1
    if numero > 0 and numero < 16:
        for i in range(1,numero+1):
            valor = valor*i
        print(valor)
    elif numero > 16:
        print('Numero maior ou igual a 16')
    elif numero == 0:
        print(0)
    valor_r_continuar = int(input('deseja calcular outra fatorial digite 1 se não 2'))
    if valor_r_continuar == 2:
        break
