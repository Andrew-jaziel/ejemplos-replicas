while True :
    cuenta=1000
    print("***Menu Principal***")
    print("1.retiro")
    print("2.agregar saldo")
    print("3.mostrar cuenta")
    print("4.exit")
    opc=input("ingrese una opcion: ")
    
    if opc=="1":
        salida=int(input("Digite el monto a retirar: "))
        total=cuenta-salida
        print("El monto que retiro es: ",salida,)
    elif opc=="2":
        agregar=int(input("Ingrese el monto a agregar: "))
        total=cuenta+agregar

    elif opc=="3":
         print("EL saldo de la cuenta es de: ",total)
    else: 
         print("salida")

