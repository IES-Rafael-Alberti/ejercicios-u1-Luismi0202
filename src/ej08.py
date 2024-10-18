#Ejercicio 1.2.8
#Escribir el programa del ejercicio 1.7 usando solamente dos variables diferentes.

print ("Dame 3 números")
#Declaramos una variable temporal a 0 para que luego podamos realizar las sumas de los 3 inputs en un mismo bucle.
suma = 0
#Hacemos bucle para que nos pida 3 inputs. En el bucle siempre se suma 1 porque python resta siempre 1 al ultimo valor.
for i in range (1,3 + 1):
    num = float(input())
    num = suma + num
    suma = num 
print (f"¡¡MAGIA!! la suma de los 3 números es {round(suma,2)}")