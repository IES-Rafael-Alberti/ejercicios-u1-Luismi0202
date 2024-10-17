#ej01 => recibe un nombre y retorna una cadena de caracteres con el resultado.

#función llamada saludo recibe nombre
def saludo(nombre):
	return f"Hola, {nombre}."
def main():
	print("Introduce un nombre")
	nombre = input()
	#imprime la función saludo que recibe el nombre
	print (saludo(nombre))
if __name__ == "__main__":
	main()