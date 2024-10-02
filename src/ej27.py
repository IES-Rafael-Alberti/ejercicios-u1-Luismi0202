#Ejercicio 1.2.27
#Escribir un programa que pregunte el nombre el un producto, su precio y un número de unidades y muestre por pantalla una cadena con el nombre del producto seguido de su precio unitario con 6 dígitos enteros y 2 decimales, el número de unidades con tres dígitos y el coste total con 8 dígitos enteros y 2 decimales.

print("Escribe el nombre del producto")
producto = input()
print("Escribe el precio del producto")
precio = float(input())
print("¿Cuántas unidades quiere?")
unidades = int(input())
coste = float(precio * unidades)
print(f"El nombre del producto es {producto} {precio:09.2f} {unidades: 003d} {coste: 011.2f} ")

