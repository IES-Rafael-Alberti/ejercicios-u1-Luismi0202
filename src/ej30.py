#Realiza un programa en Python que pida un número de inicio, un incremento y un total de la serie.

#El incremento y el total deben ser mayores que cero. Si no es así, el programa debe finalizar con un error o obligar a que introduzcan un valor correcto para ambos (os lo dejo a vuestra elección, la primera opción es más fácil, aunque el mundo está lleno de valientes).
#Por ejemplo, si introducen los valores 1, 1 y 10, el programa mostrará en consola exactamente lo siguiente: SERIE => 1-2..3..4..5..6..7..8..9-10
X=0
cadena = 0
print("Dame un número")
num = int(input())
while (X==0):
    print("Dame un incremento")
    incremento = int(input())
    print("Dame el total de números que quieres")
    total = int(input())
    if (incremento and total <0):
        print("ERROR, INTRODUZCA UN INCREMENTO Y UN TOTAL QUE NO SEA MENOR QUE 0")
    else:
        X=1
for i in range (num,total):
    cadena = i + incremento
    print(cadena)