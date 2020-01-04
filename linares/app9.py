import libreria

def agregarNota():
    nombre = libreria.pedir_nombre("Ingrese nombre del alumno:")
    nota = libreria.pedir_nota("Ingrese nota:", 1, 20)
    contenido=nombre + "-" + str(nota) + "\n"
    libreria.guardar_datos("info.txt", contenido, "a")
    print("Datos y nota del alumno Guardados")

def verificarNota():
    datos = libreria.obtener_datos("info.txt")
    if ( datos != ""):
        print(datos)
    else:
        print("Archivo sin datos")

opc=0
max=3
while(opc != max):
    print("######## MENU #######")
    print("1. Agregar nota")
    print("2. Verificar datos del Alumno")
    print("3. Salir")
    print("#####################")

    opc=libreria.pedir_numero("Ingresar Opcion:", 1, 3)

    if (opc == 1):
        agregarNota()
    if (opc == 2):
        verificarNota()

#fin_menu
print("Fin del programa")
