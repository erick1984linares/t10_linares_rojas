import libreria

def agregarSexo():
    sexo=libreria.pedir_sexo("ingrese sexo:")
    nombre=libreria.pedir_nombre("ingrese nombre:")
    nombre_del_pais=libreria.pedir_pais("ingrese nombre del pais:")
    contenido=sexo + "-" + str(nombre) + "-" + str(nombre_del_pais) + "\n"
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
    print("1. agregar sexo")
    print("2. ver datos")
    print("3. Salir")
    print("#####################")

    opc=libreria.pedir_numero("Ingresar Opcion:", 1, 3)

    if (opc == 1):
        agregarSexo()

    if (opc == 2):
        verDatos()


#fin_menu
print("Fin del programa")
