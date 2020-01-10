import libreria


def agregaranimal():
    animal_silvestre=libreria.pedir_animal("ingrese animal:")
    cont=libreria.pedir_continente("ingrese continente de origen:")
    contenido=animal_silvestre + "-" + str(cont) + "\n"
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
    print("1. Agregar animal")
    print("2. ver Datos")
    print("3. Salir")
    print("#####################")

    opc=libreria.pedir_numero("Ingresar Opcion:", 1, 3)

    if (opc == 1):
        agregaranimal()

    if (opc == 2):
        verDatos()


#fin_menu
print("Fin del programa")
