import tkinter as tk
from tkinter import messagebox

from funciones import Agenda

agenda = Agenda()


def ventana_añadir():

    ventana_añadir = tk.Toplevel()
    ventana_añadir.title("Añadir contacto")
    ventana_añadir.geometry("400x300")

    tk.Label(ventana_añadir, text="Nombre:").pack(pady=5)

    entrada_nombre = tk.Entry(ventana_añadir)
    entrada_nombre.pack(pady=5)

    tk.Label(ventana_añadir, text="Teléfono:").pack(pady=5)

    entrada_telefono = tk.Entry(ventana_añadir)
    entrada_telefono.pack(pady=5)

    tk.Label(ventana_añadir, text="Correo:").pack(pady=5)

    entrada_correo = tk.Entry(ventana_añadir)
    entrada_correo.pack(pady=5)

    def boton_guardar():
        nombre = entrada_nombre.get()
        telefono = entrada_telefono.get()
        correo = entrada_correo.get()

        correcto, mensaje = agenda.añadir_contacto(nombre, telefono, correo)

        if correcto:
            messagebox.showinfo("Éxito", mensaje)
            ventana_añadir.destroy()
        else:
            messagebox.showerror("Error", mensaje)

    tk.Button(ventana_añadir, text="Guardar", command=boton_guardar).pack(pady=20)


def ventana_eliminar():
    ventana_eliminar = tk.Toplevel()
    ventana_eliminar.title("Eliminar contacto")
    ventana_eliminar.geometry("400x200")

    tk.Label(ventana_eliminar, text="Nombre del contacto a eliminar:").pack(pady=5)

    entrada_nombre = tk.Entry(ventana_eliminar)
    entrada_nombre.pack(pady=5)

    tk.Label(ventana_eliminar, text="Teléfono del contacto a eliminar:").pack(pady=5)

    entrada_telefono = tk.Entry(ventana_eliminar)
    entrada_telefono.pack(pady=5)

    def boton_eliminar():
        nombre = entrada_nombre.get()
        telefono = entrada_telefono.get()

        correcto, mensaje = agenda.eliminar_contacto(nombre, telefono)

        if correcto:
            messagebox.showinfo("Éxito", mensaje)
            ventana_eliminar.destroy()
        else:
            messagebox.showerror("Error", mensaje)

    tk.Button(ventana_eliminar, text="Eliminar", command=boton_eliminar).pack(pady=20)
