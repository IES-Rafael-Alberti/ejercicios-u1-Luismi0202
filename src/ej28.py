#Realiza un programa en Python que lea dos números enteros, muestre cuál es el menor de los dos y cuántos números existen entre ellos dos.
#El segundo número no puede ser igual, si es así, debe mostrar el error: "Los números no pueden ser iguales".
#Si los números son diferentes, por ejemplo, 5 y 12, debe mostrar la frase: "El número menor es el 5 y entre ellos existen 7 números enteros".

#Vamos a hacer una anidación de ifs para poder hacer las 3 condiciones que se nos piden:
print("DAME DOS NÚMEROS")
num1 = int(input())
num2 = int(input())
if (num1 == num2):
    print("Los números no pueden ser iguales")
else:
    if (num1 < num2):
        resta = num2 - num1
        print(f"El número menor es el {num1} y entre ellos existen {resta} números enteros")
    else:
        resta = num1 - num2 
        print(f"El número menor es el {num2} y entre ellos existen {resta} números enteros")