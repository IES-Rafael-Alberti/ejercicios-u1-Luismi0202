#Ejercicio 1.2.23
#Escribir un programa que pregunte el correo electrónico del usuario en la consola y muestre por pantalla otro correo electrónico con el mismo nombre (la parte delante de la arroba @) pero con dominio ceu.es.

print("Escribe tu correo electronico:")
correo = input()
#utilizamos var[:var.find("@")]. var sera sustituido por el nombre de nuestra variable, los dos puntos son porque lo que va antes se conservará y el find buscará el caracter que le demos para no incluirlo.
nombre = correo[:correo.find("@")]
print(nombre + "@ceu.es.")