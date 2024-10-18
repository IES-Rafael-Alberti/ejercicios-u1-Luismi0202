#Ejercicio 1.2.18
#Escribir un programa que pregunte el nombre completo del usuario en la consola y después muestre por pantalla el nombre completo del usuario tres veces, una con todas las letras minúsculas, otra con todas las letras mayúsculas y otra solo con la primera letra del nombre y de los apellidos en mayúscula. El usuario puede introducir su nombre combinando mayúsculas y minúsculas como quiera

print("Escribe tu nombre completo:")
nombre = input()
#Usaremos los metodos .upper .lower y .title que hacen posible las cosas que nos pide el ejercicio en orden.
NOM = nombre.upper()
nom = nombre.lower()
NomBre = nombre.title()
#una vez hemos declarado que las variables son upper lower o title imprimimos cada una de ellas para que salga por pantalla el input que le hemos dado en distintos carácteres.
print(NOM)
print(nom)
print(NomBre)