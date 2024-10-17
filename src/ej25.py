#Ejercicio 1.2.25
#Escribir un programa que pregunte al usuario la fecha de su nacimiento en formato dd/mm/aaaa y muestra por pantalla, el día, el mes y el año. Adaptar el programa anterior para que también funcione cuando el día o el mes se introduzcan con un solo carácter.

print("¿Cuándo naciste? Dimelo en formato dd/mm/aaaa")
fecha = input()
lista = fecha.split("/")
print(f"NACISTE EL... {lista}")
