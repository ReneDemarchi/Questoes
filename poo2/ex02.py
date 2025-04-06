login = input('escolha um login')
senha = input('escola uma senha')
if login == senha:
    while True:
        nova_senha = input('Digite outra senha')
        if nova_senha != login:
            senha = nova_senha
            break
        else:
            print('Seu login e senha são iguais')
print(f'seu login é {login} e sua senha é {senha}')