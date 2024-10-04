#Ejercicio 1.2.2
#Escribe un programa para pedirle al usuario las horas de trabajo y el precio por hora y calcule el importe total del servicio.
def importe(horas,costes):
    return f"El importe total es {horas + costes}" 
def main():
    print("Introduce las horas")
    horas = int(input())
    print("Introduce los costes")
    costes = int(input())
    print(importe(horas,costes))
if __name__ == "__main__":
    main()