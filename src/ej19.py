#Ejercicio 1.2.19
#Escribir un programa que pregunte el nombre del usuario en la consola y después de que el usuario lo introduzca muestre por pantalla "NOMBRE tiene n letras.", donde NOMBRE es el nombre de usuario en mayúsculas y n es el número de letras que tienen el nombre.

print("Introduce tu nombre:")
nom = input()
#COMO HEMOS APRENDIDO DEL ANTERIOR EJERCICIO, USAMOS EL UPPER PARA PONER TODAS LAS LETRAS EN MAYÚSCULAS
NOM = nom.upper()
#Utilizamos len() para poder contar los caracteres de cualquier variable
n = len(NOM)
print(f"{NOM} tiene {n} letras")