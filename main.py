import tkinter as tk
from tkinter import messagebox
from funciones import Agenda
import botones

agenda = Agenda()

ventana = tk.Tk()
ventana.title("Agenda de contactos")
ventana.geometry("550x500")


titulo = tk.Label(ventana, text="AGENDA DE CONTACTOS 📒", font=("Arial", 15))

titulo.pack(pady=20)

marco_contactos = tk.Frame(ventana)
marco_contactos.pack(pady=20)

boton = tk.Frame(ventana)
boton.pack(pady=20)

boton_añadir = tk.Button(
    boton,
    text="Añadir contacto",
    width=15,
    command=lambda: botones.ventana_añadir(marco_contactos),
).pack(side="left", padx=5)

boton_eliminar = tk.Button(
    boton,
    text="Eliminar contacto",
    width=15,
    command=lambda: botones.ventana_eliminar(marco_contactos),
).pack(side="left", padx=5)

boton_buscar = tk.Button(
    boton, text="Buscar contacto", width=15, command=botones.ventana_buscar
).pack(side="left", padx=5)

botones.mostrar_contactos(agenda, marco_contactos)

ventana.mainloop()
