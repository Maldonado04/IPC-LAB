import Conversor

#Variables
opcion=1
menu=True

#Ciclo While para determinar lo que desea el usuario

while menu==True:
    print("Bienvenido al sistema de vonersión de centimetros a:metros, kilometros, pulgadas y pies")
    print("Que desea relizar?")
    print("1. Convertir centimetros a metros")
    print("2. Convertir centimetros a kilometros")
    print("3. Convertir centimetros a pulgadas")
    print("4. Convertir centimetros a pies")
    print("5. Salir")
    opcion = int(input("\nIngrese una opcion: "))
    if opcion == 1:
        cantidad = float(input("Ingrese la cantidad de centimetros que desea convertir a metros: "))
        metros = Conversor.centimetrosAmetros(cantidad)
        print("La cantidad de centimetros ingresada es igual a: ", metros, "metros")
    elif opcion == 2:
        cantidad = float(input("Ingrese la cantidad de centimetros que desea convertir a kilometros: "))
        kilometros = Conversor.centimetrosAkilometros(cantidad)
        print("La cantidad de centimetros ingresada es igual a: ", kilometros, "kilometros")
    elif opcion == 3:
        cantidad = float(input("Ingrese la cantidad de centimetros que desea convertir a pulgadas: "))
        pulgadas = Conversor.centimetrosApulgadas(cantidad)
        print("La cantidad de centimetros ingresada es igual a: ", pulgadas, "pulgadas")
    elif opcion == 4:
        cantidad = float(input("Ingrese la cantidad de centimetros que desea convertir a pies: "))
        pies = Conversor.centimetrosApies(cantidad)
        print("La cantidad de centimetros ingresada es igual a: ", pies, "pies")
    elif opcion == 5:
        print("Gracias por utilizar el sistema de conversion de centimetros a metros, kilometros, pulgadas y pies")
        menu = False
    else:
        print("Opcion invalida, por favor ingrese una opcion valida")
        menu=True