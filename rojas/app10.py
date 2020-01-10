from Rojas import libreria

def agregar_concurante():
    concurante=libreria.pedir_nombre("Ingrese el nombre del concurante: ")
    puntuacion=str(libreria.pedir_numero("ingrese la puntuacion: ",1,10))
    cont=concurante+"-"+puntuacion
    libreria.guardar_datos("concurso.txt",cont,"a")
    print("datos guardados")

def ve_concurantes():
    fgg=libreria.obtener_datos("concurso.txt")
    print(fgg)

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
    if (oppcn == 1):
        agregar_concurante()

    if (oppcn == 2):
        ve_concurantes()

print("fin del programa")
