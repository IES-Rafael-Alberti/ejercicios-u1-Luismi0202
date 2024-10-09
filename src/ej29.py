#Realiza un programa en Python que solicite un nombre y una edad.
#Si el nombre está vacío, debes utilizar el valor "Desconocido". La edad debe pedirse hasta que introduzca una edad comprendida entre 0 y 125 años.
#El programa mostrará la siguiente frase: "Te llamas Pepito y tienes 20 años, te quedan aún 105 años por cumplir".

X= 0
print("Dame tu nombre")
#Separa los huecos de derecha e izquierda del nombre
nom = input().strip("")
while(X==0):
    print("Dame tu edad")
    edad = int(input())
    #contar carácteres de nombre y sustituirlo por "Desconocido" si es 0
    contador = len(nom)
    if (contador==0):
        nom="Desconocido"
    if edad in range(0,125+1):
        resta = 125 - edad
        print(f"Te llamas {nom} y tienes {edad} años, te quedan aún {resta} años por cumplir")
        #Salida del bucle
        X=1
    else:
        print("ERROR, VUELVE A INTENTARLO")
        #Vuelta al bucle
        X=0