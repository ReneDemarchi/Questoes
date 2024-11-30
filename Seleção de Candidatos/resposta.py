regras = []
vagas = dict()

### entradas
while True:
    input_texto = input()
    if input_texto == '0 0':
        break
    passo, regra, cat, priors = input_texto.split()
    prioridades = [set(p.split(',')) for p in priors.split(";")]
    regras.append({'passo': passo, 'regra': regra, 'categoria': cat, 'prioridade': prioridades})
    vagas[cat] = 0
for _ in range(len(vagas)):
    tipo_da_vaga, quantidade = input().split()
    vagas[tipo_da_vaga] = int(quantidade)
quantidade_de_candidatos = int(input())
lista_candidatos = []
for _ in range(quantidade_de_candidatos):
    ordem, n_inscrição, categorias = input().split()
    categorias = set(c for c in categorias.split(','))
    lista_candidatos.append({'ordem': ordem, 'inscrição': n_inscrição, 'categoria': categorias})
lista_de_aprovados = []

### Logica de tratamentos

for regra in regras:
    for candidato in lista_candidatos[:]: # como tirar esse slice ?
        if vagas[regra['categoria']] != 0:
            categorias_candidato = {categorias for categorias in candidato['categoria']}
            for prioridade_conjunto in regra['prioridade']:
                oredem_prioridade = {prioridade for prioridade in prioridade_conjunto}
                categoria_encontrada = not categorias_candidato.isdisjoint(oredem_prioridade)
                if categoria_encontrada:
                    if candidato not in lista_de_aprovados:
                        lista_de_aprovados.append(candidato['inscrição'])
                        vagas[regra['categoria']] -= 1
                        lista_candidatos.remove(candidato)
                        break
for c in sorted(lista_de_aprovados):
    print(c)