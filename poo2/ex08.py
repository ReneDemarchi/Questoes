numeros = [int(n) for n in (input("digite os 5 numeros").split())]
soma = sum(numeros)
media = soma/len(numeros)
print(f'soma = {soma} ---- media {media}')