from src.ej05_def2 import calcula_precio

def ej05prueba_1():
    assert calcula_precio(7,1) == "El precio de su articulo con IVA es de 8.47€"
def ej05prueba_2():
    assert calcula_precio(7,2) == "El precio de su articulo con IVA es de 7.7€"
def ej05prueba_3():
    assert calcula_precio(7,3) == "El precio de su articulo con IVA es de 7.28€"