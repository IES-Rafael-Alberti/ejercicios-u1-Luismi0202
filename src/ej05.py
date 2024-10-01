#Ejercicio 1.2.5
#Escribe un programa que pida el importe sin IVA de un artículo y el tipo de IVA a aplicar y calcule e imprima por pantalla el precio final del artículo.

print("Dame el importe de un articulo")
precio = float(input())
print("¿Que tipo de IVA desea aplicar? GENERAL=1, REDUCIDO= 2, SUPERREDUCIDO=3")
tipo = int(input())
if(tipo==1):
    IVA= precio * 1.21
    print(f"El precio de su articulo con IVA es de {round(IVA,2)}€")
if(tipo==2):
    IVA= precio * 1.10
    print(f"El precio de su articulo con IVA es de {round(IVA,2)}€")
if(tipo==3):
    IVA= precio * 1.04
    print(f"El precio de su articulo con IVA es de {round(IVA,2)}€")
