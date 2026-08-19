import tkinter as tk
from tkinter import messagebox

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
            mostrar_contactos(agenda, marco_contactos)
            ventana_añadir.destroy()
        else:
            messagebox.showerror("Error", mensaje)

    tk.Button(ventana_añadir, text="Guardar", command=boton_guardar).pack(pady=20)


def ventana_eliminar(marco_contactos):
    ventana_eliminar = tk.Toplevel()
    ventana_eliminar.title("Eliminar contacto")
    ventana_eliminar.geometry("400x300")
    ventana_eliminar.resizable(
        False, False
    )  # Esta line sirve para aque no se pueda cambiar el tamaño de la ventana

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


def mostrar_contactos(agenda, marco_contactos):

    # Limpiar los contactos que ya estaban mostrados
    for widget in marco_contactos.winfo_children():
        widget.destroy()

    # Canvas
    canvas = tk.Canvas(marco_contactos)

    canvas.pack(side="left", fill="both", expand=True)

    # Scrollbar
    scrollbar = tk.Scrollbar(marco_contactos, orient="vertical", command=canvas.yview)

    scrollbar.pack(side="right", fill="y")

    # Conectar scrollbar con canvas
    canvas.configure(yscrollcommand=scrollbar.set)

    # Frame donde estarán TODOS los contactos
    contenido = tk.Frame(canvas)

    ventana_canvas = canvas.create_window((0, 0), window=contenido, anchor="nw")

    # Actualizar el tamaño del área desplazable
    def actualizar_scroll(event):
        canvas.configure(scrollregion=canvas.bbox("all"))

    contenido.bind("<Configure>", actualizar_scroll)

    def actualizar_ancho(event):
        canvas.itemconfig(ventana_canvas, width=event.width)

    canvas.bind("<Configure>", actualizar_ancho)

    # ==========================================
    # LEER CONTACTOS
    # ==========================================

    try:

        with open(agenda.contactos, "r", encoding="utf-8") as archivo:

            contactos = archivo.readlines()

        # ==========================================
        # SI NO HAY CONTACTOS
        # ==========================================

        if not contactos:

            tk.Label(
                contenido, text="No hay contactos en la agenda.", font=("Arial", 12)
            ).grid(row=0, column=0, padx=20, pady=20)

            return

        # ==========================================
        # CONFIGURAR COLUMNAS
        # ==========================================

        contenido.columnconfigure(0, weight=1, uniform="col")

        contenido.columnconfigure(1, weight=1, uniform="col")

        contenido.columnconfigure(2, weight=1, uniform="col")

        # ==========================================
        # TÍTULOS
        # ==========================================

        tk.Label(contenido, text="Nombre", font=("Arial", 12, "bold")).grid(
            row=0, column=0, padx=20, pady=20
        )

        tk.Label(contenido, text="Teléfono", font=("Arial", 12, "bold")).grid(
            row=0, column=1, padx=20, pady=20
        )

        tk.Label(contenido, text="Correo", font=("Arial", 12, "bold")).grid(
            row=0, column=2, padx=20, pady=20
        )

        # ==========================================
        # LÍNEA SEPARADORA
        # ==========================================

        tk.Frame(contenido, height=2, bd=0, relief="solid", bg="black").grid(
            row=1, column=0, columnspan=3, padx=10, pady=5, sticky="ew"
        )

        # ==========================================
        # MOSTRAR CONTACTOS
        # ==========================================

        fila = 2

        for contacto in contactos:

            contacto = contacto.strip()

            # Ignorar líneas vacías, si no hay ningun contacto en esa linea sale a la siguiente iteracion del for
            if not contacto:
                continue

            datos = contacto.split(",")

            # Comprobar que tenga nombre, teléfono y correo si tiene dos datos sale a la siguiente iteracion del for
            if len(datos) != 3:
                continue

            nombre = datos[0].strip()
            telefono = datos[1].strip()
            correo = datos[2].strip()

            # ------------------------------------------
            # Marco del contacto
            # ------------------------------------------

            marco_contacto = tk.Frame(contenido, bd=1, relief="solid")

            marco_contacto.grid(
                row=fila, column=0, columnspan=3, padx=10, pady=5, sticky="ew"
            )

            # Columnas iguales
            marco_contacto.columnconfigure(0, weight=1, uniform="contacto")

            marco_contacto.columnconfigure(1, weight=1, uniform="contacto")

            marco_contacto.columnconfigure(2, weight=1, uniform="contacto")

            # ------------------------------------------
            # Nombre
            # ------------------------------------------

            tk.Label(marco_contacto, text=nombre, font=("Arial", 10)).grid(
                row=0, column=0, padx=20, pady=10, sticky="ew"
            )

            # ------------------------------------------
            # Teléfono
            # ------------------------------------------

            tk.Label(marco_contacto, text=telefono, font=("Arial", 10)).grid(
                row=0, column=1, padx=20, pady=10, sticky="ew"
            )

            # ------------------------------------------
            # Correo
            # ------------------------------------------

            label_correo = tk.Label(
                marco_contacto,
                text=correo,
                font=("Arial", 10),
                justify="center",
            )
            label_correo.grid(row=0, column=2, padx=20, pady=10, sticky="ew")

            label_correo.bind(  # Adapta el texto del correo al ancho disponible
                "<Configure>",
                lambda event, lbl=label_correo: lbl.configure(
                    wraplength=max(event.width - 10, 50)
                ),
            )

            label_correo.bind(  # Cuando se hace clic en el correo, abre un mensaje mostrando el correo completo
                "<Button-1>",
                lambda event, c=correo, n=nombre: messagebox.showinfo(
                    f"Correo de {n}", c
                ),
            )

            fila += 1

            boton = tk.Frame(contenido)

            boton.grid(row=fila, column=0, columnspan=3, pady=20)

            tk.Button(
                boton,
                text="Añadir contacto",
                width=15,
                command=lambda: ventana_añadir(marco_contactos),
            ).pack(side="left", padx=5)

            tk.Button(
                boton,
                text="Eliminar contacto",
                width=15,
                command=lambda: ventana_eliminar(marco_contactos),
            ).pack(side="left", padx=5)

            tk.Button(
                boton, text="Buscar contacto", width=15, command=ventana_buscar
            ).pack(side="left", padx=5)

    except FileNotFoundError:

        tk.Label(
            contenido, text="No hay contactos en la agenda.", font=("Arial", 12)
        ).grid(row=0, column=0, padx=20, pady=20)
