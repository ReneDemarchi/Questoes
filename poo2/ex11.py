numero_1 = int(input('Qual o numero 1 '))
numero_2 = int(input('Qual o numero 2 '))
if numero_1 < numero_2:
    for i in range(numero_1+1,numero_2,1):
        print(i)
else:
    for i in range(numero_2+1,numero_1,1):
        print(i)
print(f"a soma dos dois numeros é {numero_2 + numero_1}")