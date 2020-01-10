from Rojas import libreria



def agregrrr():
    nombre=libreria.pedir_nombre("nombre del CONTACTO: ")
    celular=libreria.pedir_cel("celular del contacto: ")
    contenido=str(nombre) + "-" + str(celular)+"\n"
    libreria.guardar_datos("contactos.txt", contenido, "a")
    print("Datos guardados")

def ver_datos():
    datos = libreria.obtener_datos("contactos.txt")
    if ( datos != ""):
        print("nombres --- numeros")
        print(datos)
    else:
        print("sin datos")

def opcion_1():
    opc=0
    max=3
    while (opc!= max):
        print("######### AGREGAR CONTACTO 1 ########")
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
        print("######### AGREGAR CONTACTO 2########")
        print("# 1. agregar ")
        print("# 2. Var datos")
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
    print("########### MENU #########")
    print("# 1. agregar contacto 1")
    print("# 2. agregar contacto 2")
    print("# 3. Salir         ")
    print("##########################")

    opc =libreria.pedir_numero("Ingrese su opcion: ", 1, 3 )

    if( opc == 1 ):
        opcion_1()

    if( opc == 2 ):
        opcion_2()


print("fin del programa")

