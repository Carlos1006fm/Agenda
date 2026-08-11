import tkinter as tk
from tkinter import messagebox
from funciones import Agenda
import botones

agenda = Agenda()

"""
opcion = ""
while opcion != "5":
    print("1. Añadir contacto")
    print("2. Ver contactos")
    print("3. Eliminar contacto")
    print("4. Buscar contacto")
    print("5. Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        agenda.añadir_contacto()
    elif opcion == "2":
        agenda.ver_contactos()
    elif opcion == "3":
        agenda.eliminar_contacto()
    elif opcion == "4":
        agenda.buscar_contacto()
    elif opcion == "5":
        print("Saliendo de la agenda. ¡Hasta luego!")
"""

ventana = tk.Tk()
ventana.title("Agenda de contactos")
ventana.geometry("600x400")

titulo = tk.Label(ventana, text="Agenda de Contactos", font=("Arial", 20))

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

boton_buscar = tk.Button(ventana, text="Buscar contacto", width=20)

boton_buscar.pack(pady=5)

ventana.mainloop()
