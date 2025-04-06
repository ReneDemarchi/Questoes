candidatos = {"c1":0,"c2":0,'c3':0}
print(type(candidatos))
numero_de_eleitores = int(input('Qual o numero de eleitores'))
for i in range(numero_de_eleitores):
    voto = input('Vote em uma das opções 1 2 ou 3')
    if voto == '1':
        candidatos["c1"] += 1
    elif voto == '2':
        candidatos['c2'] += 1
    elif voto == '3':
        candidatos['c3'] += 1


maximo_votos = max(candidatos.values())
candidatos_mais_votos = [cand for cand,votos in candidatos.items() if maximo_votos == votos]
if len(candidatos_mais_votos) == 1:
    print(candidatos_mais_votos)
else:
    print(f'Houve um empate entre esses candidatos {candidatos_mais_votos}')