from Rojas import libreria

#creamos dos funciones para ingreasr y ver los datos
def anotacion():
    anont=input("Escriba su anotacion: ")
    contenido="- "+anont + "\n"
    libreria.guardar_datos("anotaciones.txt",contenido,"a")
    print("Anotacion agregada")

def ver_anotacion():
    verr=libreria.obtener_datos("anotaciones.txt")
    if (verr != ""):
        print(verr)
    else:
        print("No hay datos")

oppcn=0
limit=3
while (oppcn != limit):
    print("########################")
    print("#         MENU         #")
    print("########################")
    print("# 1. Agregar anotacion #")
    print("# 2. Ver agregados     #")
    print("# 3. Salir             #")
    print("########################")

    oppcn=libreria.pedir_numero("Ingrese la opcion deseada: ",1,3)
    #agregamos las opciones
    if (oppcn == 1):
        anotacion()

    if (oppcn == 2):
        ver_anotacion()

print("fin del programa")







