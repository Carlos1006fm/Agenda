def añadir_contacto():
    nombre = input("Ingrese el nombre del contacto: ")
    telefono = input("Ingrese el número de teléfono del contacto: ")
    correo = input("Ingrese el correo electrónico del contacto: ")

    if not nombre or not telefono or not correo:
        print("Error: Todos los campos son obligatorios.")

    elif not telefono.isdigit() or len(telefono) != 9:
        print("Error: El teléfono debe contener 9 dígitos.")

    elif "@" not in correo or "." not in correo:
        print("Error: El correo no es válido.")

    else:
        with open("contactos.txt", "a", encoding="utf-8") as archivo:
            archivo.write(f"{nombre},{telefono},{correo}\n")

    return "Contacto añadido exitosamente."


def ver_contactos():
    try:
        with open("contactos.txt", "r") as archivo:
            contactos = archivo.readlines()
            if contactos:
                print("Lista de contactos:")
                print("-------------------------------------------------------------")
                print("Nombre\t Teléfono\t Correo")
                print("-------------------------------------------------------------")
                for contacto in contactos:
                    nombre, telefono, correo = contacto.strip().split(",")
                    print(f"{nombre}\t {telefono}\t {correo}\n")
            else:
                print("No hay contactos en la agenda.\n")
    except FileNotFoundError:
        print("No se encontró el archivo de contactos.")


def eliminar_contacto():
    nombre_eliminar = input("Ingrese el nombre del contacto a eliminar: ")
    try:
        with open("contactos.txt", "r") as archivo:
            contactos = archivo.readlines()

        with open("contactos.txt", "w") as archivo:
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


def buscar_contacto():
    nombre_buscar = input("Ingrese el nombre del contacto a buscar: ")
    try:
        with open("contactos.txt", "r") as archivo:
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
