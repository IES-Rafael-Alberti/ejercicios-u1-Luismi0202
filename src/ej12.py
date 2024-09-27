print ("¿Cuántos kg pesas?")
peso = float(input())
print ("¿Cuánto metros mides?")
altura = float(input())
IMC = peso / altura **2
RESULTADO = round(IMC, 3)
print (f"pesas {peso}, mides {altura} y su IMC es {RESULTADO}")