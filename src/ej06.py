print("Dame el importe final de un articulo")
precio = float(input())
IVA= precio * 0.10
SINIVA= precio - IVA
print(f"El precio de su articulo sin IVA es de {SINIVA} y el iva pagado es {IVA}€")

