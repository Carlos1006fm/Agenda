import tkinter as tk


class BarraLateral:

    def __init__(self, ventana, mostrar_contactos, mostrar_favoritos=None):

        self.color_fondo = "#172B4D"
        self.color_activo = "#2878E8"

        self.barra = tk.Frame(ventana, bg=self.color_fondo, width=220)

        self.barra.pack(side="left", fill="y")
        self.barra.pack_propagate(False)

        self.mostrar_contactos = mostrar_contactos
        self.mostrar_favoritos = mostrar_favoritos

        self.crear_titulo()
        self.crear_botones()
        self.crear_pie()

    def crear_titulo(self):

        tk.Label(
            self.barra,
            text="AGENDA\nDE CONTACTOS",
            bg=self.color_fondo,
            fg="white",
            font=("Arial", 17, "bold"),
            justify="left",
        ).pack(anchor="w", padx=15, pady=25)

    def crear_botones(self):

        self.boton_contactos = tk.Button(
            self.barra,
            text="  ♟  Contactos",
            command=self.mostrar_contactos,
            bg=self.color_activo,
            fg="white",
            relief="flat",
            anchor="w",
            padx=15,
            pady=13,
            font=("Arial", 11),
        )

        self.boton_contactos.pack(fill="x", padx=10, pady=5)

        self.boton_favoritos = tk.Button(
            self.barra,
            text="  ★  Favoritos",
            command=self.abrir_favoritos,
            bg=self.color_fondo,
            fg="white",
            activebackground=self.color_activo,
            activeforeground="white",
            relief="flat",
            anchor="w",
            padx=15,
            pady=13,
            font=("Arial", 11),
        )

        self.boton_favoritos.pack(fill="x", padx=10, pady=5)

        self.crear_boton("  ◆  Etiquetas")
        self.crear_boton("  ⚙  Configuración")

    def crear_boton(self, texto):

        tk.Button(
            self.barra,
            text=texto,
            bg=self.color_fondo,
            fg="white",
            activebackground=self.color_activo,
            activeforeground="white",
            relief="flat",
            anchor="w",
            padx=15,
            pady=13,
            font=("Arial", 11),
        ).pack(fill="x", padx=10, pady=5)

    def abrir_favoritos(self):

        if self.mostrar_favoritos:
            self.mostrar_favoritos()

    def crear_pie(self):

        tk.Frame(self.barra, bg="#52647D", height=1).pack(
            side="bottom", fill="x", padx=20, pady=15
        )

        tk.Label(
            self.barra,
            text="Agenda de contactos",
            bg=self.color_fondo,
            fg="white",
            font=("Arial", 10),
        ).pack(side="bottom", pady=10)
