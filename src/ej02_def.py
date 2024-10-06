#ej02 => recibe horas y coste y retorna el importe total.

#función llamada importe que recibe horas y costes
def importe(horas,costes):
    #devuelve a importe(horas,costes) el valor de horas + costes y una serie de caracteres
    return f"El importe total es {horas + costes}" 
def main():
    print("Introduce las horas")
    horas = int(input())
    print("Introduce los costes")
    costes = int(input())
    #imprime la función con su resultado
    print(importe(horas,costes))
if __name__ == "__main__":
    main()