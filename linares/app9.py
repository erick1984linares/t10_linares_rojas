import libreria

def agregarBytes():
    byte1=libreria.pedir_byte("Ingrese Byte 1:")
    byte2=libreria.pedir_byte("Ingrese Byte 2:")

    contenido=byte1 + "-" + byte2 + "\n"
    libreria.guardar_datos("bytes.txt", contenido, "a")
    print("Datos guardados")

def enmascarar():
    # 1. Abrir el archivo bytes.txt
    # 2. Mostrar los datos
    print("Byte 1       Byte2       Enmascamiento")
    datos=libreria.obtener_datos_lista("bytes.txt")
    # 3. Recorrer todos los elementos del archivo
    for linea in datos:
        linea = linea.replace("\n", "")
        byte1, byte2 = linea.split("-")
        mascara = libreria.enmascarar(byte1, byte2)
        print(byte1 + " - " + byte2 + " - " + mascara)

opc=0
max=3
while(opc != max):
    print("######### MENU #########")
    print("# 1. Agregar Bytes     #")
    print("# 2. Enmascarar        #")
    print("# 3. Salir             #")
    print("########################")
    opc=libreria.pedir_numero("Ingrese Opcion:", 1, 3)

    if ( opc == 1):
        agregarBytes()
    else:
        enmascarar()

#fin_menu
print("Programa finalizado")


