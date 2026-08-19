import tkinter as tk
from tkinter import messagebox
from funciones import Agenda
import botones

agenda = Agenda()

ventana = tk.Tk()
ventana.title("Agenda de contactos")
ventana.geometry("600x500")


titulo = tk.Label(ventana, text="AGENDA DE CONTACTOS 📒", font=("Arial", 15))

titulo.pack(pady=20)

marco_contactos = tk.Frame(ventana)
marco_contactos.pack(pady=20, fill="both", expand=True)

botones.mostrar_contactos(agenda, marco_contactos)

ventana.mainloop()
