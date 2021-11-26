myString = "Hello Mundo"
myString = "Erudito"
print (f"My name is {myString}") # CUANDO COLOCAMCIOSCOMBINAMOS UN +,-,*,/ ESTA SUMANDO RESTANDO  ETC

# NOS ENSEÑA QUE HACER CON ESTE TIPO DE DATOS
#print (dir(myString)) 
print (myString.upper()) # UPPER SE USA PARA CAMBIAR EL TEXTO EN MAYUSCULA
print (myString.lower()) # LOWER SE USA PARA CAMBIAR EL TEXTO EN MINUSCULA
print (myString.swapcase()) # SWAPCASE SE USA PARA CAMBIAR EL TEXTO PRIMERA LETRA MINUSCULA
print (myString.capitalize()) # CAPITALLAZE CAMBIA SOLO LA PRIMERA LETRA A MAYUSCULA
print (myString.replace("Hello", "Bye")) # REEMPLAZER 
print (myString.replace("Hello", "Bye").upper) # PONER EN MAYUSCULA EL REEMPLAZO
print (myString.count("l")) # CONTAR CUANTOS CARACTERES HAY 
print (myString.count(" ")) # CARACTER VACIO

print (myString.startswith("He")) # COMPROBAR CONQUE LETRA EMPIEZA EL TEXTO VERDADERO O FALSO
print (myString.endswith("Mundo")) # COMPRUEBA SI MI TEXTO TERMINA SI ES VERDADERO O FALSO
# SOLO FUNCIONA CON UN STRING

# DIVIDIR DATOS
print (myString.split()) #LO QUE HACE ESTE COMANDO SEPARA LOS DATOS O TEXTO BASADO EN UN SPACIO
print (myString.split(",")) # SEPARA APARTIR DE UNA COMA
print (myString.split("o")) # SEPARA APARTIR DE UNA LETRA
print (myString.find("o")) # BUSCA LA LETRA ATRAVEZ DE UNA POSICION POR SU INCICE
print (myString.find(" ")) # BUSCA ATRAVEZ DEL INDICE 

# EN LA SALIDA ME CRA UNA LISTA 

print(len(myString)) # VER LA LONGITUD DE LA CADENA DE TEXTO
print (myString.index("e")) # BUSCA EL INDICE
print (myString.isnumeric()) # SI MI CADENA DE TEXTO ES NUMERO
print(myString.isalpha()) # SI MI CADENA DE TEXTO ALFANUMERICO

print(myString[4]) #ME DEBUELVE EL VALOR DEL INCICE
print(myString[2])
print(myString[5])

print(myString[-1]) # LO INVERSO
print(myString[-2])
print(myString[-3]) 

# PARA COMENTAR UNA PARTE PRECIONAS CTRL+ SHIF + P -> COMENT

