#Laboratorio de pensamiento computacional, seccion 17
#19/09/2023
#Daniel Maldonado
#Objetivo: 
#Entrada: 
#Proceso: 
#Salida: 

#Menu de opciones

opcion=""
num=0
conta=1
while opcion!="3":
    print("1.Factorial")
    print("2.Secuencia de Fibonacci")
    print("3.Salir")
    opcion=input("Ingrese la opcion: ")
    
    if opcion=="1":
        print("Selecciono factorial")
        num=int(input("Ingrese el numero:"))
        print("Vamos a mostrar el factorial de: ", num)
        
        while conta <= num:
            print(num, "*",conta)
            conta=conta + 1
    
    elif opcion=="2":
        print("Selecciono Secuencia de Fibonacci")
        num=int(input("Ingrese el numero: "))
        secuencia="fibonacci"(num)
    elif opcion=="3":
        print("Hasta pronto")