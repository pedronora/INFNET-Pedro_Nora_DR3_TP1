class FilaPrioridadeHeap:
    def __init__(self):
        self.heap = []

    def _heapify(self, indice, tamanho):
        """Ajusta o heap para manter a propriedade do heap máximo"""
        maior = indice
        esq = 2 * indice + 1
        dir = 2 * indice + 2

        if esq < tamanho and self.heap[esq][1] > self.heap[maior][1]:
            maior = esq
        if dir < tamanho and self.heap[dir][1] > self.heap[maior][1]:
            maior = dir

        if maior != indice:
            self.heap[indice], self.heap[maior] = self.heap[maior], self.heap[indice]
            self._heapify(maior, tamanho)

    def inserir(self, nome, prioridade):
        """Insere um novo elemento na fila de prioridade"""
        self.heap.append((nome, prioridade))
        indice = len(self.heap) - 1

        while indice > 0:
            pai = (indice - 1) // 2
            if self.heap[indice][1] > self.heap[pai][1]:
                self.heap[indice], self.heap[pai] = self.heap[pai], self.heap[indice]
                indice = pai
            else:
                break

    def remover(self):
        """Remove o item de maior prioridade da fila"""
        if len(self.heap) == 0:
            return None
        if len(self.heap) == 1:
            return self.heap.pop()

        raiz = self.heap[0]
        self.heap[0] = self.heap.pop()

        self._heapify(0, len(self.heap))

        return raiz

    def mostrar_raiz(self):
        print(self.heap[0])

    def esta_vazia(self):
        """Verifica se a fila de prioridade está vazia"""
        return len(self.heap) == 0

    def ordenar(self):
        """Ordena todos os elementos da fila de prioridade"""
        resultado = []
        while not self.esta_vazia():
            resultado.append(self.remover())

        self.heap = resultado
        return resultado

    def __str__(self):
        return str(self.heap)


if __name__ == "__main__":
    dados = {
        "Responder emails urgentes": 1,
        "Agendar reunião com o chefe": 2,
        "Organizar arquivos na pasta compartilhada": 4,
        "Fazer café para a equipe": 8,
        "Trocar o cartucho da impressora": 3,
        "Solicitar material de escritório": 5,
        "Reservar sala de reunião": 6,
        "Atualizar o relatório semanal": 7,
        "Regar as plantas do escritório": 9,
        "Enviar memorando para os funcionários": 10,
    }

    fila_de_prioridade = FilaPrioridadeHeap()

    print("Inserindo dados na Fila de Prioridade\n")
    for tarefa, prioridade in dados.items():
        fila_de_prioridade.inserir(tarefa, prioridade)
    print()

    print("Fila de Prioridade atual:")
    print(fila_de_prioridade)
    print()

    tarefa_finalizada = fila_de_prioridade.remover()
    print(f"Finalizada a tarefa {tarefa_finalizada}")
    print(f"Nova prioridade: ")
    fila_de_prioridade.mostrar_raiz()
    print()

    tarefa_finalizada = fila_de_prioridade.remover()
    print(f"Finalizada a tarefa {tarefa_finalizada}")
    print(f"Nova prioridade: ")
    fila_de_prioridade.mostrar_raiz()
    print()

    tarefa_finalizada = fila_de_prioridade.remover()
    print(f"Finalizada a tarefa {tarefa_finalizada}")
    print(f"Nova prioridade: ")
    fila_de_prioridade.mostrar_raiz()
    print()
