#Ejercicio 1.2.3
#Suponiendo que se han ejecutado las siguientes sentencias de asignación:

ancho = 17
alto = 12.0

#17 entre 2 será decimal (float)
tipo1 =(type (ancho /2))
resultado1= (ancho /2)
print (f"ancho/2= {resultado1} y es de tipo {tipo1}")
#Será entero
tipo2 = (type (ancho //2))
resultado2= (ancho //2)
print (f"ancho//2= {resultado2} y es de tipo {tipo2}")
#12.0 entre 3 dará decimal
tipo3 = (type(alto /3))
resultado3 =(alto /3)
print (f"alto/3= {resultado3} y es de tipo {tipo3}")
#Al ser una suma con  multiplicación simple esto será un número entero
tipo4 = (type (1 + 2 * 5))
resultado4 = (1 + 2 * 5)
print (f"1+2*5= {resultado4} y es de tipo {tipo4}")