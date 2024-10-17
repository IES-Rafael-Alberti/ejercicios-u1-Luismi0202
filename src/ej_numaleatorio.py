#Ejercicio 1.2.29¶
#Cálculo de un número aleatorio entre dos valores
from random import uniform

def aleatorio(num1,num2: int):
    return round(uniform(num1,num2))

def main():
    print("Dame dos números")
    num1= int(input("Número 1:"))
    num2 = int(input("Número 2:"))
    print(aleatorio(num1,num2))

if __name__ == "__main__":
    main()