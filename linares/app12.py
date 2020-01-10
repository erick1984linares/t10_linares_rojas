import libreria


def llamada_familiar():
    telefono=libreria.pedir_telefono("Agregar telefono:")
    nombre=libreria.pedir_nombre("nombre del familiar:")
    contenido=str(telefono) + "-" + str(nombre) + "\n"
    libreria.guardar_datos("info.txt", contenido, "a")
    print("Datos guardados")

def llamada_a_amigo():
    telefono=libreria.pedir_telefono("Agregar telefono:")
    nombre=libreria.pedir_nombre("nombre del amigo:")
    contenido=str(telefono) + "-" + str(nombre) + "\n"
    libreria.guardar_datos("info.txt", contenido, "a")
    print("Datos guardados")

def verDatos():
    datos = libreria.obtener_datos("info.txt")
    if ( datos != ""):
        print(datos)
    else:
        print("Archivo sin datos")

def llamar_tia():
    opc=0
    max=3
    while (opc!= max):
        print("######### llamada a familiar ########")
        print("1. llamar tia")
        print("2. Var datos")
        print("3. Salir")
        print("#######################")
        opc =libreria.pedir_numero("Ingrese subopcion: ", 1, 3)
        if( opc == 1):
            llamada_familiar()
        if( opc == 2):
            verDatos()

def llamada_a_amistades():
    opc=0
    max=3
    while (opc!= max):
        print("######### llamada a amigo ########")
        print("1. llamar tio")
        print("2. Var datos")
        print("3. Salir")
        print("#######################")
        opc =libreria.pedir_numero("Ingrese subopcion: ", 1, 3)
        if( opc == 1):
            llamada_a_amigo()
        if( opc == 2):
            verDatos()
opc=0
max=3
while( opc!= max ):
    print("######### MENU ########")
    print("1. llamar tia")
    print("2. llamar a amigo")
    print("3. Salir")
    print("#######################")

    opc =libreria.pedir_numero("Ingrese opcion: ", 1, 3 )

    if( opc == 1 ):
        llamar_tia()
    if( opc == 2 ):
        llamada_a_amistades()

#fin

print("Fin del programa")
