import libreria


def hacercompra():
    precio=libreria.pedir_numero("precio:", 30, 50)
    nombre=libreria.pedir_nombre("nombre del producto:")
    contenido=str(precio) + "-" + str(nombre) + "\n"
    libreria.guardar_datos("info.txt", contenido, "a")
    print("Datos guardados")

def hacercompra_en_joyeria():
    precio=libreria.pedir_numero("precio:", 800, 900)
    nombre=libreria.pedir_nombre("nombre de la Joya:")
    contenido=str(precio) + "-" + str(nombre) + "\n"
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
        print("######### COMPRA DE PRODUCTOS ########")
        print("1. Hacer compra de joyas")
        print("2. Var datos")
        print("3. Salir")
        print("#######################")
        opc =libreria.pedir_numero("Ingrese subopcion: ", 1, 3)
        if( opc == 1):
            hacercompra()
        if( opc == 2):
            verDatos()
def opcionB():
    opc=0
    max=3
    while (opc!= max):
        print("######### COMPRA DE JOYAS ########")
        print("1. Hacer compra del producto 2")
        print("2. Var datos")
        print("3. Salir")
        print("#######################")
        opc =libreria.pedir_numero("Ingrese subopcion: ", 1, 3)
        if( opc == 1):
            hacercompra_en_joyeria()
        if( opc == 2):
            verDatos()

opc=0
max=3
while( opc!= max ):
    print("######### MENU ########")
    print("1. Comprar producto ")
    print("2. Compra de joyas")
    print("3. Salir")
    print("#######################")

    opc =libreria.pedir_numero("Ingrese opcion: ", 1, 3 )

    if( opc == 1 ):
        opcionA()
    if( opc == 2 ):
        opcionB()

#fin

print("Fin del programa")

