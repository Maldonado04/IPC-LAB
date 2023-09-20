#Laboratorio de pensamiento computacional, seccion 17
#20/09/2023
#Daniel Maldonado
#Objetivo: Crear un programa que permita realizar operaciones aritmeticas basicas
#Entrada: Dos numeros enteros
#Salida: El resultado de la operacion aritmetica
#Ejericio 4: operaciones aritmeticas

#Creacion de las variables

num1 = 0
num2 = 0
menu=True
resultado = 0
opcion = 0

#Creacion del Menu

while menu==True:
    print("Ejericio 1: operaciones aritmeticas ") 
    print("Que opiacion desea realizar")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicacion")
    print("4. Division")
    print("5. Modulo")
    print("6. Exponienciacion")
    print("7. cociente")
    print("8. Salir")
    opcion = int(input("Ingrese la opcion: "))
    if opcion == 1:
        num1 = int(input("Ingrese el primer numero: "))
        num2 = int(input("Ingrese el segundo numero: "))
        resultado = num1 + num2
        print(num1, "+", num2, "=", resultado)
    
    if opcion == 2:
        num1 = int(input("Ingrese el primer numero: "))
        num2 = int(input("Ingrese el segundo numero: "))
        resultado = num1 - num2
        print(num1, "-", num2, "=", resultado)   
    
    if opcion == 3:
        num1 = int(input("Ingrese el primer numero: "))
        num2 = int(input("Ingrese el segundo numero: "))
        resultado = num1 * num2
        print(num1, "*", num2, "=", resultado)
    
    if opcion == 4:
        num1 = int(input("Ingrese el primer numero: "))
        num2 = int(input("Ingrese el segundo numero: "))
        resultado = num1 / num2
        print(num1, "/", num2, "=", resultado)
    
    if opcion == 5:
        num1 = int(input("Ingrese el primer numero: "))
        num2 = int(input("Ingrese el segundo numero: "))
        resultado = num1 % num2
        print(num1, "%", num2, "=", resultado)
    
    if opcion == 6:
        num1 = int(input("Ingrese el primer numero: "))
        num2 = int(input("Ingrese el segundo numero: "))
        resultado = num1 ** num2
        print(num1, "**", num2, "=", resultado)
    
    if opcion == 7:
        num1 = int(input("Ingrese el primer numero: "))
        num2 = int(input("Ingrese el segundo numero: "))
        resultado = num1 // num2
        print(num1, "//", num2, "=", resultado)
    
    if opcion == 8:
        menu=False
        print("Gracias por usar el programa")
