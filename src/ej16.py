pan = 3.49
print ("¿Cuánto panes que no son del día hemos vendido?")
panpasado = float(input())
descuento = 0.60
preciodescuento = round(pan * descuento,2)
coste = round(pan * (1 - descuento),2)
print(f"El precio habitual del pan es de {pan}€, el descuento que se le hace es de {preciodescuento}€ y el coste final del pan que no es del día es de {coste}€")