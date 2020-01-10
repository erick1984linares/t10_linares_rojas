from Rojas import libreria

def agregar_votante():
    nombre=libreria.pedir_nombre("ingrese nombre del votante: ")
    dni=libreria.pedir_dni("ingrese el dni: ")
    content=nombre+"-"+dni+"\n"
    libreria.guardar_datos("votantes.txt",content,"a")
    print("votante agregado")

def mostrar_votantes():
    ler=libreria.obtener_datos("votantes.txt")
    if (ler != ""):
        print(ler)
    else:
        print("no hay datos")


oppcn=0
limit=3
while (oppcn != limit):
    print("########################")
    print("#    ELECCIONES 2020   #")
    print("########################")
    print("# 1. Agregar votante   #")
    print("# 2. Ver agregados     #")
    print("# 3. Salir             #")
    print("########################")

    oppcn=libreria.pedir_numero("Ingrese la opcion deseada: ",1,3)
    if (oppcn == 1):
        agregar_votante()

    if (oppcn == 2):
        mostrar_votantes()

print("fin del programa")
