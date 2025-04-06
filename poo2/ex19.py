entrada = [int(n) for n in input('Numeros').split() if int(n) < 1000 and int(n) > 0]
menor = min(entrada)
maior = max(entrada)
soma = sum(entrada)
print(menor,maior,soma)