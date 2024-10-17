#Realiza un programa en Python que pida un número de inicio, un incremento y un total de la serie.

#El incremento y el total deben ser mayores que cero. Si no es así, el programa debe finalizar con un error o obligar a que introduzcan un valor correcto para ambos (os lo dejo a vuestra elección, la primera opción es más fácil, aunque el mundo está lleno de valientes).
#Por ejemplo, si introducen los valores 1, 1 y 10, el programa mostrará en consola exactamente lo siguiente: SERIE => 1-2..3..4..5..6..7..8..9-10
def incremento(num,aumento,total):
    X=0
    cadena = "SERIE =>"
    while(X==0):
        if(aumento <=0 and total <=0):
            print("ERROR, INTRODUCE DE NUEVO INCREMENTO Y TOTAL, NINGUNO DE LOS DOS DEBE SER MENOR O IGUAL A 0")
            aumento = int(input("Introduce incremento"))
            total = int(input("Introduce numero final de la cadena"))
        else:
            X=1
            for i in range (num,total +1, aumento):
                if i == num:
                    cadena += str(i) + "-"
                else:
                        cadena +=".." + str(i)
            print(f"{cadena}-{total}")
def main():
    print("Dame un número")
    num = int(input())
    print("Dame un incremento")
    aumento = int(input())
    print("Dame un número para acabar la serie")
    total = int(input())
    incremento(num,aumento,total)

if __name__ == "__main__":
    main()