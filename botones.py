import tkinter as tk
from tkinter import messagebox
import interfaz
from funciones import Agenda

agenda = Agenda()


def ventana_añadir(marco_contactos):

    ventana_añadir = tk.Toplevel()
    ventana_añadir.title("Añadir contacto")
    ventana_añadir.geometry("400x300")
    ventana_añadir.resizable(
        False, False
    )  # Esta line sirve para aque no se pueda cambiar el tamaño de la ventana

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
            interfaz.mostrar_contactos(agenda, marco_contactos)
            ventana_añadir.destroy()
        else:
            messagebox.showerror("Error", mensaje)

    tk.Button(ventana_añadir, text="Guardar", command=boton_guardar).pack(pady=20)


def eliminar_contacto(nombre, telefono, agenda, marco_contactos):
    respuesta = messagebox.askyesno(
        "Confirmar eliminación",
        f"¿Estás seguro de que deseas eliminar el contacto '{nombre}'?",
    )

    if respuesta:
        correcto, mensaje = agenda.eliminar_contacto(nombre, telefono)

        if correcto:
            messagebox.showinfo("Éxito", mensaje)
            interfaz.mostrar_contactos(agenda, marco_contactos)
        else:
            messagebox.showerror("Error", mensaje)


def ventana_buscar():
    ventana_buscar = tk.Toplevel()
    ventana_buscar.title("Buscar contacto")
    ventana_buscar.geometry("400x200")
    ventana_buscar.resizable(
        False, False
    )  # Esta line sirve para aque no se pueda cambiar el tamaño de la ventanaS

    tk.Label(ventana_buscar, text="Nombre del contacto a buscar:").pack(pady=5)

    entrada_nombre = tk.Entry(ventana_buscar)
    entrada_nombre.pack(pady=5)

    def boton_buscar():
        nombre = entrada_nombre.get()

        resultado = agenda.buscar_contacto(nombre)

        if resultado:
            ventana_resultados = tk.Toplevel(ventana_buscar)
            ventana_resultados.title("Resultados de búsqueda")
            ventana_resultados.geometry("600x400")
            ventana_resultados.resizable(False, False)

            tk.Label(
                ventana_resultados,
                text="Contactos encontrados",
                font=("Arial", 14, "bold"),
            ).pack(pady=10)

            marco = tk.Frame(ventana_resultados)
            marco.pack(pady=10)

            # Encabezados
            tk.Label(marco, text="Nombre", font=("Arial", 12, "bold")).grid(
                row=0, column=0, padx=20, pady=10
            )

            tk.Label(marco, text="Teléfono", font=("Arial", 12, "bold")).grid(
                row=0, column=1, padx=20, pady=10
            )

            tk.Label(marco, text="Correo", font=("Arial", 12, "bold")).grid(
                row=0, column=2, padx=20, pady=10
            )
            # Resultados
            for fila, contacto in enumerate(resultado, start=1):

                nombre, telefono, correo = contacto

                tk.Label(marco, text=nombre).grid(row=fila, column=0, padx=20, pady=5)

                tk.Label(marco, text=telefono).grid(row=fila, column=1, padx=20, pady=5)

                tk.Label(marco, text=correo).grid(row=fila, column=2, padx=20, pady=5)

        else:

            messagebox.showerror("Error", "El contacto no se encuentra en la agenda.")

    tk.Button(ventana_buscar, text="Buscar", command=boton_buscar).pack(pady=20)


def ventana_editar(nombre_antiguo, telefono_antiguo, correo_antiguo, marco_contactos):
    ventana_editar = tk.Toplevel()
    ventana_editar.title("Editar contacto")
    ventana_editar.geometry("400x300")
    ventana_editar.resizable(False, False)

    tk.Label(ventana_editar, text="Nombre", anchor="center").pack(pady=5)

    entrada_nombre = tk.Entry(ventana_editar, justify="center")
    entrada_nombre.pack(pady=5)
    entrada_nombre.insert(0, nombre_antiguo)

    tk.Label(ventana_editar, text="Teléfono", anchor="center").pack(pady=5)

    entrada_telefono = tk.Entry(ventana_editar, justify="center")
    entrada_telefono.pack(pady=5)
    entrada_telefono.insert(0, telefono_antiguo)

    tk.Label(ventana_editar, text="Correo", anchor="center").pack(pady=5)

    entrada_correo = tk.Entry(ventana_editar, justify="center")
    entrada_correo.pack(pady=5)
    entrada_correo.insert(0, correo_antiguo)

    def boton_guardar():
        nombre_nuevo = entrada_nombre.get()
        telefono_nuevo = entrada_telefono.get()
        correo_nuevo = entrada_correo.get()

        correcto, mensaje = agenda.editar_contacto(
            nombre_antiguo,
            telefono_antiguo,
            correo_antiguo,
            nombre_nuevo,
            telefono_nuevo,
            correo_nuevo,
        )

        if correcto:
            messagebox.showinfo("Éxito", mensaje)
            interfaz.mostrar_contactos(agenda, marco_contactos)
            ventana_editar.destroy()
        else:
            messagebox.showerror("Error", mensaje)

    tk.Button(ventana_editar, text="Guardar", command=boton_guardar).pack(pady=20)
