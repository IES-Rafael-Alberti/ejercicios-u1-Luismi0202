from random import uniform

#FUNCIÓN PARA VER SI ES UN NÚMERO
def comprobar_si_num(valor:str):
    try:
        valor = float(valor)
        return True
    except ValueError:
        return False
#FUNCIÓN PARA VER SI ES DECIMAL

def decimal(num):
    X= 0
    while (X == 0):
        if num %1 != 0:
            print("**ERROR**, SU NÚMERO DEBE SER UN ENTERO")
            num = float(input("Dame otravez el número:"))
            X=0
        else:
            X=1
            num = int(num)
        
#FUNCIÓN PARA VER SI ESTA EN EL RANGO 1-100
def rango(num):
    X=0
    while(X==0):
        if (num < 1 or num > 100):
            print("**ERROR** DAME UN NÚMERO ENTERO ENTRE EL RANGO 1-100")
            num = float(input())
            #LLAMADA A LA FUNCIÓN DECIMAL PARA QUE VUELVA A COMPROBAR SI ES DECIMAL O NO
            decimal(num)
            X=0
        else:
            X=1
        
#FUNCIÓN QUE TE DIGA CALIENTE O FRIO EN FUNCIÓN DE LO CERCA QUE ESTÉ

def caliente_o_frio(num,numA):
    #HACEMOS QUE EL NUMERO MAYOR SE RESTE PRIMERO PARA QUE NO DE ERRORES

    if num < numA: 
        diferencia = numA - num
    else: 
        diferencia = num - numA
    if diferencia <= 5:
        return "¡¡CALIENTE, CALIENTE!!"
    elif diferencia <= 30:
        return "Te vas calentando...."
    elif diferencia <= 40:
        return "Templadito templadito...."
    elif diferencia <= 50:
        return "Estás fresquito"
    elif diferencia <= 100:
        return "Estás en el ártico!"
    
#FUNCIÓN PRINCIPAL

def main():
    print("ESTOY PENSANDO EN UN NÚMERO ENTERO QUE SE ENCUENTRA ENTRE EL 1 Y EL 100 ¿CUÁL ES?")
    valor = input()
    while not comprobar_si_num(valor):
        print("no estoy para bromas, sabes que eso no es un número")
        valor = input()
    num = float(valor)
    numA = round(uniform(1,100))
    decimal(num)
    rango(num)
    X=0
    while X==0:
        #SI EL NUMERO NO ES IGUAL AL NÚMERO ALEATORIO, LLAMARÁ A LA FUNCIÓN CALIENTE O FRIO PARA VER COMO DE CERCA ESTÁ.
        if num != numA:
            print(caliente_o_frio(num,numA))
            valor = input("No lo adivinaste! Sigue intentándolo:")
            while not comprobar_si_num(valor):
                print("No estoy para bromas, introduce un número válido")
                valor = input()
            num = float(valor)
            decimal(num)
            rango(num)
            X=0
        else:
         X=1
         print(f"EHNORABUENA, EL NÚMERO ERA {numA}")

if __name__ == "__main__":
    main()