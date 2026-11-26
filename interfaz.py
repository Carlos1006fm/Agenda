import tkinter as tk
from tkinter import messagebox
import botones
from funciones import Agenda

agenda = Agenda()
imagen_editar = None
imagen_eliminar = None


def mostrar_contactos(agenda, marco_contactos):

    # Limpiar los contactos que ya estaban mostrados
    for widget in marco_contactos.winfo_children():
        widget.destroy()

    # Canvas (se crea ya, pero se empaqueta más abajo)
    canvas = tk.Canvas(marco_contactos, bg="#F5F7FA", highlightthickness=0)

    # Scrollbar: se empaqueta PRIMERO para reservar su espacio a la derecha
    # antes de que los títulos o el canvas calculen su propio ancho.
    scrollbar = tk.Scrollbar(marco_contactos, orient="vertical", command=canvas.yview)

    scrollbar.pack(side="right", fill="y")

    # ==========================================
    # MOSTRAR TITULOS
    # ==========================================
    # Ahora el ancho disponible ya descuenta el scrollbar,
    # igual que le pasará al canvas.

    crear_marco_titulos(marco_contactos)

    canvas.pack(side="left", fill="both", expand=True)

    # Conectar scrollbar con canvas
    canvas.configure(yscrollcommand=scrollbar.set)

    canvas.bind_all(
        "<MouseWheel>",
        lambda event: canvas.yview_scroll(int(-1 * (event.delta / 120)), "units"),
    )

    # Frame donde estarán TODOS los contactos
    contenido = tk.Frame(canvas, bg="#F5F7FA")

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
        # CONFIGURAR COLUMNAS (mismo grupo "col" que los títulos)
        # ==========================================

        contenido.columnconfigure(0, weight=1, uniform="col")
        contenido.columnconfigure(1, weight=1, uniform="col")
        contenido.columnconfigure(2, weight=1, uniform="col")
        contenido.columnconfigure(3, weight=1, uniform="col")

        # ==========================================
        # MOSTRAR CONTACTOS
        # ==========================================

        fila = 2

        for contacto in contactos:

            contacto = contacto.strip()

            if not contacto:
                continue

            datos = contacto.split(",")

            if len(datos) != 3:
                continue

            nombre = datos[0].strip()
            telefono = datos[1].strip()
            correo = datos[2].strip()

            fila += 1

            # ------------------------------------------
            # Marco del contacto
            # ------------------------------------------

            marco_contacto = tk.Frame(contenido, bg="#F5F7FA")

            marco_contacto.grid(row=fila, column=0, columnspan=4, pady=5, sticky="ew")

            # Mismo grupo "col" que los títulos -> mismo ancho exacto
            marco_contacto.columnconfigure(0, weight=1, uniform="col")
            marco_contacto.columnconfigure(1, weight=1, uniform="col")
            marco_contacto.columnconfigure(2, weight=1, uniform="col")
            marco_contacto.columnconfigure(3, weight=1, uniform="col")

            # ------------------------------------------
            # Nombre y Estrella a la izquierda
            # ------------------------------------------

            marco_nombre = tk.Frame(marco_contacto, bg="#F5F7FA")
            marco_nombre.grid(row=0, column=0, padx=20, pady=10, sticky="ew")

            # Compureba si el contacto es favorito y muestra la estrella correspondiente
            estrella = "★" if agenda.es_favorito(nombre, telefono, correo) else "☆"

            # Estrella a la izquierda

            tk.Button(
                marco_nombre,
                text=estrella,
                font=("Arial", 14),
                relief="flat",
                bg="#F5F7FA",
                cursor="hand2",
                command=lambda n=nombre, t=telefono, c=correo: (
                    agenda.cambiar_favorito(n, t, c),
                    mostrar_contactos(agenda, marco_contactos),
                ),
            ).pack(side="left", padx=5)

            # Nombre a la derecha
            tk.Label(marco_nombre, text=nombre, font=("Arial", 10), bg="#F5F7FA").pack(
                side="left"
            )

            # ------------------------------------------
            # Teléfono
            # ------------------------------------------

            tk.Label(
                marco_contacto, text=telefono, font=("Arial", 10), bg="#F5F7FA"
            ).grid(row=0, column=1, padx=20, pady=10, sticky="ew")

            # ------------------------------------------
            # Correo
            # ------------------------------------------

            label_correo = tk.Label(
                marco_contacto,
                text=correo,
                font=("Arial", 10),
                justify="center",
                bg="#F5F7FA",
            )
            label_correo.grid(row=0, column=2, padx=20, pady=10, sticky="ew")

            label_correo.bind(
                "<Configure>",
                lambda event, lbl=label_correo: lbl.configure(
                    wraplength=max(event.width - 10, 50)
                ),
            )

            label_correo.bind(
                "<Button-1>",
                lambda event, c=correo, n=nombre: messagebox.showinfo(
                    f"Correo de {n}", c
                ),
            )

            # ------------------------------------------
            # Frame de botones (Editar y Eliminar)
            # ------------------------------------------

            marco_botones = tk.Frame(marco_contacto, bg="#F5F7FA")
            marco_botones.grid(row=0, column=3, padx=5)

            boton_editar = tk.Button(
                marco_botones,
                image=imagen_editar,
                relief="flat",
                borderwidth=0,
                cursor="hand2",
                command=lambda: botones.ventana_editar(
                    nombre, telefono, correo, marco_contactos
                ),
            )
            boton_editar.pack(side="left", padx=5)

            boton_eliminar = tk.Button(
                marco_botones,
                image=imagen_eliminar,
                bg="#F5F7FA",
                activebackground="#F5F7FA",
                relief="flat",
                borderwidth=0,
                cursor="hand2",
                command=lambda n=nombre, t=telefono: botones.eliminar_contacto(
                    n, t, agenda, marco_contactos
                ),
            )
            boton_eliminar.pack(side="left", padx=5)
            # ==========================================
            # BOTONES DE ACCIÓN (fuera del for, una sola vez)
            # ==========================================

        marco_contactos.winfo_children()

    except FileNotFoundError:

        tk.Label(
            contenido, text="No hay contactos en la agenda.", font=("Arial", 12)
        ).grid(row=0, column=0, padx=20, pady=20)


def crear_marco_titulos(contenedor):
    # Marco de los títulos (sin padx en el pack -> mismo punto de partida que el canvas)
    marco_titulos = tk.Frame(contenedor, bg="#2878E8")

    marco_titulos.pack(side="top", fill="x")

    # Configurar las columnas con el MISMO grupo "col" usado en contenido y marco_contacto
    for i in range(4):
        marco_titulos.columnconfigure(i, weight=1, uniform="col")

    # Títulos (mismo padx=20 que las columnas de datos, para que quede exacto)
    tk.Label(
        marco_titulos,
        text="Nombre",
        font=("Arial", 12, "bold"),
        bg="#2878E8",
        fg="white",
    ).grid(row=0, column=0, padx=20, pady=10, sticky="ew")

    tk.Label(
        marco_titulos,
        text="Teléfono",
        font=("Arial", 12, "bold"),
        bg="#2878E8",
        fg="white",
    ).grid(row=0, column=1, padx=20, pady=10, sticky="ew")

    tk.Label(
        marco_titulos,
        text="Correo",
        font=("Arial", 12, "bold"),
        bg="#2878E8",
        fg="white",
    ).grid(row=0, column=2, padx=20, pady=10, sticky="ew")

    tk.Label(
        marco_titulos,
        text="Acción",
        font=("Arial", 12, "bold"),
        bg="#2878E8",
        fg="white",
    ).grid(row=0, column=3, padx=20, pady=10, sticky="ew")


def mostrar_botones(contenedor, marco_contactos):

    boton = tk.Frame(contenedor, bg="#F5F7FA")

    boton.pack(side="left", padx=5)

    tk.Button(
        boton,
        text="Añadir contacto",
        width=15,
        command=lambda: botones.ventana_añadir(marco_contactos),
        bg="#F5F7FA",
    ).pack(side="left", padx=5)

    tk.Button(
        boton,
        text="Buscar contacto",
        width=15,
        bg="#F5F7FA",
        command=botones.ventana_buscar,
    ).pack(side="left", padx=5)
