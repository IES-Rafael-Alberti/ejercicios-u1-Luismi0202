#Ejercicio 1.2.1
#Escribe un programa que pida el nombre del usuario para luego darle la bienvenida.
def saludo(nombre):
	return f"Hola, {nombre}."
def main():
	print("Introduce un nombre")
	nombre = input()
	print (saludo(nombre))

if __name__ == "__main__":
	main()
