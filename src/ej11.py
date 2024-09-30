print("DAME UN NÚMERO ENTERO POSITIVO")
num = float(input())
suma = 0
if(num < 0 or num % 1 != 0):
    print("NO!! DAME UN ENTERO POSITIVO")
    num=0
else:
    num = int(num)
    for i in range(1, num + 1):
     suma=suma+i
    print(f"LA SUMA DE LOS ENTEROS DE TU NÚMERO INTRODUCIDO ES DE {suma}")