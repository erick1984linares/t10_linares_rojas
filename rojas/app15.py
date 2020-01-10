from Rojas import libreria



def agregrrr():
    nombre=libreria.pedir_nombre("nombre del estudiante: ")
    dni=libreria.pedir_dni("ingrese su dni: ")
    celular=libreria.pedir_cel("ingrese su numero celular: ")
    contenido=str(nombre) + "-" + dni+"-"+str(celular)+"\n"
    libreria.guardar_datos("estudintees.txt", contenido, "a")
    print("Datos guardados")

def ver_datos():
    datos = libreria.obtener_datos("estudintees.txt")
    if ( datos != ""):
        print("nombre----dni-----celular")
        print(datos)
    else:
        print("sin datos")

def opcion_1():
    opc=0
    max=3
    while (opc!= max):
        print("######### AGREGAR ESTUDIANTE 1 ########")
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
        print("######### AGREGAR ESTUDIANTE 2########")
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
    print("##########################")
    print("#          MENU          #")
    print("##########################")
    print("# 1. agregar estudiante 1")
    print("# 2. agregar estudiante 2")
    print("# 3. Salir         ")
    print("##########################")

    opc =libreria.pedir_numero("Ingrese su opcion: ", 1, 3 )

    if( opc == 1 ):
        opcion_1()

    if( opc == 2 ):
        opcion_2()


print("fin del programa")

