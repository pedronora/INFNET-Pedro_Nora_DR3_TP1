class MinHeap:
    def __init__(self):
        self.heap = []

    def _heapify(self, indice, tamanho):
        """Ajusta o heap para manter a propriedade do heap mínimo"""
        menor = indice
        esq = 2 * indice + 1
        dir = 2 * indice + 2

        if esq < tamanho and self.heap[esq][1] < self.heap[menor][1]:
            menor = esq
        if dir < tamanho and self.heap[dir][1] < self.heap[menor][1]:
            menor = dir

        if menor != indice:
            self.heap[indice], self.heap[menor] = self.heap[menor], self.heap[indice]
            self._heapify(menor, tamanho)

    def inserir(self, nome, prioridade):
        """Insere um novo elemento na fila de prioridade"""
        self.heap.append((nome, prioridade))
        indice = len(self.heap) - 1

        while indice > 0:
            pai = (indice - 1) // 2
            if self.heap[indice][1] < self.heap[pai][1]:
                self.heap[indice], self.heap[pai] = self.heap[pai], self.heap[indice]
                indice = pai
            else:
                break

    def remover(self):
        """Remove o item de menor prioridade da fila"""
        if len(self.heap) == 0:
            return None
        if len(self.heap) == 1:
            return self.heap.pop()

        raiz = self.heap[0]
        self.heap[0] = self.heap.pop()

        self._heapify(0, len(self.heap))

        return raiz

    def esta_vazia(self):
        """Verifica se a fila de prioridade está vazia"""
        return len(self.heap) == 0

    def ordenar(self):
        """Ordena todos os elementos da fila de prioridade e atualiza a Heap"""
        resultado = []
        while not self.esta_vazia():
            resultado.append(self.remover())

        self.heap = resultado
        return self.heap

    def exibir_prioridade_minima(self):
        return self.heap[0]

    def __str__(self):
        return str(self.heap)


if __name__ == "__main__":
    dados = {
        "Maria": 15,
        "Ademar": 5,
        "Gabriela": 20,
        "Fernanda": 18,
        "Luigi": 1,
        "João": 7,
    }

    min_heap = MinHeap()
    print("Inserindo dados na MinHeap:")

    for k, v in dados.items():
        print(f"Prioridade: {v} - {k}")
        min_heap.inserir(k, v)

    print("\nMinHeap após a inserção de todos os valores.")
    print(min_heap)

    print("\nRaiz após inserção de todos os dados:")
    print(min_heap.exibir_prioridade_minima())

    print("\nRaiz após 1ª remoção:")
    min_heap.remover()
    print(min_heap.exibir_prioridade_minima())

    print("\nRaiz após 2ª remoção:")
    min_heap.remover()
    print(min_heap.exibir_prioridade_minima())

    print("\nRaiz após 3ª remoção:")
    min_heap.remover()
    print(min_heap.exibir_prioridade_minima())

    print("\nDados restantes ordenados: ")
    print(min_heap.ordenar())
