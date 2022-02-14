from typing import List
from time import sleep

from models.cliente import Cliente
from models.conta import Conta


contas: List[Conta] = []

def main():
    menu()


def menu():
    print('==================================')
    print('==============ATM=================')
    print('===========Geek Bank==============')
    print('==================================')

    print('Selecione uma opção no menu:\n')
    print('1 - Criar conta.')
    print('2 - Efetuar saque.')
    print('3 - Efetuar depósito.')
    print('4 - Efetuar transferência.')
    print('5 - Listar contas.')
    print('6 - Sair do sistema.')

    opcao = int(input())

    if opcao == 1:
        criar_conta()
    elif opcao == 2:
        efetuar_saque()
    elif opcao == 3:
        efetuar_deposito()
    elif opcao == 4:
        efetuar_transferencia()
    elif opcao == 5:
        listar_contas()
    elif opcao == 6:
        print('Volte sempre!')
        sleep(2)
        exit(0)
    else:
        print('Opção inválida!')
        sleep(2)
        menu()




def criar_conta():
    print('Informe os dados do cliente:\n')

    nome = input('Digite o nome do cliente:\n')
    email = input('Digite o email do cliente:\n')
    cpf = input('Digite o cpf do cliente:\n')
    data_nascimento = input('Digite a data de nascimento do cliente:\n')

    cliente = Cliente(nome=nome, email=email, cpf=cpf, data_nascimento=data_nascimento)

    conta = Conta(cliente)

    contas.append(conta)

    print('Conta criada com sucesso!')
    print('Dados da conta.')
    print('-------------------------')
    print(conta)
    sleep(2)
    menu()


def efetuar_saque():
    if len(contas) > 0:

        numero = int(input('Informe o número da sua conta!'))

        conta = buscar_conta_por_numero(numero=numero)

        if conta:
            valor = float(input('Informe o valor do saque!'))
            conta.sacar(valor)
        else:
            print(f'Não foi encontrado a conta com o número {numero}')
    else:
        print('Não existem contas cadastradas!')
    sleep(2)
    menu()


def efetuar_deposito():
    if len(contas) > 0:

        numero = int(input('Informe o número da conta para depósita!'))

        conta = buscar_conta_por_numero(numero=numero)

        if conta:
            valor = float(input('Informe o valor do depósito!'))
            conta.depositar(valor)
        else:
            print(f'Não foi encontrado a conta com o número {numero}')
    else:
        print('Não existem contas cadastradas!')
    sleep(2)
    menu()


def efetuar_transferencia():
    if len(contas) > 0:

        numero = int(input('Informe o número da sua conta!'))

        conta_o = buscar_conta_por_numero(numero=numero)

        if conta_o:
            numero_d = int(input('Informe o número da conta de destino'))

            conta_d = buscar_conta_por_numero(numero=numero_d)

            if conta_d:

                valor = float(input('Informe o valor da transferência!'))
                conta_o.transferir(conta_d, valor)
            else:
                print(f'A conta de destino com o numero {numero_d} não foi encontrada')
        else:
            print(f'Não foi encontrado a conta com o número {numero}')
    else:
        print('Não existem contas cadastradas!')
    sleep(2)
    menu()


def listar_contas():
    if len(contas) > 0:

        print('Listagem de contas:')
        for conta in contas:
            print(conta)
            print('----------------------')
            sleep(1)
    else:
        print('Não existem contas cadastradas!')
    sleep(2)
    menu()


def buscar_conta_por_numero(numero):
    c: Conta = None

    if len(contas) > 0:
        for conta in contas:
            if conta.numero==numero:
                c = conta
    return c


if __name__ == '__main__':
    main()