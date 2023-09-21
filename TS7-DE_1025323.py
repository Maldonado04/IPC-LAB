#Pensamiento computacional, seccion 17
#20/09/2023
#Daniel Maldonado
#Objetivo: Aprender a usar el for
#Entrada: Numeros ingresados del 1 al 10
#Proceso: Pedir al usuario que seleccione una opcion
#Salida: Que se salga cuando el usuario quiere

print("Daniel Maldonado")

while True:
    num1= int(input("Ingrese un numero de 1 a 10"))

    if num1<=0:
        print("Error, ingrese un numero valido")

    if num1>=10:
        print("Error, ingrese un numero valido")

    else:
        for i in range (1, 11):
            print(num1, "x",i, "=", i*num1)

    num2= str(input("Si desea volver a las tablas, ingrese si o no"))
    if num2== "no":
        break