### pedir idade das pessoas
idades = []
while True:
    idade = int(input("Qual sua idade ? "))

    print('''Para cadastrar mais pessoas digite 1
            Para calcular a media Digite 2''')
    navegação = input('')
    idades.append(idade)
    if navegação == '2':
        break
### calcular a media
media = sum(idades)/len(idades)
### Mostrar em qual faixa a media de idade esta
if media <= 25:
    print(f'Jovem {media}')
elif media <= 60:
    print(f'Adulto {media}')
else:
    print(f'Idosa {media}')