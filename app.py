from network import Network
from objects.STDatabase import STDatabase

# print("Informações de rede")
# ssid = input("Digite o SSID:: ")
# password = input("Digite a senha:: ")

network = Network()
# network.hack("ANDERSONBORGES_0408")
# network.list()
# network.connect("Jorge Henrique", "")


db = STDatabase().createTable('client')
