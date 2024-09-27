#Ejercicio 1.2.12
#Escribir un programa que pida al usuario su peso (en kg) y estatura (en metros), calcule el índice de masa corporal y lo almacene en una variable, y muestre por pantalla la frase Tu índice de masa corporal es donde es el índice de masa corporal calculado redondeado con dos decimales.

print ("¿Cuántos kg pesas?")
peso = float(input())
print ("¿Cuánto metros mides?")
altura = float(input())
IMC = peso / altura **2
RESULTADO = round(IMC, 3)
print (f"pesas {peso}, mides {altura} y su IMC es {RESULTADO}")