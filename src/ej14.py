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