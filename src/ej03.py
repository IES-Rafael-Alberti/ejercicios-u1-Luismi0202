#Ejercicio 1.2.3
#Suponiendo que se han ejecutado las siguientes sentencias de asignación:

ancho = 17
alto = 12.0

#17 entre 2 será decimal (float)
tipo1 =(type (ancho /2))
resultado1= (ancho /2)
print (f"El tipo sera {tipo1} y el resultado será {resultado1}")
#Será entero
tipo2 = (type (ancho //2))
resultado2= (ancho //2)
print (f"El tipo sera {tipo2} y el resultado será {resultado2}")
#12.0 entre 3 dará decimal
tipo3 = (type(alto /3))
resultado3 =(alto /3)
print (f"El tipo sera {tipo3} y el resultado será {resultado3}")
#Al ser una suma con  multiplicación simple esto será un número entero
tipo4 = (type (1 + 2 * 5))
resultado4 = (1 + 2 * 5)
print (f"El tipo sera {tipo4} y el resultado será {resultado4}")