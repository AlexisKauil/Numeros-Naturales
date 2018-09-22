


#Operaciones con numeros naturales
#Alexis Eliseo Kauil Dzib

from operacion import *



while True:

    print("OPERACIONES CON NUMEROS NATURALES: ")
    print("Elige una opción: ")
    print("\t1 - Comenzar")
    print("\t2 - Finalizar")
    # solicituamos una opción al usuario

    opcionMenu = input("\ninserte de una opcion>> ")
    if opcionMenu=="1":
        numero = int(input("introduzca el valor del numero: "))
        numero2 = int(input("introduzca otro valor del numero, NOTA: este numero sera empleado para la suma y diferencia: "))
        prototipo = operaciones(numero, numero2)
        prototipo.verificar_cero()
        prototipo.sucesor()
        prototipo.escero()
        prototipo.igual()
        prototipo.suma()
        prototipo.antecesor()
        prototipo.diferencia()
        prototipo.menor()
        input("Pulsa una tecla para continuar")

    elif opcionMenu=="2":
        break
    else:
        print("")
        input("No has pulsado ninguna opción correcta...\npulsa una tecla para continuar")

