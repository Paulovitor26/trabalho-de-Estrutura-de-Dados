tarefas = []

def prioridade_valida(p):
    return p in ["alta", "media", "baixa"]

def cadastrar_tarefa():
    nome = input("Nome da tarefa: ").strip().title()
    prioridade = input("Prioridade (alta, media, baixa): ").strip().lower()
    if not prioridade_valida(prioridade):
        print("Prioridade inválida.\n")
        return
    tarefa = {"nome": nome, "prioridade": prioridade}
    tarefas.append(tarefa)
    print("Tarefa cadastrada!\n")

def listar_tarefas():
    if not tarefas:
        print("Nenhuma tarefa cadastrada.\n")
        return
    print("\nTarefas por prioridade:")
    prioridade_ordem = {"alta": 1, "media": 2, "baixa": 3}
    tarefas_ordenadas = sorted(tarefas, key=lambda x: prioridade_ordem[x["prioridade"]])
    for t in tarefas_ordenadas:
        print(f"- {t['nome']} ({t['prioridade'].capitalize()})")
    print()

def remover_tarefa():
    nome = input("Nome da tarefa a remover: ").strip().title()
    for t in tarefas:
        if t["nome"] == nome:
            tarefas.remove(t)
            print("Tarefa removida.\n")
            return
    print("Tarefa não encontrada.\n")

def menu():
    while True:
        print("1. Cadastrar tarefa")
        print("2. Listar tarefas")
        print("3. Remover tarefa")
        print("4. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            cadastrar_tarefa()
        elif opcao == "2":
            listar_tarefas()
        elif opcao == "3":
            remover_tarefa()
        elif opcao == "4":
            print("Encerrando o programa.")
            break
        else:
            print("Opção inválida.\n")

if __name__ == "__main__":
    menu()