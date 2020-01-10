from Rojas import libreria

def agregar_idioma():
    agregado=libreria.pedir_idioma("Ingrese el idioma a aprender: ")
    contenido="-"+agregado+"\n"
    libreria.guardar_datos("lista.txt",contenido,"a")
    print("idioma agregado a su lista")

def mostrar_idos_slec():
    verr=libreria.obtener_datos("lista.txt")
    print("Los idiomas que usted ha seleccionado son: ")
    print("------------------------------------------")
    print(verr)

oppcn=0
limit=3
while (oppcn != limit):
    print("########################")
    print("#   CENTRO DE IDIOMAS  #")
    print("########################")
    print("# 1. Agregar idioma    #")
    print("# 2. Ver disponibles   #")
    print("# 3. Ver agregados     #")
    print("# 4. Salir             #")
    print("########################")

    oppcn=libreria.pedir_numero("Ingrese la opcion deseada: ",1,3)
    if (oppcn == 1):
        agregar_idioma()

    if (oppcn == 2):
        print(" **Los idiomas disponibles en el centro son los siguientes:**")
        print(" * Ingles   - Aleman")
        print(" * Italiano - Chino")
        print(" * Frances  - Coreano")
        print(" * Ruso     - Quechua")

    if (oppcn == 3):
        mostrar_idos_slec()

print("fin del programa")
