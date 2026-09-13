import re
from FilaComPrioridade import fila

#Separa uma parte do programa de outra para mante-lo organizado visualmente
def separaTexto():
    print("="*115)

#Imprimi o menu das funcionalidades da fila
def menu():
    separaTexto()
    print("1. Adicionar pessoa na fila")
    print("2. Atender pessoa")
    print("3. Listar todas as pessoas")
    print("4. Sair")
    print("Escolha: ")

def main():
    # As pessoas sem e com prioridade ficam em filas diferentes
    filaNormal = fila()
    filaPrioridade = fila()

    # Quando o contador estiver em 2 ou mais, o programa irá tentar atender uma pessoa com prioridade
    contador = 0

    #Contagem de pessoas atendidas
    quant_atendidos = 0
    quant_com_prioridade = 0

    #Separa a entrada de dados de uma linha e insere os nomes nas fila 
    separaTexto()
    print(f"{'FILA COM PRIORIDADES':^115}")
    separaTexto()
    print("Observação: Para adicionar uma pessoa que tenha " \
            "prioridade na fila coloque '*' enfrete ao seu nome")
    separaTexto()
    listaFila = input("Digite a fila inicial: ")
    pessoas = re.split(r'[.,;:!? \s]', listaFila)
    for pessoa in pessoas:
        if pessoa != "":
            if pessoa[0] == '*':
                filaPrioridade.adicionar(pessoa)
            else:
                filaNormal.adicionar(pessoa)

    while True:
        try:
            menu()
            opcao = int(input())
            separaTexto()

            if opcao == 1:
                try:

                    print("Observação: Para adicionar uma pessoa que tenha " \
                    "prioridade na fila coloque '*' enfrete ao seu nome")
                    separaTexto()
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
                    filaNormal.listar(filaPrioridade, contador)
            
                    print("")

            elif opcao == 4:

                #Só é possível fechar o menu de atendimento se as filas estiverem vazias
                if filaNormal.isEmpty() and filaPrioridade.isEmpty():
                    break
                else:
                    print("Ainda há pessoas na fila. A fila só pode ser encerrada quando a fila terminar")

            else:
                print("Opcao invalida!")
        except ValueError:
            print("Opcao invalida!")

    print(f"Quantidade de atendimentos: {quant_atendidos}\nQuantidade de atendimentos com prioridade: {quant_com_prioridade}")

    try:
        print(f"Porcentagem de atendimentos com prioridade: {quant_com_prioridade / quant_atendidos * 100: .1f} %")
    except ZeroDivisionError:
        print("Não houve atendimentos!")

    print("Fila encerrada")
    separaTexto()

main()