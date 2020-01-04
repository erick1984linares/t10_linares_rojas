import libreria
#1
assert(libreria.validar_continente("asia")==True)
assert(libreria.validar_continente("america")==True)
assert(libreria.validar_continente("africa")==True)
assert(libreria.validar_continente("a")==False)
print("validar continente OK")

#2
assert(libreria.validar_sexo("Masculino")==True)
assert(libreria.validar_sexo("Femenino")==True)
assert(libreria.validar_sexo("hola")==False)
print("Validar sexo OK")

#3
assert(libreria.validar_pais("peru")==True)
print("validar pais OK")

#4
assert(libreria.validar_universidad("universidad nacional pedro ruiz gallo")==True)
assert(libreria.validar_universidad("")==False)
assert(libreria.validar_universidad("hola")==False)
print("validar universidad OK")

#5
assert(libreria.validar_region("Lambayeque")==True)
assert(libreria.validar_region("Lamb")==False)
assert(libreria.validar_region("")==False)
print("Validar region OK")

#7
assert(libreria.validar_entero("m") == False)
assert(libreria.validar_entero("6") == False)
assert(libreria.validar_entero(10) == True)
print("validar_entero OK")

#8
assert (libreria.validar_rango(2, 1, 5) == True)
assert (libreria.validar_rango(4, 1, 5) == True)
assert (libreria.validar_rango(6, 1, 5) == False)
print("validar_rango ok")

#9
assert (libreria.validar_nombre("0") == False)
assert (libreria.validar_nombre("12") == False)
assert (libreria.validar_nombre("pedro") == True)
print("validar_nombre OK")

#10
assert (libreria.validar_celular("Samsung")==True)
assert (libreria.validar_celular("Iphone")==True)
assert (libreria.validar_celular("sangun")==False)
assert (libreria.validar_celular("hola")==False)
print("validar celular OK")

#11
assert (libreria.validar_guerras("1era guerra mundial")==True)
assert (libreria.validar_guerras("2da guerra mundial")==True)
assert (libreria.validar_guerras("1 guerra mundial")==False)
print("validar guerras OK")

#12
assert (libreria.validar_paises_involucrados("ESTADOS UNIDOS")==True)
assert (libreria.validar_paises_involucrados("RUSIA")==True)
assert (libreria.validar_paises_involucrados("INGLATERRA")==True)
assert (libreria.validar_paises_involucrados("HOLA")==False)
print("validar involucrados OK")

#13
assert (libreria.validar_curso("programacion 1")==True)
assert (libreria.validar_curso("tecnicas")==True)
assert (libreria.validar_curso("abcd")==False)
print("validar curso OK")

#14
assert (libreria.validar_trabajo("docente")==True)
assert (libreria.validar_trabajo("ingeniero")==True)
assert (libreria.validar_trabajo("abd")==False)
print("Validar trabajo OK")

#15
assert (libreria.validar_telefono("987654321")==True)
print("validar telefono OK")

#16
assert (libreria.validar_departamento("lambayeque")==True)
assert (libreria.validar_departamento("Ica")==True)
assert (libreria.validar_departamento("ab")==False)
print("validar dep OK")

#17
assert (libreria.validar_maravilla_del_mundo("Machu Picchu")==True)
assert (libreria.validar_maravilla_del_mundo("Taj mahal")==True)
assert (libreria.validar_maravilla_del_mundo("hola")==False)
assert (libreria.validar_maravilla_del_mundo("la antartida")==False)
print("validar maravilla OK")

#18
assert (libreria.validar_paises_de_las_maravillas("Perú")==True)
assert (libreria.validar_paises_de_las_maravillas("Brazil")==True)
assert (libreria.validar_paises_de_las_maravillas("EUA")==False)
assert (libreria.validar_paises_de_las_maravillas("Rusia")==False)
print("validar paises de las maravllas OK")

#19
assert (libreria.validar_cantante("Katy Perry")==True)
assert (libreria.validar_cantante("Maluma")==True)
assert (libreria.validar_cantante("Marisol")==False)
assert (libreria.validar_cantante("ABCED")==False)
print("validar cantante OK")

#20
assert (libreria.validar_pais_de_origen("Estados Unidos")==True)
assert (libreria.validar_pais_de_origen("Colombia")==True)
assert (libreria.validar_pais_de_origen("Rusia")==False)
print("validar pais de origen OK")

#21
assert (libreria.validar_red_social("Facebook")==True)
assert (libreria.validar_red_social("Twitter")==True)
assert (libreria.validar_red_social("Instagram")==True)
print("validar red social OK")

#22
assert (libreria.validar_dni("73461321")==True)
assert (libreria.validar_dni(3461321)==False)
assert (libreria.validar_dni(61321)==False)
print("Validar dni OK")
#
opc=libreria.pedir_numero("Ingrese num:", 1, 3)
assert (libreria.validar_rango(opc, 1, 3) == True)
print("pedir_numero OK")

#
assert (libreria.validar_nota(-10)==False)
assert (libreria.validar_nota(0)==True)
assert (libreria.validar_nota(20)==True)
print("validar nota OK")

print("validar_nota -> OK")




