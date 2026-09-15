# Para pedirle informacion al usuario, se usa la función input

nombre = input("¿Cómo te llamás?: ")
print(f"Hola {nombre}")

# Nótese que input trata cualquier entrada del usuario como si fuera una cadena

edad = input("Decime tu edad por favor: ")

print(edad + 1) # Da error, porque edad es una cadena, no un número
