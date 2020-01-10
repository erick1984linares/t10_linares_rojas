
def validar_entero(n):
    if (isinstance(n, int)):
        return True
    else:
        return False

def validar_rango(n, ri, rf):
    if ( validar_entero(n) == True):
        if (n >= ri and n <= rf):
            return True
        else:
            return False
    else:
        return False

def pedir_numero(msg, ri, rf):
    n=""
    while( validar_rango(n, ri, rf) == False):
       n=input(msg)
       if ( n.isdigit() == True):
           n = int(n)
    #fin_while
    return n
#fin_pedir_numero

def validar_nombre(nombre):
    if ( isinstance(nombre, str)):
        if (len(nombre) >= 3):
            return True
        else:
            return False
    else:
        return False

def pedir_nombre(msg):
    nombre=""
    while ( validar_nombre(nombre) == False ):
        nombre=input(msg)
    #fin_while
    return nombre
#fin_pedir_nombre

def guardar_datos(nombre_archivo, contenido, modo):
    archivo=open(nombre_archivo, modo)
    archivo.write(contenido)
    archivo.close()

def obtener_datos(nombre_archivo):
    archivo=open(nombre_archivo)
    contenido = archivo.read()
    archivo.close()
    return contenido

def obtener_datos_lista(nombre_archivo):
    archivo=open(nombre_archivo)
    lista = archivo.readlines()
    archivo.close()
    return lista

def pedir_nota(msg, ri, rf):
    n=""
    while( validar_rango(n, ri, rf) == False):
       n=input(msg)
       if ( n.isdigit() == True):
           n = int(n)
    #fin_while
    return n
def validar_continente(cont):
    if ( isinstance(cont, str)):
        if(len(cont) >= 4):
            return True
            if(cont=="asia" or cont=="africa" or cont=="america" or cont=="oceania" or cont=="europa"):
                return True
            else:
                return False
        else:
            return False
    else:
        return False

def pedir_continente(msg):
    cont=""
    while ( validar_continente(cont) == False ):
        cont=input(msg)
    #fin_while
    return cont
#fin_pedir_cont


def validar_sexo(sexo):
    if ( isinstance(sexo, str)):
        if(len(sexo) == 8 or len(sexo)==9):
            return True
            if(sexo=="Masculino" or sexo=="Femenino"):
                return True
            else:
                return False
        else:
            return False
    else:
        return False

def pedir_sexo(msg):
    sexo=""
    while ( validar_sexo(sexo) == False ):
        sexo=input(msg)
    #fin_while
    return sexo
#fin_pedir_cont


def validar_pais(pais):
    if ( isinstance(pais, str)):
        if(len(pais)>=4):
            return True
        else:
            return False
    else:
        return False

def pedir_pais(msg):
    pais=""
    while ( validar_pais(pais) == False ):
        pais=input(msg)
    #fin_while
    return pais
#fin_pedir_pais

def validar_universidad(uni):
    if ( isinstance(uni, str)):
        if(uni=="universidad nacional pedro ruiz gallo"):
            return True
        else:
            return False
    else:
        return False

def pedir_universidad(msg):
    uni=""
    while ( validar_universidad(uni) == False ):
        uni=input(msg)
    #fin_while
    return uni
#fin_pedir_uni

def validar_region(reg):
    if ( isinstance(reg, str)):
        if(reg=="Lambayeque"):
            return True
        else:
            return False
    else:
        return False

def pedir_region(msg):
    reg=""
    while ( validar_region(reg) == False ):
        reg=input(msg)
    #fin_while
    return reg
#fin_pedir_reg

def validar_celular(celular):
    if ( isinstance(celular, str)):
        if(celular=="Samsung" or celular=="Iphone" or celular=="LG" or celular=="Huawei"):
            return True
        else:
            return False
    else:
        return False

def pedir_celular(msg):
    celular=""
    while ( validar_celular(celular) == False ):
        celular=input(msg)
    #fin_while
    return celular
#fin_pedir_cel

def validar_guerras(guerras):
    if ( isinstance(guerras, str)):
        if(guerras=="1era guerra mundial" or guerras=="2da guerra mundial"):
            return True
        else:
            return False
    else:
        return False

def pedir_guerras(msg):
    guerras=""
    while ( validar_guerras(guerras) == False ):
        guerras=input(msg)
    #fin_while
    return guerras
#fin_pedir_guerras

def validar_paises_involucrados(involucrados):
    if ( isinstance(involucrados, str)):
        if(involucrados=="ESTADOS UNIDOS" or involucrados=="RUSIA" or involucrados=="INGLATERRA"
           or involucrados=="ALEMANIA" or involucrados=="ITALIA" or involucrados=="FRANCIA"):
            return True
        else:
            return False
    else:
        return False

def pedir_paises_involucrados(msg):
    involucrados=""
    while ( validar_paises_involucrados(involucrados) == False ):
        involucrados=input(msg)
    #fin_while
    return involucrados
#fin

def validar_curso(cur):
    if ( isinstance(cur, str)):
        if (cur=="programacion 1" or cur=="tecnicas" or cur=="quimica"):
            return True
        else:
            return False
    else:
        return False

def pedir_curso(msg):
    cur=""
    while ( validar_curso(cur) == False ):
        cur=input(msg)
    #fin_while
    return cur
#fin_pedir_curso

def validar_trabajo(trabajo):
    if ( isinstance(trabajo, str)):
        if (len(trabajo)>=5):
            return True
        else:
            return False
    else:
        return False

def pedir_trabajo(msg):
    trabajo=""
    while ( validar_trabajo(trabajo) == False ):
        trabajo=input(msg)
    #fin_while
    return trabajo
#fin_pedir_trabajo

def validar_animal(animal):
    if ( isinstance(animal, str)):
        if (animal=="jaguar" or animal=="guacamayo" or animal=="caiman" or animal=="aguila"):
            return True
            if (len(animal)>=5):
                return True
            else:
                return False
        else:
            return False
    else:
        return False

def pedir_animal(msg):
    animal=""
    while ( validar_animal(animal) == False ):
        animal=input(msg)
    #fin_while
    return animal
#fin_pedir_trabajo

def validar_telefono(tel):
    if(isinstance(tel, str)):
        if(len(tel)==9):
            return True
        else:
            return False
    else:
        return False
#fin
def pedir_telefono(msg):
    tel=""
    while(validar_telefono(tel)==False):
        tel=input(msg)
        #fin_while

#fin_def

def validar_departamento(dep):
    if ( isinstance(dep, str)):
        if (len(dep)>=3):
            return True
        else:
            return False
    else:
        return False

def pedir_departamento(msg):
    dep=""
    while ( validar_departamento(dep) == False ):
        dep=input(msg)
    #fin_while
    return dep
#fin_pedir_trabajo

def validar_maravilla_del_mundo(maravilla):
    if ( isinstance(maravilla, str)):
        if (maravilla=="Machu Picchu" or maravilla=="Chichen Itza" or maravilla=="Coliseo Romano"
                or maravilla=="Cristo Redentor" or maravilla=="La gran muralla China" or maravilla=="Petra"
                or maravilla=="Taj mahal"):
            return True
        else:
            return False
    else:
        return False

def pedir_maravilla(msg):
    maravilla=""
    while ( validar_maravilla_del_mundo(maravilla) == False ):
        maravilla=input(msg)
    #fin_while
    return maravilla
#fin_pedir_trabajo

def validar_paises_de_las_maravillas(pais):
    if ( isinstance(pais, str)):
        if (pais=="Perú" or pais=="China" or pais=="Roma" or pais=="Jordania"
                or pais=="India" or pais=="Mexico" or pais=="Brazil"):
            return True
        else:
            return False
    else:
        return False

def pedir_pais_de_mara(msg):
    pais=""
    while ( validar_paises_de_las_maravillas(pais) == False ):
        pais=input(msg)
    #fin_while
    return pais
#fin_pedir_trabajo

def validar_cantante(cantante):
    if ( isinstance(cantante, str)):
        if (cantante=="J Balvin" or cantante=="Katy Perry" or cantante=="Maluma" or cantante=="Taylor Swift"):
            return True
        else:
            return False
    else:
        return False

def pedir_cantante(msg):
    cantante=""
    while ( validar_cantante(cantante) == False ):
        cantante=input(msg)
    #fin_while
    return cantante
#fin_pedir_curso

def validar_pais_de_origen(pais):
    if ( isinstance(pais, str)):
        if (pais=="Colombia" or pais=="Estados Unidos"):
            return True
        else:
            return False
    else:
        return False

def pedir_pais_de_origen(msg):
    pais=""
    while ( validar_pais_de_origen(pais) == False ):
        pais=input(msg)
    #fin_while
    return pais
#fin_pedir_curso
def validar_red_social(red):
    if ( isinstance(red, str)):
        if (red=="Facebook" or red=="Twitter" or red=="Instagram"):
            return True
        else:
            return False
    else:
        return False

def pedir_red_social(msg):
    red=""
    while ( validar_red_social(red) == False ):
        red=input(msg)
    #fin_while
    return red
#fin_pedir_curso

def validar_dni(dni):
    if(isinstance(dni, str)):
        if(len(dni)==8):
            return True
        else:
            return False
    else:
        return False
#fin
def pedir_dni(msg):
    dni=""
    while(validar_dni(dni)==False):
        dni=input(msg)
        #fin_while
        return dni



def validar_byte(byte):
    # 1. Ocupa 8 caracteres
    if ( len(byte) != 8):
        return False

    # 2. La cadena debe ser digitos
    if ( byte.isdigit() == False ):
        return False

    # 3. Cada caracter debe ser 0 o 1
    for bit in byte:
        if ( bit != "0" and bit != "1" ):
            return False
        #fin_if
    #fin_for

    # Si llego hasta aqui, es porque es un Byte correcto
    return True
#fin_validar_byte

def pedir_byte(msg):
    byte=""
    while( validar_byte(byte) == False):
        byte=input(msg)
    return byte
#fin_pedir_byte

def mascara(bit1, bit2):
    if ( bit1 == "1" and bit2 == "1" ):
        return "1"
    else:
        return "0"

def enmascarar(byte1, byte2):
    mask=""
    for i in range(8):
        mask += mascara(byte1[i], byte2[i])
    #fin_for
    return mask
