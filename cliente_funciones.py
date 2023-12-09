from cliente import Cliente

class ClientesEnsayo:
    def __init__(self):
        self.clientes = []

    def agregar_cliente(self, nombre, direccion, localidad, abono):
        """
            Agrega clientes a la lista ya existente.
        """
        cliente = Cliente(nombre, direccion, localidad, abono)
        self.clientes.append(cliente)

    def cargar_pago(self, nombre_cliente, monto):
        """
            Carga el pago ingresado.
            Debug para ver el saldo antes y después del pago.
        """
        for cliente in self.clientes:
            if cliente.nombre == nombre_cliente:
                print(f"Saldo antes del pago para {nombre_cliente}: {cliente.saldo}") #DEBUG
                cliente.saldo -= monto
                print(f"Saldo después del pago para {nombre_cliente}: {cliente.saldo}") #DEBUG
                return "success"
        return "error"

    def obtener_saldo(self, nombre_cliente):
        """
            Obtiene el saldo de cada cliente.
        
        """
        for cliente in self.clientes:
            if cliente.nombre == nombre_cliente:
                return cliente.saldo
        return None
    
    def obtener_info_cliente(self, nombre_cliente):
        """
            Obtiene la información de cada cliente.
        """
        for cliente in self.clientes:
            if cliente.nombre == nombre_cliente:
                #abono_formateado = "{:.3f}".format(cliente.abono)
                info = f"Cliente: {cliente.nombre}\nDirección: {cliente.direccion}\nLocalidad: {cliente.localidad}\nAbono: $ {cliente.abono}"
                return info
        return f"No se encontró al cliente {nombre_cliente}."