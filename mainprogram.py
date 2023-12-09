from cliente_funciones import ClientesEnsayo
from interfaz import ClientesEnsayoInterfaz
import json

def cargar_clientes_desde_json(ruta_archivo):
    try:
        with open(ruta_archivo) as file:
            data_clientes = json.load(file)
        return data_clientes.get("Clientes", [])
    except FileNotFoundError:
        print(f"Error: No se encontró el archivo {ruta_archivo}")
        return []

def main():
    ruta_archivo = "C:\\Users\\donof\\OneDrive\\Escritorio\\Programación\\Programación\\Clientes Ensayo Teson\\data_clientes.json"
    
    clientes_info = cargar_clientes_desde_json(ruta_archivo)
    
    if not clientes_info:
        print("No se pudieron cargar clientes. Saliendo.")
        return
    
    programa = ClientesEnsayo()

    #Agregar clientes 
    for cliente_info in clientes_info:
        programa.agregar_cliente(
            nombre=cliente_info.get("cliente", ""),
            direccion=cliente_info.get("direccion", ""),
            localidad=cliente_info.get("localidad", ""),
            abono=float(cliente_info.get("abono", 0))
        )

    #Crear la interfaz después de agregar clientes
    interfaz = ClientesEnsayoInterfaz(programa)

    #Iniciar la interfaz gráfica
    interfaz.ventana.mainloop()

if __name__ == "__main__":
    main()
