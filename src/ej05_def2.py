#ej05 => recibe el importe del artículo sin iva y el tipo de iva a aplicar, pero no retorna nada, sino que se imprime desde dentro de la función.
def calcula_precio(importe,IVA):
    if(IVA==1):
        IVA= importe * 1.21
        print(f"El precio de su articulo con IVA es de {round(IVA,2)}€")
    if(IVA==2):
        IVA= importe * 1.10
        print(f"El precio de su articulo con IVA es de {round(IVA,2)}€")
    if(IVA==3):
        IVA= importe * 1.04
        print(f"El precio de su articulo con IVA es de {round(IVA,2)}€")
def main():
    print("Dame el importe de un articulo")
    importe = float(input())
    print("¿Que tipo de IVA desea aplicar? GENERAL=1, REDUCIDO= 2, SUPERREDUCIDO=3")
    IVA = int(input())
    #llamada a la función
    calcula_precio(importe,IVA)    
if __name__ == "__main__":
    main()