#ej01 => recibe un nombre y retorna una cadena de caracteres con el resultado.
def saludo(nombre):
	return f"Hola, {nombre}."
def main():
	print("Introduce un nombre")
	nombre = input()
	print (saludo(nombre))
if __name__ == "__main__":
	main()