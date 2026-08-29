import random

opcoes = ["pedra", "papel", "tesoura"]

vitorias_jogador = 0
vitorias_computador = 0
empates = 0

print("BEM-VINDO AO JOGO PEDRA, PAPEL E TESOURA")
print("Digite 'sair' a qualquer momento para encerrar o jogo.\n")

while True:
    jogador = input("Escolha pedra, papel, tesoura (ou 'sair'): ").strip().lower()

    if jogador == "sair":
        print("\nObrigado por jogar!")
        break

    if jogador not in opcoes:
        print("Opção inválida! Tente novamente.\n")
        continue  

    computador = random.choice(opcoes)
    print(f"\nVocê: {jogador.capitalize()}\nComputador: {computador.capitalize()}")

    
    if jogador == computador:
        print("Resultado: Empate!")
        empates += 1

    elif (jogador == "pedra" and computador == "tesoura") or \
         (jogador == "papel" and computador == "pedra") or \
         (jogador == "tesoura" and computador == "papel"):
        print("Resultado: Você venceu a rodada!")
        vitorias_jogador += 1

    else:
        print("Resultado: O computador venceu a rodada!")
        vitorias_computador += 1

    print(f"PLACAR: [Você {vitorias_jogador} x {vitorias_computador} Computador\n Empates: {empates}]\n")


print("\n" + "="*30)
print("          PLACAR FINAL          ")
print("="*30)
print(f"Suas Vitórias:      {vitorias_jogador}")
print(f"Vitórias Computador: {vitorias_computador}")
print(f"Empates:             {empates}")
print("="*30)