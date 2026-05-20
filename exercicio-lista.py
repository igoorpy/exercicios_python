import os 

lista = []   

while True:
    print('\nSelecione uma opção')
    opcao = input('[i]nserir [a]pagar [l]istar: ').strip().lower()

    if opcao == 'i':
        os.system('cls')
        valor = input('Valor: ')
        lista.append(valor)
        print(f'{valor} adicionado')

    elif opcao == 'a':   
        if not lista:
            print('Lista vazia')
            continue

        print('\n Lista atual:')
        for i, valor in enumerate(lista):
            print(f'  [{i}] {valor}')
        
        indice_str = input('\nEscolha o indice para apagar: ')

        try:
            indice = int(indice_str)
            item_removido = lista[indice]
            del lista[indice]
            print(f' "{item_removido}" removido!')
        except ValueError:
            print(' Digite um numero inteiro')
        except IndexError:
            print(' Indice nao existe na lista')
        except Exception:
            print(' Erro')

    elif opcao == 'l':
        os.system('cls')

        if len(lista) == 0:
            print('Nada para listar')  
        else:
            for i, valor in enumerate(lista):
                print(i, valor)
                
    else:
        print('Opção inválida')