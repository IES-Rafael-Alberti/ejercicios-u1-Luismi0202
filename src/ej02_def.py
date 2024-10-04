#ej02 => recibe horas y coste y retorna el importe total.
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