from Rojas import libreria

def agregar_marca():
    marca=libreria.pedir_marca("Ingrese la marca de zapatilla deseada:")
    talla=str(libreria.pedir_numero("Ingrese la talla deseada: ",33,45))
    contenn=marca+"-"+talla+"\n"
    libreria.guardar_datos("zapatillas.txt",contenn,"a")
    print("datos agregados")

def ver_maraca():
    okis=libreria.obtener_datos("zapatillas.txt")
    print(okis)

oppcn=0
limit=3
while (oppcn != limit):
    print("########################")
    print("#         MENU         #")
    print("########################")
    print("# 1. Agregar marca     #")
    print("# 2. Ver los agregados #")
    print("# 3. Salir             #")
    print("########################")

    oppcn=libreria.pedir_numero("Ingrese la opcion deseada: ",1,3)
    if (oppcn == 1):
        agregar_marca()

    if (oppcn == 2):
        ver_maraca()

print("fin del programa")
