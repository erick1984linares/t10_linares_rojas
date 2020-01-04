import libreria

def los_canatantes_mas_famosos():
    nombre_de_cantante=libreria.pedir_cantante("Nombre del cantante:")
    pais_de_origen=libreria.pedir_pais_de_origen("Pais de origen:")
    sexo=libreria.pedir_sexo("Ingrese sexo:")
    contenido=nombre_de_cantante + "-" + pais_de_origen + "-" + sexo + "\n"
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
        print("######### Los cantantes mas famosos del mundo ########")
        print("1. Los cantantes mas famosos del mundo")
        print("2. Var datos")
        print("3. Salir")
        print("#######################")
        opc =libreria.pedir_numero("Ingrese subopcion: ", 1, 3)
        if( opc == 1):
            los_canatantes_mas_famosos()
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
    if( opc == 1 ):
        opcionB()

#fin

print("Fin del programa")

