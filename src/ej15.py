#Ejercicio 1.2.15
#Imagina que acabas de abrir una nueva cuenta de ahorros que te ofrece el 4% de interés al año. Estos ahorros debido a intereses, que no se cobran hasta finales de año, se te añaden al balance final de tu cuenta de ahorros. Escribir un programa que comience leyendo la cantidad de dinero depositada en la cuenta de ahorros, introducida por el usuario. Después el programa debe calcular y mostrar por pantalla la cantidad de ahorros tras el primer, segundo y tercer años. Redondear cada cantidad a dos decimales.

print("INTRODUCE CUÁNTO DINERO TIENES AHORRADO")
dinero = float(input())
cuenta = dinero
#Bucle que se usará para poder saber cuanto irá ahorrando con los años. En este bucle imprimiremos cada i para que nos especifique el año y cuanto dinero tendremos ese año.
for i in range (1,4):
    cuenta = cuenta * 1.4
    DINERO = round(cuenta, 2)
    print(f"Al final del año{i} tendrás {DINERO}€ en la cuenta.")