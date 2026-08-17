import tkinter as tk
from tkinter import messagebox
from pathlib import Path


class Agenda:

    BASE_DIR = Path(__file__).resolve().parent

    ruta_txt = BASE_DIR / "contactos.txt"

    with open(ruta_txt, "r", encoding="utf-8") as f:
        datos = f.read()

    def __init__(self):
        self.contactos = self.ruta_txt

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

    def eliminar_contacto(self, nombre_eliminar, telefono_eliminar):
        lista_contactos = []
        try:
            with open(self.contactos, "r") as archivo:
                contactos = archivo.readlines()

            with open(self.contactos, "w") as archivo:
                encontrado = False
                for contacto in contactos:
                    nombre, telefono, correo = contacto.strip().split(",")
                    if nombre == nombre_eliminar and telefono == telefono_eliminar:
                        encontrado = True
                    else:
                        lista_contactos.append(contacto)
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
                    if nombre.lower() == nombre_buscar.lower():
                        encontrado.append((nombre, telefono, correo))
                return encontrado
        except FileNotFoundError:
            return "No se encontró el archivo de contactos."
