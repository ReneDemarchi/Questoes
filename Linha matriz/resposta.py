linha_e = int(input())
operacao = input()
matriz = []
for l in range(11):
    linha = []
    for _ in range(12):
        linha.append(float(input()))
    matriz.append(linha)
if operacao == 'S':
    soma = 0
    for i in range(12):
        soma += matriz[linha_e][i]
    print(soma)
else:
    soma = 0
    for i in range(12):
        soma += matriz[linha_e][i]
    media = soma/12
    print(f"{media:.1f}")