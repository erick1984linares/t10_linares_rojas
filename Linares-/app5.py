import libreria


def agregarguerras():
    guerra=libreria.pedir_guerras("Ingrese guerra acontecida:")
    paises=libreria.pedir_paises_involucrados("Ingrese pais involucrado:")
    contenido=guerra + "-" + str(paises) + "\n"
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
    print("1. Agregar Guerras")
    print("2. ver datos")
    print("3. Salir")
    print("#####################")

    opc=libreria.pedir_numero("Ingresar Opcion:", 1, 3)

    if (opc == 1):
        agregarguerras()

    if (opc == 2):
        verDatos()


#fin_menu
print("Fin del programa")
