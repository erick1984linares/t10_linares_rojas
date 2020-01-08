import libreria


def agregarUniversidad():
    universidad=libreria.pedir_universidad("ingrese universidad:")
    ciclo=libreria.pedir_numero("ingrese ciclo:", 1, 10)
    nombre_de_la_region=libreria.pedir_region("ingrese nombre de la region:")
    contenido=universidad + "-" + str(ciclo) + "-" + str(nombre_de_la_region) + "\n"
    libreria.guardar_datos("info.txt", contenido, "a")
    print("Datos guardados")

def verDatos():
    datos = libreria.obtener_datos("info.txt")
    if ( datos != ""):
        print(datos)
    else:
        print("Archivo sin datos")

opc=0
max=3
while(opc != max):
    print("######## MENU #######")
    print("1. agregar Uiversidad")
    print("2. ver datos")
    print("3. Salir")
    print("#####################")

    opc=libreria.pedir_numero("Ingresar Opcion:", 1, 3)

    if (opc == 1):
        agregarUniversidad()

    if (opc == 2):
        verDatos()


#fin_menu
print("Fin del programa")
