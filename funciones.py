import os
CARPETA = 'contactos/'

def mostrarMenu():
    print("AGENDA TELEFÓNICA CON PYTHON")
    
    print("Bienvenido a la agenda telefónica, por favor seleccione una opción: \n")
    print("1. Agregar contacto")
    print("2. Buscar contacto")
    print("3. Mostrar todos los contactos")
    print("4. Eliminar contacto")
    print("5. Editar contacto")
    print("6. Salir")

def crearDirectorio():
    if(not os.path.exists(CARPETA)):
        os.makedirs(CARPETA)