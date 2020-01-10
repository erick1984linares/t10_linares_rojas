import libreria


def Maravillas_de_mundo_en_america():
    paisdelamaravilla=libreria.pedir_pais_de_mara("Pais de america donde se encuentra la maravilla:")
    nombredelamaravilla=libreria.pedir_maravilla("Nombre de la maravilla:")
    contienente_donde_se_encuentre=libreria.pedir_continente("ingrese nombre de continente:")
    contenido=paisdelamaravilla + "-" + str(nombredelamaravilla) + "-" + contienente_donde_se_encuentre + "\n"
    libreria.guardar_datos("info.txt", contenido, "a")
    print("Datos guardados")

def Maravillas_del_mundo():
    paisdelamaravilla=libreria.pedir_pais_de_mara("Pais donde se encuentra la maravilla:")
    nombredelamaravilla=libreria.pedir_maravilla("Nombre de la maravilla:")
    contienente_donde_se_encuentre=libreria.pedir_continente("ingrese nombre de continente:")
    contenido=paisdelamaravilla + "-" + str(nombredelamaravilla) + "-" + contienente_donde_se_encuentre + "\n"
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
        print("######### maravillas del mundo moderno en america ########")
        print("1. Maravillas de mundo")
        print("2. Var datos")
        print("3. Salir")
        print("#######################")
        opc =libreria.pedir_numero("Ingrese subopcion: ", 1, 3)
        if( opc == 1):
            Maravillas_de_mundo_en_america()
        if( opc == 2):
            verDatos()

def opcionB():
    opc=0
    max=3
    while (opc!= max):
        print("######### maravillas del mundo moderno ########")
        print("1. Maravillas de mundo")
        print("2. Var datos")
        print("3. Salir")
        print("#######################")
        opc =libreria.pedir_numero("Ingrese subopcion: ", 1, 3)
        if( opc == 1):
            Maravillas_del_mundo()
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

