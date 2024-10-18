#Ejercicio 1.2.14
#Una juguetería tiene mucho éxito en dos de sus productos: payasos y muñecas. Suele hacer venta por correo y la empresa de logística les cobra por peso de cada paquete así que deben calcular el peso de los payasos y muñecas que saldrán en cada paquete a demanda. Cada payaso pesa 112 g y cada muñeca 75 g. Escribir un programa que lea el número de payasos y muñecas vendidos en el último pedido y calcule el peso total del paquete que será enviado.

#La primera p significa peso (peso payaso,peso muñeca)
ppayaso = 112
pmuñeca = 75
print("¿Cuántos payasos ha comprado?")
payaso = int(input())
print("¿Cuántas muñecas ha comprado?")
muñeca = int(input())
#pt significa peso total (pesototal payaso, peso total muñecas)
ptpayaso = payaso * ppayaso 
ptmuñeca = muñeca * pmuñeca
pesopaquete = ptpayaso + ptmuñeca
print(f"El peso total del paquete es {pesopaquete}g y ha comprado {payaso} payasos y {muñeca} muñecas.")