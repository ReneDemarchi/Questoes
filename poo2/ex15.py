n1 = 0
n2 = 1
serie_f = [0,1]

n_numero_de_fiponate = int(input('N numero da serie de fiponate'))

for i in range(1,n_numero_de_fiponate-1):
    novo_numero = n1 + n2
    n1 = n2
    n2 = novo_numero
    serie_f.append(novo_numero)
if n_numero_de_fiponate >= 2:
    print(serie_f)
elif n_numero_de_fiponate == 1:
    print(serie_f[:1])
else:
    print(serie_f[0])