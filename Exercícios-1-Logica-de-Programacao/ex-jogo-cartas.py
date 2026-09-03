import random

# Dados fixos em tuplas
naipes = ("Copas", "Ouros", "Espadas", "Paus")
valores = ("Ás", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K")

# Conjunto (Set) evita cartas repetidas no sorteio
cartas_retiradas = set()

# Loop principal para manter o jogo rodando
while True:
    opcao = input("\nPressione Enter para tirar carta (ou 'sair'): ").strip().lower()
    
    if opcao == "sair":
        print("Jogo encerrado.")
        break

    # Sorteia um valor e um naipe
    valor = random.choice(valores)
    naipe = random.choice(naipes)
    
    # Identificador para checar o conjunto
    identificador = (valor, naipe)

    # Verifica se a carta já foi sorteada antes
    if identificador in cartas_retiradas:
        print("Carta repetida! Sorteando novamente...")
        continue
    
    # Adiciona a carta nova no conjunto de tiradas
    cartas_retiradas.add(identificador)

    # Dicionário da carta atual
    carta = {
        "valor": valor,
        "naipe": naipe
    }

    # Formatação do texto e desenho da carta no terminal
    v = carta["valor"].ljust(2)
    print("┌─────────┐")
    print(f"│ {v}      │")
    print(f"│ {carta['naipe']:^7} │")
    print(f"│      {v} │")
    print("└─────────┘")
    print(f"Cartas tiradas até agora: {len(cartas_retiradas)}")