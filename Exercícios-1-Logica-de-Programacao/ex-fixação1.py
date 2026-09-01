senha_correta = 'igor123'
nome = input('Qual o seu nome?: ')
tentativas = 0 

while tentativas < 3:
    senha = input('Informe a sua senha: ')

    if not senha.strip():
        print("Você não digitou nada! Digite uma senha válida.")
        continue 

    if senha == senha_correta:
        print(f"Bem vindo {nome}, acesso liberado!")
        break  
    else:
        print("Acesso negado! Tente novamente.")
        tentativas += 1

if tentativas == 3:
    print('Acesso Bloqueado!')