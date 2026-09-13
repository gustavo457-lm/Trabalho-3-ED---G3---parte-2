from Node import Node

class fila():
    def __init__(self):
        self.head = None
        self.tail = None

    def isEmpty(self):
        return self.tail==None

    def adicionar(self, item):
        novo = Node(item)
        if self.head == None or self.tail == None:
            self.tail = novo
            self.head = novo
        else:
            self.head.prox = novo
            self.head = novo

    def listar(self, outra, contador):
        aux = self.tail
        auxOutra = outra.tail
        print("Início ->", end=' ')
#imprime as pessoas da fila, respeitando a ordem do 2Sem1Com utilizando do match e o while
        match contador:
            case 0:
                if aux is not None:
                    print(f"{aux.nome} ->", end=' ')
                    aux = aux.prox
                if aux is not None:
                    print(f"{aux.nome} ->", end=' ')
                    aux = aux.prox
                if auxOutra is not None:
                    print(f"{auxOutra.nome} ->", end=' ')
                    auxOutra = auxOutra.prox

            case 1:
                if aux is not None:
                    print(f"{aux.nome} ->", end=' ')
                    aux = aux.prox
                if auxOutra is not None:
                    print(f"{auxOutra.nome} ->", end=' ')
                    auxOutra = auxOutra.prox

            case 2:
                if auxOutra is not None:
                    print(f"{auxOutra.nome} ->", end=' ')
                    auxOutra = auxOutra.prox

        while aux is not None or auxOutra is not None:
            if aux is not None:
                print(f"{aux.nome} ->", end=' ')
                aux = aux.prox
            if aux is not None:
                print(f"{aux.nome} ->", end=' ')
                aux = aux.prox
            if auxOutra is not None:
                print(f"{auxOutra.nome} ->", end=' ')
                auxOutra = auxOutra.prox
        print("Fim", end=' ')


    def atender(self):
        print(f"Atendido: {self.tail}")
        self.tail = self.tail.prox