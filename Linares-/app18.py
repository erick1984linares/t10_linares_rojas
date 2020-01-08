import libreria


def ciclo1():
    nombre_de_docente=libreria.pedir_nombre("Nombre del docente:")
    curso=libreria.pedir_nombre("Nombre del curso:")
    contenido=nombre_de_docente + "-" + str(curso) + "\n"
    libreria.guardar_datos("info.txt", contenido, "a")
    print("Datos guardados")

def ciclo2():
    nombre_de_docente=libreria.pedir_nombre("Nombre del docente:")
    curso=libreria.pedir_nombre("Nombre del curso:")
    contenido=nombre_de_docente + "-" + str(curso) + "\n"
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
        print("######### Ver datos del ciclo 1 ########")
        print("1. ciclo")
        print("2. Var datos")
        print("3. Salir")
        print("#######################")
        opc =libreria.pedir_numero("Ingrese subopcion: ", 1, 3)
        if( opc == 1):
            ciclo1()
        if( opc == 2):
            verDatos()
def opcionB():
    opc=0
    max=3
    while (opc!= max):
        print("######### ver datos del ciclo 2 ########")
        print("1. ciclo 2")
        print("2. Var datos")
        print("3. Salir")
        print("#######################")
        opc =libreria.pedir_numero("Ingrese subopcion: ", 1, 3)
        if( opc == 1):
            ciclo2()
        if( opc == 2):
            verDatos()

opc=0
max=3
while( opc!= max ):
    print("######### MENU ########")
    print("1. ver datos del ciclo 1")
    print("2. ver datos del ciclo 2")
    print("3. Salir")
    print("#######################")

    opc =libreria.pedir_numero("Ingrese opcion: ", 1, 3 )

    if( opc == 1 ):
        opcionA()
    if( opc == 2 ):
        opcionB()
#fin

print("Fin del programa")

