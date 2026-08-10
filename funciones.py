import tkinter as tk
from tkinter import messagebox


class Agenda:
    def __init__(self):
        self.contactos = "contactos.txt"

    def añadir_contacto(self):
        nombre = input("Ingrese el nombre del contacto: ")
        telefono = input("Ingrese el número de teléfono del contacto: ")
        correo = input("Ingrese el correo electrónico del contacto: ")
        existe_nombre = False

        if not nombre or not telefono or not correo:
            print("Error: Todos los campos son obligatorios.")

        elif not telefono.isdigit() or len(telefono) != 9:
            print("Error: El teléfono debe contener 9 dígitos.")

        elif "@" not in correo or "." not in correo:
            print("Error: El correo no es válido.")

        else:
            with open(self.contactos, "r", encoding="utf-8") as archivo:
                contactos = archivo.readlines()
                for contacto in contactos:
                    nombre_existente, telefono, correo = contacto.strip().split(",")
                    if nombre_existente == nombre:
                        existe_nombre = True
                        break

            if not existe_nombre:
                with open(self.contactos, "a", encoding="utf-8") as archivo:
                    archivo.write(f"{nombre},{telefono},{correo}\n")
                print("Contacto añadido exitosamente.")
            else:
                print("Error: El contacto ya existe en la agenda.")

    """
    def ver_contactos(self):
            try:
                with open(self.contactos, "r") as archivo:
                    contactos = archivo.readlines()
                    if contactos:
                        print("Lista de contactos:")
                        print(
                            "-------------------------------------------------------------"
                        )
                        print("Nombre\t Teléfono\t Correo")
                        print(
                            "-------------------------------------------------------------"
                        )
                        for contacto in contactos:
                            nombre, telefono, correo = contacto.strip().split(",")
                            print(f"{nombre}\t {telefono}\t {correo}\n")
                    else:
                        print("No hay contactos en la agenda.\n")
            except FileNotFoundError:
                print("No se encontró el archivo de contactos.")
    """

    def ver_contactos(self):
        try:
            with open(self.contactos, "r", encoding="utf-8") as archivo:
                contactos = archivo.readlines()

            ventana_contactos = tk.Toplevel()
            ventana_contactos.title("Contactos")
            ventana_contactos.geometry("600x400")

            if contactos:
                for contacto in contactos:
                    nombre, telefono, correo = contacto.strip().split(",")

                    texto = f"{nombre}    {telefono}    {correo}"

                    tk.Label(ventana_contactos, text=texto, font=("Arial", 12)).pack(
                        pady=5
                    )

            else:
                tk.Label(ventana_contactos, text="No hay contactos en la agenda.").pack(
                    pady=20
                )

        except FileNotFoundError:
            messagebox.showerror("Error", "No se encontró el archivo de contactos.")

    def eliminar_contacto(self):
        nombre_eliminar = input("Ingrese el nombre del contacto a eliminar: ")
        try:
            with open(self.contactos, "r") as archivo:
                contactos = archivo.readlines()

            with open(self.contactos, "w") as archivo:
                encontrado = False
                for contacto in contactos:
                    nombre, telefono, correo = contacto.strip().split(",")
                    if nombre != nombre_eliminar:
                        archivo.write(contacto)
                    else:
                        encontrado = True

            if encontrado:
                print("Contacto eliminado exitosamente.\n")
            else:
                print("No se encontró el contacto especificado.")
        except FileNotFoundError:
            print("No se encontró el archivo de contactos.")

    def buscar_contacto(self):
        nombre_buscar = input("Ingrese el nombre del contacto a buscar: ")
        try:
            with open(self.contactos, "r") as archivo:
                contacto = archivo.readlines()
                encontrado = False
                for c in contacto:
                    nombre, telefono, correo = c.strip().split(",")
                    if nombre == nombre_buscar:
                        if not encontrado:
                            print("Contacto(s) encontrado(s)")
                            print(
                                "-------------------------------------------------------------"
                            )
                            print("Nombre\t Teléfono\t Correo")
                            print(
                                "-------------------------------------------------------------"
                            )
                        encontrado = True
                        print(f"{nombre}\t {telefono}\t {correo}\n")
                if not encontrado:
                    print("El contacto no se encuentra en la agenda.\n")
        except FileNotFoundError:
            print("No se encontró el archivo de contactos.")
