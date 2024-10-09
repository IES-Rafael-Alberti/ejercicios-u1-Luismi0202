#Ejercicio 1.2.17
#Escribir un programa que pregunte el nombre del usuario en la consola y un número entero e imprima por pantalla en líneas distintas el nombre del usuario tantas veces como el número introducido.

print ("DAME TU NOMBRE Y HARE MAGIA CON ÉL...")
nombre = input()
print ("FALTA UNA COSA MÁS... DAME UN NÚMERO ENTERO...")
num = int(input())
for i in range(1,num + 1):
    print(nombre)