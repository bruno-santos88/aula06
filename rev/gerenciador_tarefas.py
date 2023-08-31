from utils import listar_tarefas, GerenciadorTarefas

# Hello World
print("Olá, Mundo! Bem-vindo ao Gerenciador de Tarefas.")

# Função print() e input()
nome_usuario = input("Por favor, digite seu nome: ")
print(f"Olá, {nome_usuario}. Vamos organizar suas tarefas!")

# Tipos de Variáveis e Dicionários
tarefas_iniciais = [
    {"id": 1, "descricao": "Comprar leite", "completa": False}
]

# Criando um objeto da classe GerenciadorTarefas
gerenciador = GerenciadorTarefas(nome_usuario, tarefas_iniciais)

# Loop principal
while True:
    print("\nO que você gostaria de fazer?")
    print("1: Listar tarefas")
    print("2: Adicionar nova tarefa")
    print("3: Completar tarefa")
    print("4: Sair")
    
    escolha = input("Escolha uma opção: ")
    
    if escolha == "1":
        listar_tarefas(gerenciador.tarefas)
    elif escolha == "2":
        nova_tarefa = input("Digite a descrição da nova tarefa: ")
        gerenciador.adicionar_tarefa(nova_tarefa)
        print("Tarefa adicionada com sucesso!")
    elif escolha == "3":
        id_tarefa = int(input("Digite o ID da tarefa que deseja completar: "))
        resultado = gerenciador.completar_tarefa(id_tarefa)
        print(resultado)
    elif escolha == "4":
        print("Obrigado por usar o Gerenciador de Tarefas. Até mais!")
        break
    else:
        print("Opção inválida. Tente novamente.")
