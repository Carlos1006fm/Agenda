import funciones

print("Bienvenido a la Agenda de Contactos")

opcion = ""
while opcion != "5":
    print("1. Añadir contacto")
    print("2. Ver contactos")
    print("3. Eliminar contacto")
    print("4. Buscar contacto")
    print("5. Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        funciones.añadir_contacto()
    elif opcion == "2":
        funciones.ver_contactos()
    elif opcion == "3":
        funciones.eliminar_contacto()
    elif opcion == "4":
        funciones.buscar_contacto()
    elif opcion == "5":
        print("Saliendo de la agenda. ¡Hasta luego!")
