import libreria

def agregarcelular():
    celular=libreria.pedir_celular("Ingrese Marca del telefono:")
    pais=libreria.pedir_pais("Ingrese País de origen del telefono:")
    costo=libreria.pedir_numero("Ingrese costo del telefono:", 1000, 3000)
    contenido=celular + "-" + str(pais) + "-" + str(costo) + "\n"
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
    print("1. Agregar Celular")
    print("2. ver datos")
    print("3. Salir")
    print("#####################")

    opc=libreria.pedir_numero("Ingresar Opcion:", 1, 3)

    if (opc == 1):
        agregarcelular()

    if (opc == 2):
        verDatos()


#fin_menu
print("Fin del programa")

