n=int(input("Digite el numero de edades a evaluar para tomar el promedio: "))
x=1
promedio=0
while x <=n :
    edad=int(input("ingresa una edad: "))
    promedio=promedio+edad
    x += 1
    print("El promedio de edades de x numero es : ",edad,)