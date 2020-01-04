import libreria

def movimiento():
    epicentro=libreria.pedir_departamento("lugar del terremoto:")
    magnitud=libreria.pedir_numero("magnitud aproximado del terremoto:", 4, 9)
    contenido=epicentro + "-" + str(magnitud) + "\n"
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
        print("######### terremoto ########")
        print("1. terremoto")
        print("2. Var datos")
        print("3. Salir")
        print("#######################")
        opc =libreria.pedir_numero("Ingrese subopcion: ", 1, 3)
        if( opc == 1):
            movimiento()
        if( opc == 2):
            verDatos()
def opcionB():
    opc=0
    max=3
    while (opc!= max):
        print("######### temblor ########")
        print("1. temblor")
        print("2. Var datos")
        print("3. Salir")
        print("#######################")
        opc =libreria.pedir_numero("Ingrese subopcion: ", 1, 3)
        if( opc == 1):
            movimiento()
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

