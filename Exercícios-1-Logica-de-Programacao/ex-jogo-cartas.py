import random

# Tuplas para guardar naipes e valores (dados que não mudam)
naipes = ("Copas", "Ouros", "Espadas", "Paus")
valores = ("Ás", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Valete", "Dama", "Rei")

# Dicionário guarda a chave e o valor de uma única carta
carta = {
    "valor": random.choice(valores),
    "naipe": random.choice(naipes)
}

# Mostra no terminal o resultado do sorteio
print("=== CARTA SORTEADA ===")
print(f"Valor: {carta['valor']}")
print(f"Naipe: {carta['naipe']}")