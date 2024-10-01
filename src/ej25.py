#Ejercicio 1.2.25
#Escribir un programa que pregunte al usuario la fecha de su nacimiento en formato dd/mm/aaaa y muestra por pantalla, el día, el mes y el año. Adaptar el programa anterior para que también funcione cuando el día o el mes se introduzcan con un solo carácter.

print("¿Cuándo naciste? Dimelo en formato dd/mm/aaaa")
fecha = input()
dia = fecha[:2]
num_mes = int(fecha[3:5])
año = fecha[6:10]
#Creamos una lista (indice) con los nombres de los meses para que a la hora de que nos digan en que mes nace el usuario se lo de diciendole el nombre en vez de con los números, que es algo mucho más lógico.
meses = ["Enero", "Febrero","Marzo", "Abril", "Mayo", "Junio","Julio","Agosto","Septiembre","Octubre","Noviembre", "Diciembre"]
#Al igual que en los bucles for sumábamos porque python empezaba a contar por 0 y nos restaba 1, aquí restamos nosotros para poder ajustarnos a la lista que va del 0 al 11
nombremes = meses[num_mes - 1]
print(f"Naciste el día {dia} del mes de {nombremes} en el año {año}")
