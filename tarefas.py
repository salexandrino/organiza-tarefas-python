def mostrar_menu():
    print("\n===== ORGANIZA TAREFAS =====")
    print("1 - Adicionar tarefa")
    print("2 - Listar tarefas")
    print("3 - Concluir tarefa")
    print("4 - Excluir tarefa")
    print("0 - Sair")


def adicionar_tarefa(tarefas, proximo_id):
    titulo = input("Digite o título da tarefa: ").strip()

    if not titulo:
        print("O título não pode ficar vazio.")
        return proximo_id

    tarefa = {
        "id": proximo_id,
        "titulo": titulo,
        "concluida": False
    }

    tarefas.append(tarefa)
    print(f'Tarefa "{titulo}" adicionada!')

    return proximo_id + 1


def listar_tarefas(tarefas):
    if not tarefas:
        print("\nNenhuma tarefa cadastrada.")
        return

    print("\n===== SUAS TAREFAS =====")

    for tarefa in tarefas:
        status = "Concluída" if tarefa["concluida"] else "Pendente"

        print(
            f'{tarefa["id"]} - {tarefa["titulo"]} '
            f'[{status}]'
        )

    concluidas = sum(
        1 for tarefa in tarefas if tarefa["concluida"]
    )

    print(f"\nTotal: {len(tarefas)}")
    print(f"Concluídas: {concluidas}")
    print(f"Pendentes: {len(tarefas) - concluidas}")


def buscar_tarefa(tarefas, id_tarefa):
    for tarefa in tarefas:
        if tarefa["id"] == id_tarefa:
            return tarefa

    return None


def solicitar_id():
    entrada = input("Digite o número da tarefa: ").strip()

    try:
        id_tarefa = int(entrada)
    except ValueError:
        print("Digite um número inteiro válido.")
        return None

    if id_tarefa <= 0:
        print("O número da tarefa deve ser positivo.")
        return None

    return id_tarefa


def concluir_tarefa(tarefas):
    if not tarefas:
        print("Não há tarefas para concluir.")
        return

    listar_tarefas(tarefas)
    id_tarefa = solicitar_id()

    if id_tarefa is None:
        return

    tarefa = buscar_tarefa(tarefas, id_tarefa)

    if tarefa is None:
        print("Tarefa não encontrada.")
    elif tarefa["concluida"]:
        print("Essa tarefa já está concluída.")
    else:
        tarefa["concluida"] = True
        print(f'Tarefa "{tarefa["titulo"]}" concluída!')


def excluir_tarefa(tarefas):
    if not tarefas:
        print("Não há tarefas para excluir.")
        return

    listar_tarefas(tarefas)
    id_tarefa = solicitar_id()

    if id_tarefa is None:
        return

    tarefa = buscar_tarefa(tarefas, id_tarefa)

    if tarefa is None:
        print("Tarefa não encontrada.")
        return

    confirmacao = input(
        f'Excluir "{tarefa["titulo"]}"? (s/n): '
    ).strip().lower()

    if confirmacao == "s":
        tarefas.remove(tarefa)
        print("Tarefa excluída.")
    else:
        print("Exclusão cancelada.")


def main():
    tarefas = []
    proximo_id = 1

    while True:
        mostrar_menu()
        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            proximo_id = adicionar_tarefa(tarefas, proximo_id)
        elif opcao == "2":
            listar_tarefas(tarefas)
        elif opcao == "3":
            concluir_tarefa(tarefas)
        elif opcao == "4":
            excluir_tarefa(tarefas)
        elif opcao == "0":
            print("Programa encerrado. Até mais!")
            break
        else:
            print("Opção inválida. Tente novamente.")


if __name__ == "__main__":
    main()