from utils.helper import format_float_str_moeda
from models.cliente import Cliente


class Conta:

    codigo = 1001

    def __init__(self, cliente):
        self.__numero = Conta.codigo
        self.__cliente = cliente
        self.__saldo = 0.0
        self.__limite = 100.0
        self.__saldo_total = self._calcula_saldo_total
        Conta.codigo += 1


    @property
    def numero(self):
        return self.__numero

    @property
    def cliemte(self):
        return self.__cliente

    @property
    def saldo(self):
        return self.__saldo

    @saldo.setter
    def saldo(self, valor):
        self.__saldo = valor

    @property
    def limite(self):
        return self.__limite

    @limite.setter
    def limite(self, valor):
        self.__limite = valor

    @property
    def saldo_total(self):
        return self.__saldo_total

    @saldo_total.setter
    def saldo_total(self, valor):
        self.__saldo_total = valor

    @property
    def _calcula_saldo_total(self):
        return self.saldo + self.limite

    def depositar(self, valor):
        if valor > 0:
            self.saldo = self.saldo + valor
            self.saldo_total = self._calcula_saldo_total
            print('Depósito efetuado com sucesso.')
        else:
            print('Erro ao efetuar depósito. Tente novamente.')

    def sacar(self, valor):
        if 0 < valor <= self.saldo_total:
            if valor < self.saldo:
                self.saldo = self.saldo - valor
                self.saldo_total = self._calcula_saldo_total
                print('Saque efetuado com sucesso')
            else:
                restante = saldo-valor
                self.limite = self.limite+restante
                self.saldo = 0
                self.saldo_total = self._calcula_saldo_total
                print('Saque efetuado com sucesso')
        else:
            print('Saque não realizado. Tente novamente')

    def transferir(self, destino, valor):
        if 0 < valor <= self.saldo_total:
            if valor < self.saldo:
                self.saldo = self.saldo - valor
                self.saldo_total = self._calcula_saldo_total
                destino.saldo = destino.saldo + valor
                destino.saldo_total = destino._calcula_saldo_total
                print('Transferência efetuada com sucesso')
            else:
                restante = saldo - valor
                self.limite = self.limite + restante
                self.saldo = 0
                self.saldo_total = self._calcula_saldo_total
                destino.saldo = destino.saldo + valor
                destino.saldo_total = destino._calcula_saldo_total
                print('Transferência efetuada com sucesso')
        else:
            print('Transferência não realizado. Tente novamente')

    def __str__(self):
        return f'Número da conta: {self.numero}\n' \
               f'Cliente: {self.cliemte}\n' \
               f'Saldo: {self.saldo}\n' \
               f'Limite: {self.limite}\n' \
               f'Saldo Total: {self.saldo_total}'