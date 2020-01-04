import libreria

def agregarcont():
    continente=libreria.pedir_continente("ingrese continente:")
    nombre_del_turista=libreria.pedir_nombre("ingrese nombre del turista:")
    contenido=continente + "-" + str(nombre_del_turista) + "\n"
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
    print("1. Agregar continente")
    print("2. ver Datos")
    print("3. Salir")
    print("#####################")

    opc=libreria.pedir_numero("Ingresar Opcion:", 1, 3)

    if (opc == 1):
        agregarcont()

    if (opc == 2):
        verDatos()


#fin_menu
print("Fin del programa")

