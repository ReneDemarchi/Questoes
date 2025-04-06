polulacao_a = 80000
polulacao_b = 200000
numero_de_anos = 0
while True:
    if polulacao_a > polulacao_b:
        print(numero_de_anos)
        break
    numero_de_anos += 1
    polulacao_a = polulacao_a + polulacao_a*0.03
    polulacao_b = polulacao_b + polulacao_b*0.015