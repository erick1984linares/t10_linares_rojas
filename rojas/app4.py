from Rojas import libreria

def agragar_empres():
    empp=libreria.pedir_empresa("ingresar la empresa tecnologica:")
    contenido="> "+empp+"\n"
    libreria.guardar_datos("otralista.txt",contenido,"a")
    print("empresa agregada ")

def ver_empresas():
    al=libreria.obtener_datos("otralista.txt")
    if (al!=""):
        print(al)
    else:
        print("no hay datos")

oppcn=0
limit=3
while (oppcn != limit):
    print("########################")
    print("#         MENU         #")
    print("########################")
    print("# 1. Agregar empresa   #")
    print("# 2. Ver agregados     #")
    print("# 3. Salir             #")
    print("########################")

    oppcn=libreria.pedir_numero("Ingrese la opcion deseada: ",1,3)
    if (oppcn == 1):
        agragar_empres()

    if (oppcn == 2):
        ver_empresas()

print("fin del programa")
