import tkinter as tk
from tkinter import ttk
from tkinter import messagebox


import tkinter as tk
from tkinter import ttk

class ClientesEnsayoInterfaz:
    def __init__(self, programa):
        self.programa = programa
        self.ventana = tk.Tk()
        self.ventana.title("Clientes Ensayo")
        self.ventana.geometry("800x800")

        #Configurar las columnas y filas para que se expandan
        self.ventana.columnconfigure(0, weight=1)
        self.ventana.columnconfigure(1, weight=1)
        self.ventana.columnconfigure(2, weight=1)
        self.ventana.rowconfigure(0, weight=1)
        self.ventana.rowconfigure(1, weight=1)
        self.ventana.rowconfigure(2, weight=1)

        #ComboBox para mostrar los nombres de los clientes
        self.etiqueta_cliente = ttk.Label(self.ventana, text="Cliente:")
        self.etiqueta_cliente.grid(row=0, column=0, padx=10, pady=10, sticky="e")
        self.combobox_clientes = ttk.Combobox(self.ventana, values=[cliente.nombre for cliente in programa.clientes], width=20)
        self.combobox_clientes.grid(row=0, column=1, padx=10, pady=10, sticky="w")

        #Campo de entrada para el monto del pago
        self.etiqueta_monto = ttk.Label(self.ventana, text="Importe:")
        self.etiqueta_monto.grid(row=1, column=0, padx=10, pady=10, sticky="e")
        self.monto_var = tk.StringVar()
        self.entry_monto = ttk.Entry(self.ventana, textvariable=self.monto_var, width=20)
        self.entry_monto.grid(row=1, column=1, padx=10, pady=10, sticky="w")

        #Botón para cargar el pago
        self.boton_cargar_pago = ttk.Button(self.ventana, text="Cargar Pago", command=self.cargar_pago, width=20)
        self.boton_cargar_pago.grid(row=1, column=2, pady=10, sticky="w")

        #Botón para ver la información del cliente
        self.boton_ver_info = ttk.Button(self.ventana, text="Ver Info", command=self.ver_info, width=40)
        self.boton_ver_info.grid(row=2, column=0, columnspan=3, pady=10, sticky="ew")
      
    def cargar_pago(self):
        nombre_cliente = self.combobox_clientes.get()
        monto = float(self.obtener_monto())
        resultado = self.programa.cargar_pago(nombre_cliente, monto)

        if resultado == "success":
            mensaje = f"Se ha cargado un pago de {monto} para {nombre_cliente}. Saldo actualizado: {self.programa.obtener_saldo(nombre_cliente)}"
            messagebox.showinfo("Pago Cargado", mensaje)
        else:
            messagebox.showerror("Error", f"No se encontró al cliente {nombre_cliente}.")

    def ver_info(self):
        nombre_cliente = self.combobox_clientes.get()
        info = self.programa.obtener_info_cliente(nombre_cliente)
        messagebox.showinfo("Información del Cliente: ", info)

    def obtener_monto(self):
        return float(self.monto_var.get()) if self.monto_var.get() else 0

    def mostrar_info(self, info):
        tk.messagebox.showinfo("Información del Cliente: ", info)
