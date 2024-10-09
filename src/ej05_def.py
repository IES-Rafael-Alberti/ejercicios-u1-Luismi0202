#ej05 => recibe el importe del artículo sin iva y el tipo de iva a aplicar, pero no retorna nada, sino que se imprime desde dentro de la función.
def importe(precio,tipo):
    if(tipo==1):
        IVA= precio * 1.21
        print(f"El precio de su articulo con IVA es de {round(IVA,2)}€")
    if(tipo==2):
        IVA= precio * 1.10
        print(f"El precio de su articulo con IVA es de {round(IVA,2)}€")
    if(tipo==3):
        IVA= precio * 1.04
        print(f"El precio de su articulo con IVA es de {round(IVA,2)}€")
def main():
    print("Dame el importe de un articulo")
    precio = float(input())
    print("¿Que tipo de IVA desea aplicar? GENERAL=1, REDUCIDO= 2, SUPERREDUCIDO=3")
    tipo = int(input())
    #llamada a la función
    importe(precio,tipo)    
if __name__ == "__main__":
    main()