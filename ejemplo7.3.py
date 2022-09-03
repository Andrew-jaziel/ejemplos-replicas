from tkinter import N


alumnos =[]

lim = int(input("DIgite el numero de alumnos a evaluar: "))

for h in range(lim):
    print("Digite la altura segun el numero:  ",h+1, " : ")
    altura = float(input())
    alumnos.append(altura)

suma = 0
for i in alumnos: 
    suma = suma + i

mediaDeAltura = suma/lim

altos = 0
bajos = 0
x = 0

for x in alumnos:
    if x <= mediaDeAltura:
        bajos = bajos + 1
    elif x >= mediaDeAltura:
        altos = altos + 1

print("El promedio de la altura es: ", mediaDeAltura)
print("Los altos son: ", altos)
print("Los bajos son: ", bajos)