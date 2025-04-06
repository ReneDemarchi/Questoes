while True:
    nota_entrada = input('Qual a nota do aluno')
    try:
        nota_entrada = float(nota_entrada)
        if nota_entrada >= 0 and nota_entrada <= 10:
            print('Nota adicionada')
            break
        else:
            print(f'Nota invalida digite uma nota de 0 a 10 voce digitou {nota_entrada}')
    except:
        print('Voce digitou uma nota invalida.')

