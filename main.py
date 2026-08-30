listaContactos = [] #Almacena todos los contactos 
opcion = 0
while(opcion !=6):

    print("AGENDA TELEFÓNICA CON PYTHON")

    print("Bienvenido a la agenda telefónica, por favor seleccione una opción: \n")
    print("1. Agregar contacto")
    print("2. Buscar contacto")
    print("3. Mostrar todos los contactos")
    print("4. Eliminar contacto")
    print("5. Editar contacto")
    print("6. Salir")

    opcion = int(input("Eliga la opción que deseas realizar: "))


    match opcion:
        case 1:
            print("Has elegido Agregar Contacto")
            nombre = input("Introduce el nombre de la persona: ")
            telefono = input("Introduce el telefono de la persona: ")
            email = input("Introduce el correo electronico de la persona: ")

            contacto = {
                "nombre":nombre,
                "telefono":telefono,
                "email":email
            }
            #listaContactos.append(contacto)
            with open("contactos.txt", "a") as archivo:
                archivo.write("Nombre contacto: " + contacto["nombre"] + ", Telefono contacto: " + contacto["telefono"] + ", Email contacto: " + contacto["email"]+"\n")
        case 2:
            print("Has elegido opcion 2")
        case 3:
            print("Has elegido opcion 3")
        case 4:
            print("Has elegido opcion 4")
        case 5:
            print("Has elegido opcion 5")
        case 6:
            print("Has elegido Salir del Programa")

print("El programa se terminó")