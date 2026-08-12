import tkinter as tk
from tkinter import messagebox
from funciones import Agenda
import botones

agenda = Agenda()

ventana = tk.Tk()
ventana.title("Agenda de contactos")
ventana.geometry("600x400")
ventana.configure(bg="gray")

titulo = tk.Label(
    ventana, text="Agenda de Contactos", font=("Arial", 20), bg="gray", fg="white"
)

titulo.pack(pady=20)

boton_ver = tk.Button(ventana, text="Contactos", width=20, command=agenda.ver_contactos)

boton_ver.pack(pady=5)

boton_añadir = tk.Button(
    ventana, text="Añadir contacto", width=20, command=botones.ventana_añadir
)

boton_añadir.pack(pady=5)

boton_eliminar = tk.Button(
    ventana, text="Eliminar contacto", width=20, command=botones.ventana_eliminar
)

boton_eliminar.pack(pady=5)

boton_buscar = tk.Button(
    ventana, text="Buscar contacto", width=20, command=botones.ventana_buscar
)

boton_buscar.pack(pady=5)

ventana.mainloop()
