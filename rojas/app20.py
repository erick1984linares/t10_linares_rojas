from Rojas import libreria



def agregrrr():
    nombre=libreria.pedir_nombre("nombre del recordatorio: ")
    mensaje=input("ingrese el mensaje: ")
    contenido=str(nombre) + "->" + str(mensaje)+"\n"
    libreria.guardar_datos("reminders.txt", contenido, "a")
    print("Datos guardados")

def ver_info():
    datos = libreria.obtener_datos("reminders.txt")
    if ( datos != ""):
        print("nombre -- mensaje")
        print(datos)
    else:
        print("sin datos")

def opcion_1():
    opc=0
    max=3
    while (opc!= max):
        print("######### AGREGAR RECORDATORIO ########")
        print("# 1. agregar ")
        print("# 2. Ver datos")
        print("# 3. Salir")
        print("####################################")
        opc =libreria.pedir_numero("Ingrese la opcion: ", 1, 3)
        if( opc == 1):
            agregrrr()
        if( opc == 2):
            ver_info()
def opcion_2():
    opc=0
    max=3
    while (opc!= max):
        print("######### AGREGAR RECORDATORIO########")
        print("# 1. agregar ")
        print("# 2. Ver datos")
        print("# 3. Salir")
        print("#################################")
        opc =libreria.pedir_numero("Ingrese la opcion: ", 1, 3)
        if( opc == 1):
            agregrrr()
        if( opc == 2):
            ver_info()

opc=0
max=3
while( opc!= max ):
    print("####### RECORDATORIOS #####")
    print("# 1. agregar recordatorio 1")
    print("# 2. agregar recoradtorio 2")
    print("# 3. Salir         ")
    print("##########################")

    opc =libreria.pedir_numero("Ingrese su opcion: ", 1, 3 )

    if( opc == 1 ):
        opcion_1()

    if( opc == 2 ):
        opcion_2()


print("fin del programa")

