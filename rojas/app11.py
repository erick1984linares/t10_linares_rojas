from Rojas import libreria

def ingresr_product():
    color=libreria.pedir_color("ingrese el color del producto: ")
    precio=str(libreria.pedir_numero("ingrese el precio: ",50,400))
    contenido=color+"-"+precio+"\n"
    libreria.guardar_datos("productos.txt",contenido,"a")
    print("datos guardados")

def ver_product():
    gigig=libreria.obtener_datos("productos.txt")
    print(gigig)


def primer_opc():
  opx=0
  max=3
  while (opx != max):
        print("#######################")
        print("#       PANTALON      #")
        print("#######################")
        print("# 1. Elegir pantalon  #")
        print("# 2. Ver compra       #")
        print("# 3. Salir            #")
        print("#######################")

        opx=libreria.pedir_numero("Ingrese la opcion deseada: ",1,3)
        if (opx == 1):
            ingresr_product()


        if (opx == 2):
            ver_product()




def segund_opc():
  opx=0
  max=3
  while (opx != max):
        print("########################")
        print("#        POLOS         #")
        print("########################")
        print("# 1. Elegir polo       #")
        print("# 2. Ver compra        #")
        print("# 3. Salir             #")
        print("########################")

        opx=libreria.pedir_numero("Ingrese la opcion deseada: ",1,3)
        if (opx == 1):
            ingresr_product()


        if (opx == 2):
            ver_product()


#menu principal
limit=3
oppcn=0
while (oppcn != limit):
    print("########################")
    print("#         MENU         #")
    print("########################")
    print("# 1. Comprar pantalon  #")
    print("# 2. comprar polo      #")
    print("# 3. Salir             #")
    print("########################")

    oppcn=libreria.pedir_numero("Ingrese la opcion deseada: ",1,3)
    if (oppcn == 1):
        primer_opc()


    if (oppcn == 2):
        segund_opc()


print("fin del programa")
