#ej11 => recibe un número y retorna una cadena de caracteres con el resultado de la función.

#recibe (num)
def resultado(num):
    suma = 0
    X=0
    while(X==0):
        if(num < 0 or num % 1 != 0):
            print("NO!! DAME UN ENTERO POSITIVO")
            #se vuelve a pedir input hasta que de entero positivo
            num = float(input())
            X=0
        else: 
            X=1
            num = int(num)
            for i in range(1, num + 1):
                suma=suma+i
            return f"LA SUMA DE LOS ENTEROS DE TU NÚMERO INTRODUCIDO ES DE {suma}"

def main():
    print("DAME UN NÚMERO ENTERO POSITIVO")
    num = float(input())
    #imprime la función resultado(num)
    print(resultado(num))

if __name__ == "__main__":
    main()