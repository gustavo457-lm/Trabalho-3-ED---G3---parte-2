import re

class Node:
    def __init__(self, item):
        self.nome = item
        self.prox = None
    def __str__(self):
        return self.nome

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

    def listar(self, outra):
        aux = self.tail
        auxOutra = outra.tail
#imprime as pessoas da fila, respeitando a ordem do 2Sem1Com utilizando do match e o while
        match contador:
            case 0:
                if aux is not None:
                    print(f"<- {aux.nome}", end=' ')
                    aux = aux.prox
                if aux is not None:
                    print(f"<- {aux.nome}", end=' ')
                    aux = aux.prox
                if auxOutra is not None:
                    print(f"<- {auxOutra.nome}", end=' ')
                    auxOutra = auxOutra.prox

            case 1:
                if aux is not None:
                    print(f"<- {aux.nome}", end=' ')
                    aux = aux.prox
                if auxOutra is not None:
                    print(f"<- {auxOutra.nome}", end=' ')
                    auxOutra = auxOutra.prox

            case 2:
                if auxOutra is not None:
                    print(f"<- {auxOutra.nome}", end=' ')
                    auxOutra = auxOutra.prox

        while aux is not None or auxOutra is not None:
            if aux is not None:
                print(f"<- {aux.nome}", end=' ')
                aux = aux.prox
            if aux is not None:
                print(f"<- {aux.nome}", end=' ')
                aux = aux.prox
            if auxOutra is not None:
                print(f"<- {auxOutra.nome}", end=' ')
                auxOutra = auxOutra.prox


    def atender(self):
        print(f"Atendido: {self.tail}")
        self.tail = self.tail.prox


# As pessoas sem e com prioridade ficam em filas diferentes
filaNormal = fila()
filaPrioridade = fila()

# Quando o contador estiver em 2 ou mais, o programa irá tentar atender uma pessoa com prioridade
contador = 0

#Contagem de pessoas atendidas
quant_atendidos = 0
quant_com_prioridade = 0


listaFila = input("Digite a fila: ")
listaFila = listaFila.lower()
pessoas = re.split(r'[.,;:!? \s]', listaFila)
for pessoa in pessoas:
    if pessoa != "":
        if pessoa[0] == '*':
            filaPrioridade.adicionar(pessoa)
        else:
            filaNormal.adicionar(pessoa)
print("="*40)
print(pessoas)

while True:
    try:
        print("="*40)
        print("1. Adicionar pessoa na fila")
        print("2. Atender pessoa")
        print("3. Listar todas as pessoas")
        print("4. Sair")
        print("Escolha: ")
        opcao = int(input())
        print("="*40)
        if opcao == 1:

            try:
                nome = input("Nome: ")
            
                if nome[0] == "*":
                    filaPrioridade.adicionar(nome)
                    print(f"{nome} foi adicionado à fila")
                else:
                    filaNormal.adicionar(nome)
                    print(f"{nome} foi adicionado à fila")
            except ValueError:
                print("Opcao invalida!")

        elif opcao == 2:

            #Verifica se ainda há alguém nas filas
            if filaPrioridade.isEmpty() and filaNormal.isEmpty():
                print("Não há ninguém na fila")
            else:

                #Verifica qual fila deve ser atendida, de acordo com o contador e com a presença de pessoas nas filas
                if not filaNormal.isEmpty() and (contador < 2 or filaPrioridade.isEmpty()):
                    filaNormal.atender()
                    quant_atendidos += 1
                    contador += 1

                else:
                    filaPrioridade.atender()
                    quant_atendidos +=1
                    quant_com_prioridade += 1
                    contador = 0


        elif opcao == 3:

            if filaNormal.isEmpty() and filaPrioridade.isEmpty():

                print("Não há ninguém na fila")
            else:
                filaNormal.listar(filaPrioridade)
        
                print("")

        elif opcao == 4:

            #Só é possível fechar o menu de atendimento se as filas estiverem vazias
            if filaNormal.isEmpty() and filaPrioridade.isEmpty():
                break
            else:
                print("Ainda há pessoas na fila")

        else:
            print("Opcao invalida!")
    except ValueError:
        print("Opcao invalida!")

print(f"Quantidade de atendimentos: {quant_atendidos}\nQuantidade de atendimentos com prioridade: {quant_com_prioridade}")
try:
    print(f"Porcentagem de atendimentos com prioridade: {quant_com_prioridade / quant_atendidos * 100: .1f} %")
except ZeroDivisionError:
    print("Não houve atendimentos!")


