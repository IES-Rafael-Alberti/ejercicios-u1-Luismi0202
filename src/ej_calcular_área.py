#Ejercicio 1.2.28
#Calcular el área de un triángulo a partir de tres lados
import math

def masdeunpunto(valor : str):
    pos_punto = valor.find(".")
    if pos_punto >= 0 and valor.find(".", pos_punto + 1):
        return True
    return False


def contiene_solo_digitos_y_un_punto(valor: str):
    for i in range (len(valor)): #de 0 len(valor) -1
        if not valor[i].isdigit() or valor[i] == ".":
            return False 
        return True


def comprobar_numero_float(valor: str):
    if valor[:1] == "-":
        valor = valor[1:]
        if len(valor) == 0:
            return False
    if masdeunpunto(valor):
        return False

    return contiene_solo_digitos_y_un_punto(valor)


def area(lado_a,lado_b,lado_c):
    semiperimetro = (lado_a + lado_b + lado_c)/2
    area = math.sqrt(semiperimetro * (semiperimetro - lado_a) * (semiperimetro - lado_b) * (semiperimetro - lado_c))
    return area


def introduce_numero(msj:str):
    numero = input(msj).strip()
    while comprobar_numero_float(numero) == False:
        print("**ERROR** Número inválido")
        numero = input(msj).strip()
    return float(numero)


def main():
    print("Dame los 3 lados")
    lado_a = introduce_numero("lado 1:")
    lado_b = introduce_numero("lado 2:")
    lado_c = introduce_numero("lado 3:")
    print(area(lado_a,lado_b,lado_c))


if __name__ == "__main__":
    main()