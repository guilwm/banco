from datetime import date
from utils.helper import str_para_date, date_para_str

#classe cliente

class Cliente:
    contador = 101

    def __init__(self, nome, email, cpf, data_nascimento):
        self.__codigo = Cliente.contador
        self.__nome = nome
        self.__email = email
        self.__cpf = cpf
        self.__data_nascimento = str_para_date(data_nascimento)
        self.__data_cadastro = date.today()
        Cliente.contador += 1

    @property
    def codigo(self):
        return self.__codigo

    @property
    def nome(self):
        return self.__nome

    @property
    def emal(self):
        return self.__email

    @property
    def cpf(self):
        return self.__cpf

    @property
    def data_nascimento(self):
        return date_para_str(self.__data_nascimento)

    @property
    def data_cadastro(self):
        return date_para_str(self.__data_cadastro)

    def __str__(self):
        return f'Código: {self.codigo}\n' \
               f'Nome: {self.nome}\n' \
               f'emal: {self.emal}\n' \
               f'cpf: {self.cpf}\n' \
               f'Data de nascimento: {self.data_nascimento}\n' \
               f'Data de cadastro: {self.data_cadastro}'