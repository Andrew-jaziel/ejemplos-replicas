#Leer un carácter y deducir si está situado antes o después de la letra “m” en orden alfabético.

caracter= str(input("Digite su caracter\n"))

if caracter < "m":
    print("El caracter va antes que la letra m")
elif caracter == "m":
    print("El caracter es m")
else:
    print("El caracter va después que la letra m")