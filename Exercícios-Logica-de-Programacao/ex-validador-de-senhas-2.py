# while - if/else

senha_validador = "python123"
nome = input("Qual o seu nome?: ")

tentativas = 0

while tentativas < 3:
    senha1 = input("Informe a sua senha: ")

    if senha1 == senha_validador:
        print(f"Seja Bem-vindo, {nome}!")
        break  

    else:
        print("Senha incorreta! Tente novamente")
        tentativas = tentativas + 1 

if tentativas == 3:
    print("Acesso bloqueado! Número máximo de tentativas excedido.")