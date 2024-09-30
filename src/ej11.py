#Declaramos una variable que sea X=0 para poder declarar un while que mientras esa variable sea 0 entonces se repite si no, se rompe el bucle.
X=0
while(X==0):
    print("DAME UN NÚMERO ENTERO POSITIVO")
    num = float(input())
    suma = 0
    #El % lo que hará será dividir num entre 1 y cogerá el resto, si el resto no es igual que 0 entonces no es entero, si no que es decimal. Queremos que no sea ni menor que 0 ni decimal.
    if(num < 0 or num % 1 != 0):
        print("NO!! DAME UN ENTERO POSITIVO")
        X=0
    #De lo contrario, salimos del bucle (X=1)
    else: X=1
#Usamos el int(num) porque el for al detectar el float dará problemas, así que haremos una conversión de num a entero (realmente esto se suele utilizar para que los decimale que les pongas te lo pase a enteros.)
num = int(num)
for i in range(1, num + 1):
    suma=suma+i
print(f"LA SUMA DE LOS ENTEROS DE TU NÚMERO INTRODUCIDO ES DE {suma}")