while True:
    try:
        polulacao_a = float(input('População da cidade A  = '))
        polulacao_b = float(input('População da cidade B  = '))
        taxa_crecimeto_a = float(input('taxa de crecimento da ṕopulação da cidade A  = '))
        taxa_crecimeto_b = float(input('taxa de crecimento da ṕopulação da cidade B  = '))
        break
    except ValueError:
        print('Erro ao digita, vamos recomeçar')
numero_de_anos = 0
while True:
    if polulacao_a > polulacao_b:
        print(numero_de_anos)
        break
    numero_de_anos += 1
    polulacao_a = polulacao_a + polulacao_a*taxa_crecimeto_a
    polulacao_b = polulacao_b + polulacao_b*taxa_crecimeto_b