import tkinter as tk
from tkinter import messagebox


class Agenda:
    def __init__(self):
        self.contactos = "contactos.txt"

    def añadir_contacto(self, nombre, telefono, correo):
        existe_nombre = False

        if not nombre or not telefono or not correo:
            return False, "Todos los campos son obligatorios."

        elif not telefono.isdigit() or len(telefono) != 9:
            return False, "El teléfono debe contener 9 dígitos numericos."

        elif "@" not in correo or "." not in correo:
            return False, "El correo no es válido."

        else:
            with open(self.contactos, "r", encoding="utf-8") as archivo:
                contactos = archivo.readlines()
                for contacto in contactos:
                    nombre_existente, telefono_existente, correo_existente = (
                        contacto.strip().split(",")
                    )

                    if (
                        nombre_existente == nombre
                        and telefono_existente == telefono
                        and correo_existente == correo
                    ):
                        existe_nombre = True
                        break

            if existe_nombre:
                return False, "El contacto ya existe en la agenda."

            with open(self.contactos, "a", encoding="utf-8") as archivo:
                archivo.write(f"{nombre},{telefono},{correo}\n")

            return True, "Contacto añadido exitosamente."

    def ver_contactos(self):
        ventana_contactos = tk.Toplevel()
        ventana_contactos.title("Contactos")
        ventana_contactos.geometry("600x400")

        marco = tk.Frame(ventana_contactos)
        marco.pack(pady=10)

        def actualizar():
            # Eliminar los widgets anteriores
            for widget in marco.winfo_children():
                widget.destroy()

            try:
                with open(self.contactos, "r", encoding="utf-8") as archivo:
                    contactos = archivo.readlines()

                if contactos:

                    texto_titulo = (
                        "Lista de contactos\n"
                        "-------------------------------------------------------------\n"
                        "Nombre       Teléfono       Correo\n"
                        "-------------------------------------------------------------"
                    )

                    tk.Label(marco, text=texto_titulo, font=("Arial", 12)).pack(pady=5)

                    for contacto in contactos:
                        nombre, telefono, correo = contacto.strip().split(",")

                        texto = f"{nombre}       {telefono}       {correo}"

                        tk.Label(marco, text=texto, font=("Arial", 12)).pack(pady=5)

                else:
                    tk.Label(
                        marco, text="No hay contactos en la agenda.", font=("Arial", 12)
                    ).pack(pady=20)

            except FileNotFoundError:
                messagebox.showerror("Error", "No se encontró el archivo de contactos.")

        actualizar()

        tk.Button(ventana_contactos, text="Actualizar", command=actualizar).pack(
            pady=10
        )

    def eliminar_contacto(self, nombre_eliminar, telefono_eliminar):
        lista_contactos = []
        try:
            with open(self.contactos, "r") as archivo:
                contactos = archivo.readlines()

            with open(self.contactos, "w") as archivo:
                encontrado = False
                for contacto in contactos:
                    nombre, telefono, correo = contacto.strip().split(",")
                    if nombre != nombre_eliminar and telefono != telefono_eliminar:
                        lista_contactos.append(contacto)
                    else:
                        encontrado = True
                archivo.writelines(lista_contactos)
            if encontrado:
                return True, "Contacto eliminado exitosamente."
            else:
                return False, "El contacto no se encuentra en la agenda."
        except FileNotFoundError:
            messagebox.showerror("Error", "No se encontró el archivo de contactos.")

    def buscar_contacto(self, nombre_buscar):
        try:
            with open(self.contactos, "r") as archivo:
                contacto = archivo.readlines()
                encontrado = []
                for c in contacto:
                    nombre, telefono, correo = c.strip().split(",")
                    if nombre == nombre_buscar:
                        encontrado.append((nombre, telefono, correo))
                return encontrado
        except FileNotFoundError:
            return "No se encontró el archivo de contactos."

    def mostrar_contactos(self):
        try:
            with open(self.contactos, "r") as archivo:
                contactos = archivo.readlines()
                return contactos
        except FileNotFoundError:
            return "No se encontró el archivo de contactos."
