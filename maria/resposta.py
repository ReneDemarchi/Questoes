numero_de_nomes = int(input())
nomes = [input() for _ in range(numero_de_nomes)]
soma = 0
for nome in nomes:
    if 'Maria' in nome.split():
        soma += 1
print(soma)