import tkinter as tk
from tkinter import messagebox

from funciones import Agenda

agenda = Agenda()


def ventana_añadir(marco_contactos):

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
            mostrar_contactos(agenda, marco_contactos)
            ventana_añadir.destroy()
        else:
            messagebox.showerror("Error", mensaje)

    tk.Button(ventana_añadir, text="Guardar", command=boton_guardar).pack(pady=20)


def ventana_eliminar(marco_contactos):
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
            mostrar_contactos(agenda, marco_contactos)
            ventana_eliminar.destroy()
        else:
            messagebox.showerror("Error", mensaje)

    tk.Button(ventana_eliminar, text="Eliminar", command=boton_eliminar).pack(pady=20)


def ventana_buscar():
    ventana_buscar = tk.Toplevel()
    ventana_buscar.title("Buscar contacto")
    ventana_buscar.geometry("400x200")

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


def mostrar_contactos(agenda, marco_contactos):

    # Limpiar los contactos que ya estaban mostrados
    for widget in marco_contactos.winfo_children():
        widget.destroy()

    # Canvas
    canvas = tk.Canvas(marco_contactos)

    canvas.pack(side="left", fill="both", expand=True)

    # Scrollbar
    scrollbar = tk.Scrollbar(
        marco_contactos,
        orient="vertical",
        command=canvas.yview
    )

    scrollbar.pack(side="right", fill="y")

    # Conectar scrollbar con canvas
    canvas.configure(yscrollcommand=scrollbar.set)

    # Frame donde estarán TODOS los contactos
    contenido = tk.Frame(canvas)

    canvas.create_window(
        (0, 0),
        window=contenido,
        anchor="nw"
    )

    # Actualizar el tamaño del área desplazable
    def actualizar_scroll(event):
        canvas.configure(
            scrollregion=canvas.bbox("all")
        )

    contenido.bind("<Configure>", actualizar_scroll)

    # Configurar las 3 columnas del marco principal con el mismo "uniform"
    marco_contactos.columnconfigure(0, weight=1, uniform="col")
    marco_contactos.columnconfigure(1, weight=1, uniform="col")
    marco_contactos.columnconfigure(2, weight=1, uniform="col")

    try:
        with open(agenda.contactos, "r", encoding="utf-8") as archivo:
            contactos = archivo.readlines()

        if contactos:

            # Títulos
            tk.Label(marco_contactos, text="Nombre", font=("Arial", 12, "bold")).grid(
                row=0, column=0, padx=20, pady=20
            )
            tk.Label(marco_contactos, text="Teléfono", font=("Arial", 12, "bold")).grid(
                row=0, column=1, padx=20, pady=20
            )
            tk.Label(marco_contactos, text="Correo", font=("Arial", 12, "bold")).grid(
                row=0, column=2, padx=20, pady=20
            )

            tk.Label(
                marco_contactos, text="──────────────────────────────────────────"
            ).grid(row=1, column=0, columnspan=3, pady=5)

            # Contactos
            for fila, contacto in enumerate(contactos, start=2):

                nombre, telefono, correo = contacto.strip().split(",")

                marco_contacto = tk.Frame(marco_contactos, bd=1, relief="solid")
                marco_contacto.grid(
                    row=fila, column=0, columnspan=3, pady=5, sticky="ew"
                )

                # MISMO uniform que el marco_contactos -> mismas columnas exactas
                marco_contacto.columnconfigure(0, weight=1, uniform="col")
                marco_contacto.columnconfigure(1, weight=1, uniform="col")
                marco_contacto.columnconfigure(2, weight=1, uniform="col")

                tk.Label(marco_contacto, text=nombre, font=("Arial", 10)).grid(
                    row=0, column=0, padx=20, pady=10
                )
                tk.Label(marco_contacto, text=telefono, font=("Arial", 10)).grid(
                    row=0, column=1, padx=20, pady=10
                )
                tk.Label(marco_contacto, text=correo, font=("Arial", 10)).grid(
                    row=0, column=2, padx=20, pady=10
                )

        else:
            tk.Label(marco_contactos, text="No hay contactos en la agenda.").pack(
                pady=20
            )

    except FileNotFoundError:
        tk.Label(marco_contactos, text="No hay contactos en la agenda.").pack(pady=20)
