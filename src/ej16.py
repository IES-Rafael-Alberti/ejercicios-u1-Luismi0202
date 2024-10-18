#Ejercicio 1.2.16
#Una panadería vende barras de pan a 3.49€ cada una. El pan que no es el día tiene un descuento del 60%. Escribir un programa que comience leyendo el número de barras vendidas que no son del día. Después el programa debe mostrar el precio habitual de una barra de pan (establecido en el programa como una constante), el descuento que se le hace por no ser fresca y el coste final total de todas las barras no frescas.

pan = 3.49
print ("¿Cuánto panes que no son del día hemos vendido?")
panpasado = float(input())
descuento = 0.60
preciodescuento = round(pan * descuento,2)
coste = round(pan * (1 - descuento),2)
print(f"El precio habitual del pan es de {pan}€, el descuento que se le hace es de {preciodescuento}€ y el coste final del pan que no es del día es de {coste}€")