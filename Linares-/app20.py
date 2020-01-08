import libreria


def agregarguerras():
    guerra=libreria.pedir_guerras("Ingrese guerra acontecida:")
    paises=libreria.pedir_paises_involucrados("Ingrese paises involucrado:")
    numero_de_muertos=libreria.pedir_numero("ingrese numero en millones de muertos aproximados segun la guerra:", 15, 60)
    contenido=guerra + "-" + str(paises) + "-" + numero_de_muertos + "\n"
    libreria.guardar_datos("info.txt", contenido, "a")
    print("Datos guardados")

def agregarguerras2():
    guerra=libreria.pedir_guerras("Ingrese guerra acontecida:")
    paises=libreria.pedir_paises_involucrados("Ingrese paises involucrado:")
    numero_de_muertos=libreria.pedir_numero("ingrese numero en millones de muertos aproximados segun la guerra:", 15, 60)
    contenido=guerra + "-" + str(paises) + "-" + numero_de_muertos + "\n"
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
        print("######### Primera guerra mundial ########")
        print("1. agregar guerra 1")
        print("2. Var datos")
        print("3. Salir")
        print("#######################")
        opc =libreria.pedir_numero("Ingrese subopcion: ", 1, 3)
        if( opc == 1):
            agregarguerras()
        if( opc == 2):
            verDatos()

def opcionB():
    opc=0
    max=3
    while (opc!= max):
        print("######### Segunda guerra mundial ########")
        print("1. agregar guerra 2")
        print("2. Var datos")
        print("3. Salir")
        print("#######################")
        opc =libreria.pedir_numero("Ingrese subopcion: ", 1, 3)
        if( opc == 1):
            agregarguerras2()
        if( opc == 2):
            verDatos()


opc=0
max=3
while( opc!= max ):
    print("######### MENU ########")
    print("1. Comprar producto 1")
    print("2. Comprar producto 2")
    print("3. Salir")
    print("#######################")

    opc =libreria.pedir_numero("Ingrese opcion: ", 1, 3 )

    if( opc == 1 ):
        opcionA()
    if( opc == 2 ):
        opcionB()

#fin

print("Fin del programa")

