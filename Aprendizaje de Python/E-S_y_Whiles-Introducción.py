# Para pedirle informacion al usuario, se usa la función input

nombre = input("¿Cómo te llamás?: ")
print(f"Hola {nombre}")

# Nótese que input trata cualquier entrada del usuario como si fuera una cadena

edad = input("Decime tu edad por favor: ") # Por ejemplo, 35

# print(edad + 1) <-- Da error, porque edad es una cadena, no un número

edad = int(edad) # Para que ande hay que castearlo como entero

print(edad + 1) # Ahora si, anda e imprime 36

# Un operador 
