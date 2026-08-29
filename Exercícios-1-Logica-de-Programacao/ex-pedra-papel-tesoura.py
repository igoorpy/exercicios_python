import random

opcoes = ["pedra", "papel", "tesoura"]

jogador = input("Escolha pedra, papel ou tesoura: ").strip().lower()
computador = random.choice(opcoes)

print(f"\nVocê escolheu: {jogador}")
print(f"O computador escolheu: {computador}\n")


if jogador not in opcoes:
    print("Opção inválida! Escolha entre pedra, papel ou tesoura.")

elif jogador == computador:
    print("Resultado: Empate!")


elif jogador == "pedra" and computador == "tesoura":
    print("Resultado: Você venceu! (Pedra quebra Tesoura)")

elif jogador == "papel" and computador == "pedra":
    print("Resultado: Você venceu! (Papel cobre Pedra)")

elif jogador == "tesoura" and computador == "papel":
    print("Resultado: Você venceu! (Tesoura corta Papel)")

else:
    print("Resultado: Você perdeu!")