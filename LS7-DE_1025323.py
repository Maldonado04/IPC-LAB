#Laboratorio de pensamiento computacional, seccion 17
#19/09/2023
#Daniel Maldonado
#Objetivo: Determinar con operaciones aritmeticas los datos ingresados
#Entrada: Numeros y operaciones aritmeticas
#Proceso: Uso de condicionales y ecuaciones aritmeticas
#Salida: Resultados de las operaciones
#Ejercicio 1: "operaciones aritmeticas"

d1= int(input("Ingrese un numero"))
d2= int(input("Ingrese otro numero"))

opcion=""
while opcion != "8":
    print("Menu de opciones")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicacion")
    print("4. Cociente")
    print("5. Division")
    print("6. Porcentaje")
    print("7. Exponente")
    print("8. Salir")
    opcion= input("Seleccione alguna opcion")
    if opcion == "1":
        print("Selecciono la suma")
        print(d1, "+", d2, "=", d1 + d2)
    elif opcion == "2":
        print("Selecciono la resta")
        print(d1, "-", d2, "=", d1 - d2)
    elif opcion == "3":
        print("Selecciono la multiplicacion")
        print(d1, "*", d2, "=", d1 * d2)
    elif opcion == "4":
        print("Selecciono el cociente")
        print(d1, "//", d2, "=", d1 // d2)
    elif opcion == "5":
        print("Selecciono la division")
        print(d1, "/", d2, "=", d1 / d2)
    elif opcion == "6":
        print("Selecciono el porcentaje")
        print(d1, "%", d2, "=", d1 % d2)
    elif opcion == "7":
        print("Selecciono la exponenciacion")
        print(d1, "**", d2, "=", d1 ** d2 )
    elif opcion == "8":
        print("Selecciono salir")
    
    else:
        print("ERROR, seleccione un numero valido")