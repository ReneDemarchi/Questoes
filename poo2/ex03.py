nome = input('Qual o seu nome  =')
if len(nome) > 3:
    print('nome invalido')
idade = input('qual sua idade  =')
try:
    idade = int(idade)
    if idade >=0 and idade <= 150:
        print('idade valida')
except:
    print('Idade invalida')
salario = input('qual o seu salario  =')
try:
    salario = float(salario)
    if salario > 0:
        print('salario valido')
except:
    print('Salario invalido  =')
sexo = input('qual o seu sexo  =')
if sexo == 'f' or sexo == 'm':
    print('Sexo valido')
else:
    print('Sexo invalido')
estado_civil = input('qual o estado civil  =')
if estado_civil == 's' or estado_civil == 'c' or estado_civil == 'v' or estado_civil == 'd':
    print('estado civil valido')