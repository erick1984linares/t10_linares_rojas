from Rojas import libreria


def agregarrr():
    nombre=libreria.pedir_nombre("nombre de la persona: ")
    precio=libreria.pedir_numero("monto total: ", 10, 5000)
    categoria=libreria.pedir_clase("ingrese la categoria(aportante/deudor): ")
    contenido=str(precio) + "-" + str(nombre) +"-"+str(categoria)+ "\n"
    libreria.guardar_datos("datos.txt", contenido, "a")
    print("Datos guardados")

def ver_datos():
    datos = libreria.obtener_datos("datos.txt")
    if ( datos != ""):
        print(datos)
    else:
        print("sin datos")

def opcionA():
    opc=0
    max=3
    while (opc!= max):
        print("######### AGREGAR APORTANTE ########")
        print("# 1. agregar un aportante")
        print("# 2. Ver datos")
        print("# 3. Salir")
        print("####################################")
        opc =libreria.pedir_numero("Ingrese la opcion: ", 1, 3)
        if( opc == 1):
            agregarrr()
        if( opc == 2):
            ver_datos()
def opcionB():
    opc=0
    max=3
    while (opc!= max):
        print("######### AGREGAR DEUDOR ########")
        print("# 1. agregar un deudor")
        print("# 2. Var datos")
        print("# 3. Salir")
        print("#################################")
        opc =libreria.pedir_numero("Ingrese la opcion: ", 1, 3)
        if( opc == 1):
            agregarrr()
        if( opc == 2):
            ver_datos()

opc=0
max=3
while( opc!= max ):
    print("######### MENU ########")
    print("#---------------------#")
    print("# 1. Agregar aportantes")
    print("# 2. Agregar deudores  ")
    print("# 3. Salir")
    print("#######################")

    opc =libreria.pedir_numero("Ingrese opcion: ", 1, 3 )

    if( opc == 1 ):
        opcionA()
    if( opc == 2 ):
        opcionB()



print("fin del programa")

