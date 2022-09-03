#Leer dos caracteres y deducir si están en orden alfabético.

caracter1 = str(input("Primer caracter\n"))
caracter2 = str(input("Segundo caracter\n"))

if caracter1 <= caracter2:
    print("Estas en orden")
else:
    print("Están en desorden")