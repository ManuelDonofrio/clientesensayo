import json

class Cliente:
    def __init__(self, nombre, direccion, localidad, abono):
        self.nombre = nombre
        self.direccion = direccion
        self.localidad = localidad
        self.abono = int(abono)
        self.saldo = self.abono
        print(f"Cliente creado: {self.nombre}, Saldo inicial: {self.saldo}") #DEBUG

ruta_archivo = "C:\\Users\\donof\\OneDrive\\Escritorio\\Programación\\Programación\\Clientes Ensayo Teson\\data_clientes.json"

with open(ruta_archivo) as file:
    data_clientes = json.load(file)


clientes = [Cliente(nombre=cliente["cliente"], direccion=cliente["direccion"], localidad=cliente["localidad"], abono=cliente["abono"]) for cliente in data_clientes["Clientes"]]

for cliente in clientes:
    print("Nombre:", cliente.nombre)
    print("Dirección:", cliente.direccion)
    print("Localidad:", cliente.localidad)
    print("Abono:", cliente.abono)
    print("Saldo:", cliente.saldo)
    print("----------------------")