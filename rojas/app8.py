from Rojas import libreria

def agregar_libro():
    libro=libreria.pedir_nombre("Agregar el nombre del libro: ")
    autor=libreria.pedir_nombre("Agregar el nombre del autor(a): ")
    neto=libro+"-"+autor+"\n"
    libreria.guardar_datos("libros.txt",neto,"a")
    print("contenido agregado")

def ber_libros():
    vovo=libreria.obtener_datos("libros.txt")
    print(vovo)

oppcn=0
limit=3
while (oppcn != limit):
    print("########################")
    print("#        LIBROS        #")
    print("########################")
    print("# 1. Agregar libro     #")
    print("# 2. Ver agregados     #")
    print("# 3. Salir             #")
    print("########################")

    oppcn=libreria.pedir_numero("Ingrese la opcion deseada: ",1,3)
    if (oppcn == 1):
        agregar_libro()

    if (oppcn == 2):
        ber_libros()

print("fin del programa")
