#Ejercicio 1.2.6¶
#Escribe un programa que pida el importe final de un artículo y calcule e imprima por pantalla el IVA que se ha pagado y el importe sin IVA (suponiendo que se ha aplicado un tipo de IVA del 10%).

print("Dame el importe final de un articulo")
precio = float(input())
IVA= precio * 0.10
SINIVA= precio - IVA
print(f"El precio de su articulo sin IVA es de {SINIVA} y el iva pagado es {IVA}€")

