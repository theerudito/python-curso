# LOS ES UNA COLECION DE DATOS QUE NO TIENE INDICE
colors = {"Red","Green","Blue"}
print (colors)
print(type(colors))

print("Red" in colors) # COMPRUEBA SI ESTA ESE COLORS

colors.add("violet")  # AGREGAR ELEMENTOS
print(colors)

colors.remove("violet") # REMUEVE UN ELEMENTO
print(colors)

colors.clear() # LIMPIA TODA LA SET
print(colors)