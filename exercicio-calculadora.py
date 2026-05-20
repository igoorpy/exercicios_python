while True:
    numero1 = input('Digite o primeiro numero: ')
    numero2 = input('Digite o segundo numero: ')
    operadores = input('Digite um operador (+-/*): ')

    numeros_validos = None

    try:
        num_1 = float(numero1)
        num_2 = float(numero2)
        numeros_validos = True

    except:
        numeros_validos = None

    if numeros_validos is None:
        print('Digite apenas numeros!') 
        continue 
    
    operadores_validos = '+-/*'

    if operadores not in operadores_validos:
        print('Digite apenas operadores validos (+-/*)!')
        continue 

    if len(operadores) < 1:
        print('Digite apenas um operador')
        continue

    print('Realizando sua conta confira o valor abaixo.')

    break


