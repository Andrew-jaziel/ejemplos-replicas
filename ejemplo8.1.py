#Se desea eliminar los blancos de una frase dada terminada en un punto. Se supone que es posible leer los caracteres 
#de la frase de uno en uno.

cadena= str(input("Digite la cadena con espacios\n"))

for elemento in cadena:
    if elemento != " ":
        print(elemento, end="")