#Ejercicio 1.2.26
#Escribir un programa que pregunte por consola por los productos de una cesta de la compra, separados por comas, y muestre por pantalla cada uno de los productos en una línea distinta.

print("Dime los artículos de la cesta de la compra separados por coma")
cesta = input()
articulos = cesta.replace(",", "\n")
print(articulos)
