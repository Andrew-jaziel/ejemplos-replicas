from tkinter import N


alumnos =[]

lim = int(input("Escribe el cuantos alumnos son: "))

for h in range(lim):
    print("Ingresa el la altura ",h+1, " : ")
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

print("La media de altura fué: ", mediaDeAltura)
print("Los alumnos altos son: ", altos)
print("Los alumnos bajos son: ", bajos)


