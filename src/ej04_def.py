#ej04 => NO recibe parámetros y retorna una cadena de caracteres con la temperatura convertida en grados Celsius y entre parántesis la temperatura en grados farenheit... ambas temperaturas con 2 posiciones decimales. Por ejemplo, si introduce 212 debe retornar la cadena "100.00ºC (212.00ºF)". Dentro de la función se pedirá al usuario los grados Farenheit.

#variable temperatura que no recibe nada y te va pedir que le des número y hacerte operaciones para pasar de farenheit a celsius (alrevés del ejercicio base)
def temperatura():
    print("Dame un número")
    Fahrenheit = round(float(input()),2)
    Celsius= round(5*(Fahrenheit-32)/9, 2)
    return f"La temperatura en grados Celsius es {Celsius}ºC ({Fahrenheit}ºF)"
def main():
    #imprime la función temperatura para que muestre por pantalla el resultado de esta función.
    print(temperatura())
if __name__ == "__main__":
    main()