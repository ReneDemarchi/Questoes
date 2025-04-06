numero = int(input('Qual o numero que deseja saber se é primo'))
raiz = numero**(1/2)
primo = True
for i in range(1,int(raiz)):
    if numero%i == 0:
        primo = False
if primo:
    print('é primo')
else:
    print('Esse numero não é primo')
