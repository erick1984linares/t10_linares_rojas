import libreria

def viaje_de_fin_de_ciclo():
    pais=libreria.pedir_pais("lugar a donde viajar:")
    precio_del_pasaje=libreria.pedir_numero("precios del pasaje en dolares:", 1500, 4000)
    ciclo=libreria.pedir_numero("ciclo:", 1, 10)
    contenido=pais + "-" + str(precio_del_pasaje) + "-" + str(ciclo) + "\n"
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
        print("######### VIAJE DE FIN DE CICLO ########")
        print("1. Viaje de fin de ciclo pais 1")
        print("2. Var datos")
        print("3. Salir")
        print("#######################")
        opc =libreria.pedir_numero("Ingrese subopcion: ", 1, 3)
        if( opc == 1):
            viaje_de_fin_de_ciclo()
        if( opc == 2):
            verDatos()
def opcionB():
    opc=0
    max=3
    while (opc!= max):
        print("######### VIAJE DE FIN DE CICLO ########")
        print("1. Viaje de fin de ciclo pais 2")
        print("2. Var datos")
        print("3. Salir")
        print("#######################")
        opc =libreria.pedir_numero("Ingrese subopcion: ", 1, 3)
        if( opc == 1):
            viaje_de_fin_de_ciclo()
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

