#Ejercicio 1.2.21¶
#Escribir un programa que pida al usuario que introduzca una frase en la consola y muestre por pantalla la frase invertida.

print("Dame una frase y te haré un truco de magia:")
frase = input()
#Para invertir el orden de los caracteres actuales utilizamos la sintasis [inicio:fin:paso]. Al tener inicio y fin vacíos y paso a -1, invertirá todo a lo que le demos este valor.
print(frase[::-1])

