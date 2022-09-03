#Contar el número de letras “i” de una frase terminada en un punto. 
#Se supone que las letras pueden leerse independientemente.

frase = str(input("Digite la frase\n"))

print("Número de letras I:", frase.count("i")+frase.count("I"))
