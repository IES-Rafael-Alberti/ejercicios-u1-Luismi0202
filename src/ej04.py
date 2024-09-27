#Ejercicio 1.2.4
#Escribe un programa que le pida al usuario una temperatura en grados Celsius, la convierta a grados Fahrenheit e imprima por pantalla la temperatura convertida.

print("Dame un número")
Celsius = float(input())
#Usamos el round para redondear el resultado de la operación a dos decimales.
Fahrenheit= round(Celsius * 1.8 + 32, 2)
print(f"{Celsius} grados celsius en grados Fahrenheit son {Fahrenheit}")
