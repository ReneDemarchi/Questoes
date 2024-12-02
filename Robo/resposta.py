## fazer uma borda com zeros
n_linhas , n_colunas = [int(x) for x in input().split()]
coordenada_linha , coordenada_coluna =  [int(x) for x in input().split()]
## Cria a matriz
mat = [[x for x in input().split()] for _ in range(n_linhas)]
## Borda
for idx, linha in enumerate(mat):
    mat[idx].insert(0,'0')
    mat[idx].append(0)
linha_de_zero = ['0'] * (n_colunas+2)
mat.insert(0,linha_de_zero)
mat.append(linha_de_zero)
possivel_coordenadas = [(1,0),(-1,0),(0,1),(0,-1)]
## Solução
while True:
    for x,y in possivel_coordenadas:
        if mat[coordenada_linha + x][coordenada_coluna + y] == '1':
            mat[coordenada_linha][coordenada_coluna] = '0'
            coordenada_linha = coordenada_linha + x
            coordenada_coluna = coordenada_coluna + y
            break
    else:
        print(coordenada_linha,coordenada_coluna)
        break