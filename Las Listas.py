# LAS LISTA VAN DENTRO DE CORCHETE Y CONTIENEN DATOS STRING ENTERO BOOLL FLOAR ETC

demoList = [1, "Hello", 1.3, True, [1,2,30]]
colors = ["Red","Yellow","Green"]

# CONSTRUCTOR ES UNA FUNCION QUE PERMITE LLAMAR UNA LISTA VAN DENTRO DE CORCHETE Y CONTI
numbersList = list((1,2,3,4)) # COLOCAR DENTRO COMO ITEM DE LA LISTA
print (numbersList) #LISTA
print (type(numbersList)) # TIPO DE DATO

# CRAR UNA LISTA APARTIR DE UN RANGO TOMA DOS DATOS DESDE DONDE HASTA DONDE
# Crear una lista del 1 al 10 me devuelve valor del 1 al 10 y me guarda en una variable 
r = list(range(1,100))
print(r)

# QUIERO OBTENER LA LISTA DE COLOR O TIPO DE DATOS DESDE
print(type(colors))
# TAMBIEN PUEDO EJECUTAR METODO PARA OBTENER DATOS DES
print(len(colors))
# CUANDO QUIERO OBTENER UN DATO ESPECIFICO
print(colors[1])
print(colors[-1])

# SABER SI HAY UN ELEMENTO EN UNA LISTAR
print("Green" in colors)

# REASIGNAR CAMBIA LOS DATOS EN UNA LISTA
print(colors)
colors[0] = "Blue"
print(colors)

print(dir(colors))
# AGREGA UN NUEVO ELEMENTO A LA LISTA
#colors.append("White")
colors.extend(("Violet", "Silver"))
print(colors)
# INSERTE UN NOMBRE EN UNA LISTA DEPENDIENDO DE LA POSICION
colors.insert(0, "White")
print(colors)
# REMOVER ELEMENTO DE UNA LISTA
print(colors)
colors.pop()
print(colors)
# CUANDO QUIERO QUIETAR UNA ELEMENTO
colors.remove("Violet")
print(colors)
# CUANDO QUIERO QUIETAR UN ELEMENTO APARTIR DE UN LIMITE
colors.pop(1)
print(colors)

# QUITAR TODOS LOS ELEMENTOS DE LA LISTAR
#colors.clear()
print(colors)

# ORDENAR ALFABETICAMENTE
colors.sort() #ORDENAR ALFAVETICAMENTE
colors.sort(reverse=True) #ORDENAR A LA INVERSA
print(colors)

# OBTENER EL INDICE DE COLORES
print(colors.index("Yellow"))

# CONTAR LOS COLORES QUE HAY REPETIDOS EN UNA LISTAR
print(colors.count("Yellow"))