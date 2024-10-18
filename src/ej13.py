#Ejercicio 1.2.13
#Escribir un programa que pida al usuario dos números enteros y muestre por pantalla los siguienteS: "la división de n entre m da un cociente c y un resto r", donde n y m son los números introducidos por el usuario, y c y r son el cociente y el resto de la división entera respectivamente.

print ("Dame dos números")
n = int(input())
m = int(input())
cociente = n // m
resto = n % m
print(f"la división entre {n} y {m} da un cociente {cociente} y un resto {resto}")