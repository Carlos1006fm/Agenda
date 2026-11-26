import tkinter as tk
from funciones import Agenda
import interfaz
import barra_lateral

agenda = Agenda()

# Colores
FONDO = "#F5F7FA"

# Crear ventana
ventana = tk.Tk()
ventana.title("Agenda de contactos")
ventana.geometry("1000x650")
ventana.minsize(800, 500)

interfaz.imagen_editar = tk.PhotoImage(
    master=ventana, file="Iconos/editar.png"
).subsample(
    15, 15
)  # Ajusta el tamaño de la imagen según sea necesario

interfaz.imagen_eliminar = tk.PhotoImage(
    master=ventana, file="Iconos/basura.png"
).subsample(
    18, 18
)  # Ajusta el tamaño de la imagen según sea necesario

# Panel principal
contenido = tk.Frame(ventana, bg=FONDO)

# Titulo
titulo = tk.Label(
    contenido,
    text="AGENDA DE CONTACTOS 📒",
    bg=FONDO,
    font=("Arial", 20, "bold"),
    fg="#172B4D",
)
titulo.pack(pady=20)

# Marco para los botones
marco_botones = tk.Frame(contenido, bg=FONDO)
marco_botones.pack(pady=10)

# Zona donde se muestran los contactos
marco_contactos = tk.Frame(contenido, bg=FONDO)
marco_contactos.pack(pady=20, fill="both", expand=True)

# Mostrar botones
interfaz.mostrar_botones(marco_botones, marco_contactos)


# Funciones de navegación
def ir_contactos():
    interfaz.mostrar_contactos(agenda, marco_contactos)


def ir_favoritos():
    interfaz.mostrar_favoritos(agenda, marco_contactos)


# Creacion de la barra lateral
barra = barra_lateral.BarraLateral(ventana, ir_contactos, ir_favoritos)

# Empaquetar después el contenido principal
contenido.pack(side="left", fill="both", expand=True)

# Mostrar contactos inicialmente
ir_contactos()

ventana.mainloop()
