from Rojas import libreria



def agregrrr():
    nombre=libreria.pedir_nombre("nombre del destino: ")
    monto=libreria.pedir_numero("agrege el costo del viaje: ", 10, 5000)
    contenido=str(nombre) + "-" + str(monto)+"\n"
    libreria.guardar_datos("viajes.txt", contenido, "a")
    print("Datos guardados")

def ver_datos():
    datos = libreria.obtener_datos("viajes.txt")
    if ( datos != ""):
        print("lugar -- costo")
        print(datos)
    else:
        print("sin datos")

def opcion_1():
    opc=0
    max=3
    while (opc!= max):
        print("######### AGREGAR DESTINO NACIONAL ########")
        print("# 1. agregar ")
        print("# 2. Ver datos")
        print("# 3. Salir")
        print("####################################")
        opc =libreria.pedir_numero("Ingrese la opcion: ", 1, 3)
        if( opc == 1):
            agregrrr()
        if( opc == 2):
            ver_datos()
def opcion_2():
    opc=0
    max=3
    while (opc!= max):
        print("######### AGREGAR DESTINO INTERNACIONAL ########")
        print("# 1. agregar ")
        print("# 2. Ver datos")
        print("# 3. Salir")
        print("#################################")
        opc =libreria.pedir_numero("Ingrese la opcion: ", 1, 3)
        if( opc == 1):
            agregrrr()
        if( opc == 2):
            ver_datos()

opc=0
max=3
while( opc!= max ):
    print("####### AGENCIA DE VIAJE #####")
    print("# 1. agregar destino nacional")
    print("# 2. agregar destino internacional")
    print("# 3. Salir         ")
    print("##########################")

    opc =libreria.pedir_numero("Ingrese su opcion: ", 1, 3 )

    if( opc == 1 ):
        opcion_1()

    if( opc == 2 ):
        opcion_2()


print("fin del programa")

