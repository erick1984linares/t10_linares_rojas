import libreria


def redes_saciales():
    red=libreria.pedir_red_social("Ingrese red social:")
    años_de_creacion=libreria.pedir_numero("año de creacion:", 2004, 2010)
    contenido=red + "-" + str(años_de_creacion) + "\n"
    libreria.guardar_datos("info.txt", contenido, "a")
    print("Datos guardados")

def red_sacial_mas_famosa():
    red=libreria.pedir_red_social("Ingrese red social:")
    años_de_creacion=libreria.pedir_numero("año de creacion:", 2004, 2010)
    contenido=red + "-" + str(años_de_creacion) + "\n"
    libreria.guardar_datos("info.txt", contenido, "a")
    print("Datos guardados")

def verDatos():
    datos = libreria.obtener_datos("info.txt")
    if ( datos != ""):
        print(datos)
    else:
        print("Archivo sin datos")

def opcionA():
    opc=0
    max=3
    while (opc!= max):
        print("######### redes sociales ########")
        print("1. redes sociales")
        print("2. Var datos")
        print("3. Salir")
        print("#######################")
        opc =libreria.pedir_numero("Ingrese subopcion: ", 1, 3)
        if( opc == 1):
            redes_saciales()
        if( opc == 2):
            verDatos()

def opcionB():
    opc=0
    max=3
    while (opc!= max):
        print("######### red social mas famosa ########")
        print("1. red social mas famosa")
        print("2. Var datos")
        print("3. Salir")
        print("#######################")
        opc =libreria.pedir_numero("Ingrese subopcion: ", 1, 3)
        if( opc == 1):
            red_sacial_mas_famosa()
        if( opc == 2):
            verDatos()


opc=0
max=3
while( opc!= max ):
    print("######### MENU ########")
    print("1. opcionA")
    print("2. opcionB")
    print("3. Salir")
    print("#######################")

    opc =libreria.pedir_numero("Ingrese opcion: ", 1, 3 )

    if( opc == 1 ):
        opcionA()
    if( opc == 2 ):
        opcionB()

#fin

print("Fin del programa")

