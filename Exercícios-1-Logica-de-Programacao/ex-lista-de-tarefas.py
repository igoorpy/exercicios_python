# lista de tarefas vazia
tarefas = []

# while para o programa continuar rodando atémandar parar
while True:
    print("\n--- SUA LISTA DE TAREFAS ---")
    
    # Mostra  as tarefas que estão na lista
    print(tarefas)
    
    opcao = input("\nEscolha: (1) Adicionar, (2) Remover, (3) Sair: ")

    if opcao == "1":
        # Pego o texto e uso .append() para colocar no final da lista
        item = input("Digite a nova tarefa: ")
        tarefas.append(item)
        print("Tarefa adicionada!")

    elif opcao == "2":
        # .remove() tirar um item da lista pelo nome
        item = input("Digite o nome exato da tarefa para apagar: ")
        if item in tarefas:
            tarefas.remove(item)
            print("Tarefa removida!")
        else:
            print("Essa tarefa não está na lista!")

    elif opcao == "3":
        print("Saindo do programa...")
        break

    else:
        print("Opção inválida, tente de novo!")