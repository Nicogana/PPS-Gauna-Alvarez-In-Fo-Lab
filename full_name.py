# Se pueden concatenar cadenas utilizando el operador +, y también se pueden utilizar f-strings para formatear cadenas de manera más legible.
nombre = "san"
apellido = "martin"
#concatenacion = nombre + " " + apellido
nombre_completo = f"{nombre} {apellido}"
print(nombre_completo) # imprime san martin

# podemos aprovechar los f strings para formatear cadenas, haciendolas más legibles.

mensaje_final = f"¡Hola {nombre_completo.title()}!"
print(mensaje_final) # imprime ¡Hola San Martin, bienvenido a la clase de Python!