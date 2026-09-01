frase = input("Digite uma palavra: ")

frase_minuscula = frase.lower() # letra minuscula

total_vogais = 0
total_consoantes = 0

vogais_encontradas = []

vogais = "aeiou"

for caractere in frase_minuscula:
    if caractere.isalpha(): #retorna True se for uma letra
        if caractere in vogais:
            total_vogais = total_vogais + 1  
            vogais_encontradas.append(caractere)  # Adiciona a vogal
        else:
            total_consoantes = total_consoantes + 1

print(f"\nA sua frase tem {total_vogais} vogais.")
print(f"As vogais encontradas foram: {vogais_encontradas}")
print(f"A sua frase tem {total_consoantes} consoantes.")