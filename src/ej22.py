#Ejercicio 1.2.22
#Escribir un programa que pida al usuario que introduzca una frase en la consola y una vocal, y después muestre por pantalla la misma frase pero con la vocal introducida en mayúscula.

#Creamos esta variable para usarla ahora más adelante...
vocales = "aeiou"
#Variable para crear bucle while y luego cerrar este mismo
X=0
print ("Dame una frase:")
frase= input()
while (X==0):
    print("Dame una vocal en minúscula")
    vocal = input()
    #Y aquí es donde entra nuestra querida variable creada al inicio. Comprobaremos con un condicional que la vocal introducida sea aeiou en minúsculas para eso usamos este comando...
    if vocal in vocales:
        #Si es vocal minúscula sale del bucle de lo contrario no.
        X=1
    else:
        print("ERROR, ESCIBE UNA VOCAL EN MINÚSCULAS")
        X=0
        #Reemplazamos la vocal por la vocal que le hayamos dado en mayúsculas
print(f"{frase.replace(vocal, vocal.upper())}")