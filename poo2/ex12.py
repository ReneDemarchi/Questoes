numeros_escolido = int(input('Qual o numero q deseja ver a tabuada  ->'))
if numeros_escolido > 0 and numeros_escolido <= 10:
    for i in range(1,11,1):
        print(f'{numeros_escolido} x {i} = {numeros_escolido*i}')
else:
    print('Numero escolido invalido')
