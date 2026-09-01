nome = input("Qual o seu nome?: ")
idade_tx = input("Digite a sua idade?: ")

idade = int(idade_tx)
ano_nascimento = 2026 - idade

print(f"OLa, {nome}! Voce nasceu em {ano_nascimento}") 

if idade <= 18:
    print("Voce é maior de idade, pode entrar!")
else:
    print("Acesso liberado apenas para maiores.")