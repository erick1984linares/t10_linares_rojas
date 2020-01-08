import libreria


def agregarcurso():
    curso=libreria.pedir_curso("Ingrese curso:")
    nombre_del_alumno=libreria.pedir_nombre("ingrese nombre del alumno:")
    promedio=libreria.pedir_numero("ingrese promedio:", 0, 20)
    creditos_del_curso=libreria.pedir_numero("ingrese creditos:", 1, 4)
    contenido=curso + "-" + nombre_del_alumno + "-" + str(promedio) + "-" + str(creditos_del_curso) + "\n"
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
    print("1. Agregar Curso")
    print("2. ver datos")
    print("3. Salir")
    print("#####################")

    opc=libreria.pedir_numero("Ingresar Opcion:", 1, 3)

    if (opc == 1):
        agregarcurso()

    if (opc == 2):
        verDatos()


#fin_menu
print("Fin del programa")
