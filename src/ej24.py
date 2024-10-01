#Ejercicio 1.2.24
#Escribir un programa que pregunte por consola el precio de un producto en euros con dos decimales y muestre por pantalla el número de euros y el número de céntimos del precio introducido.

print("Escribe el precio de un producto en euros")
precio = float(input())
preciod = round(precio, 2)
#Para que .find funcione, debe buscar en formato str así que haremos el cambiazo de float a str, haremos lo habitual pero sin imprimirlo por pantalla (por obvias razones).
preciodstr = f"{preciod}"
#Ahora buscaremos en precidstr lo que va antes de la coma y lo que va después.
euros = preciodstr[:preciodstr.find(".")]
#Para lo que va después le sumaremos 1 a la posición y le indicaremos con los dos puntos que desde ahí nos coja todo
céntimos = preciodstr[preciodstr.find(".")+1:]
print (f" Su producto ha costado {euros} euros y {céntimos} céntimos")