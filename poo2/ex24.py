notas = [int(n) for n in input("Digite as notas").split()]

media_aritimetica = sum(notas)/len(notas)

print(f'A media aritimetica desse conjunto de dados é : {media_aritimetica}')
