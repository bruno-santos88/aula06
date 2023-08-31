# Função para listar tarefas
def listar_tarefas(tarefas):
    print("\nSua lista de tarefas:")
    for tarefa in tarefas:
        estado = "completa" if tarefa["completa"] else "incompleta"
        print(f"ID: {tarefa['id']}, Descrição: {tarefa['descricao']}, Estado: {estado}")

# Classe, Métodos e Atributos
class GerenciadorTarefas:
    def __init__(self, usuario, tarefas_iniciais):
        self.usuario = usuario
        self.tarefas = tarefas_iniciais
        self.tarefa_id = len(tarefas_iniciais)
    
    def adicionar_tarefa(self, descricao):
        self.tarefa_id += 1
        self.tarefas.append({"id": self.tarefa_id, "descricao": descricao, "completa": False})
    
    def completar_tarefa(self, id_tarefa):
        for tarefa in self.tarefas:
            if tarefa['id'] == id_tarefa:
                tarefa['completa'] = True
                return "Tarefa completada!"
        return "Tarefa não encontrada!"
