listaContactos = [] #Almacena todos los contactos 

while(True):

    print("AGENDA TELEFÓNICA CON PYTHON")

    print("Bienvenido a la agenda telefónica, por favor seleccione una opción: \n")
    print("1. Agregar contacto")
    print("2. Buscar contacto")
    print("3. Mostrar todos los contactos")
    print("4. Eliminar contacto")
    print("5. Editar contacto")
    print("6. Salir")

    opcion = input("Eliga la opción que deseas realizar: ")


    match opcion:
        case "1":
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
                archivo.write(contacto["nombre"] + "," + contacto["telefono"] + ","+ contacto["email"]+"\n")
        case "2":
            print("Has elegido Buscar un contacto")
            telefonoContacto = input("Ingrese un numero de telefono: ")
            encontrado = False
            with open("contactos.txt", "r", encoding='utf-8') as archivo:
                for linea in archivo:
                    datos = linea.split(',')
                    if(datos[1] == telefonoContacto):
                        print("Encontrado!!!" + " corrresponde al contacto de" + datos[0])
                        encontrado = True
            if(not encontrado):
                print(f"El telefono {telefonoContacto} no existe en la base de contacto")
        case "3":
            print("Has elegido Mostrar Contactos")

            with open("contactos.txt", "r", encoding='utf-8') as archivo:
                for linea in archivo:
                    print(linea)
        case "4":
            print("Has elegido Eliminar un Contacto")
            listaContactos.clear()
            telefonoContacto = input("Introduce un numero de telefono para eliminar")
            with open("contactos.txt", "r", encoding='utf-8') as archivo:
                for linea in archivo:
                    datos = linea.split(',')
                    if(telefonoContacto != datos[1]):
                        contacto = {
                            "nombre": datos[0],
                            "telefono": datos[1],
                            "email" : datos[2]
                        }
                        listaContactos.append(contacto)
            for contact in listaContactos:
                print(contact)

            respuesta = input("¿Deseas realmente eliminar este contacto (S=Si \ N=No)")
            if(respuesta == "S" or respuesta == "s"):
                texto = ""
                for contacto in listaContactos:
                    texto = texto + contacto["nombre"] + "," + contacto["telefono"] + ","+ contacto["email"]
                with open("contactos.txt", "w", encoding='utf-8') as archivo:
                    archivo.write(texto)
                        
            else:
                print("Cancelar operación")
        case "5":
            print("Has elegido Editar un Contacto")
            listaContactos.clear()
            telefonoContacto = input("Introduce un numero de telefono para editar")
            with open("contactos.txt", "r", encoding='utf-8') as archivo:
                for linea in archivo:
                    datos = linea.split(',')
                    if(telefonoContacto != datos[1]):
                        contacto = {
                            "nombre": datos[0],
                            "telefono": datos[1],
                            "email" : datos[2]
                        }
                        listaContactos.append(contacto)
                    else:
                        nombre=input("Introduce un nuevo nombre para el contacto")
                        telefono=input("Introduce un nuevo telefono para el contacto")
                        email = input("Introduce el nuevo correo para el contacto")

                        contacto = {
                                    "nombre": nombre,
                                    "telefono": telefono,
                                    "email" : email+"\n"
                                }
                        listaContactos.append(contacto)

            texto = ""
            for contacto in listaContactos:
                texto = texto + contacto["nombre"] + "," + contacto["telefono"] + ","+ contacto["email"]
            with open("contactos.txt", "w", encoding='utf-8') as archivo:
                archivo.write(texto)

        case "6":
            print("Has elegido Salir del Programa")
            break

print("El programa se terminó")