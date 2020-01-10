from Rojas import libreria

def agregar_afiliado():
    nombre=libreria.pedir_nombre("Ingrese el nombre del afiliado:")
    dni=libreria.pedir_dni("Ingrese su dni: ")
    cel=str(libreria.pedir_cel("Ingrese su numero de celular: "))
    contenido=nombre+"-"dni+"-"cel
    libreria.guardar_datos("afiliados.txt",contenido,"a")
    print("datos guardados")

def ver_afiiliados():
    odof=libreria.obtener_datos("afiliados.txt")
    print(odof)


oppcn=0
limit=3
while (oppcn != limit):
    print("#########################")
    print("# PROGRAMA DE AFILIADOS #")
    print("#########################")
    print("# 1. Agregar afiliado   #")
    print("# 2. Ver agregados      #")
    print("# 3. Salir              #")
    print("#########################")

    oppcn=libreria.pedir_numero("Ingrese la opcion deseada: ",1,3)
    if (oppcn == 1):
        agregar_afiliado()

    if (oppcn == 2):
        ver_afiiliados()

print("fin del programa")
