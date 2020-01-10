from Rojas import libreria

def agregar_productos():
    nombre=libreria.pedir_nombre("Ingrese el nombre del prodcuto: ")
    precio=str(libreria.pedir_numero("Ingrese el precio del producto: ",0,1000))
    cont=nombre+"-"+precio+"\n"
    libreria.guardar_datos("products.txt",cont,"a")
    print("producto agrgado")

def ver_producto():
    aver=libreria.obtener_datos("products.txt")
    print(aver)

oppcn=0
limit=3
while (oppcn != limit):
    print("########################")
    print("#  LISTA DE PRODUCTOS  #")
    print("########################")
    print("# 1. Agregar productos #")
    print("# 2. Ver agregados     #")
    print("# 3. Salir             #")
    print("########################")

    oppcn=libreria.pedir_numero("Ingrese la opcion deseada: ",1,3)
    if (oppcn == 1):
        agregar_productos()

    if (oppcn == 2):
        ver_producto()

print("fin del programa")
