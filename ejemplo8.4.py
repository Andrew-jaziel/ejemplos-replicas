#Leer una letra. Deduce si está o no comprendida entre las letras mayúsculas I-M inclusive

letra = str(input("Digite la letra\n"))

if letra.upper() >= 'I' and letra.upper() <= 'M':
    print("Esta comprendida")
else:
    print("No esta comprendida")