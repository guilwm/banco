from models.cliente import Cliente
from models.conta import Conta


felicity = Cliente('Felicity Jones', 'felicity@gmail.com', '123.456.789-90', '02/09/1987')
angelina = Cliente('Angelina Jolie', 'angelina@gmail.com', '098.765.432-11', '08/07/1978')

# print(felicity)
# print(angelina)

contaf = Conta(felicity)
contaa = Conta(angelina)

print(contaf)
print(contaa)