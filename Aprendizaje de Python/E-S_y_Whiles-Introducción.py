# Para pedirle informacion al usuario, se usa la función input

nombre = input("¿Cómo te llamás?: ")
print(f"Hola {nombre}")

# Nótese que input trata cualquier entrada del usuario como si fuera una cadena

edad = input("Decime tu edad por favor: ") # Por ejemplo, 35

# print(edad + 1) <-- Da error, porque edad es una cadena, no un número

edad = int(edad) # Para que ande hay que castearlo como entero

print(edad + 1) # Ahora si, anda e imprime 36

# Otro bucle particularmente interesante es el While. A diferencia del for, que se ejecuta n veces, el while se ejecuta 
# mientras se cumpla una determinada condicion.

nro_actual = 0

while nro_actual <= 5:
    print(nro_actual) # Imprime los números del 0 al 5
    nro_actual += 1

# Los whiles nos permiten crear cosas como programas de ejecucion infinitas, que solo paran cuando el usuario lo indica

mensaje = ""

while mensaje != 'salir':
    mensaje = input("Decime algo y te lo repito. Si querés salir, digitá 'salir'") # Repetirá infinitamente lo que el usuario le digité 
    if mensaje != 'salir':                                                         # hasta que este escriba salir
            print(mensaje)
    else:
            print("Saliendo...")

# Es muy común utilizar banderas junto con los bucles. 
# Una bandera es una variable que almacena un valor que es relevante para definir cómo sigue la ejecución del programa 
# (si ejecuta tal o cuál función, si detiene la ejecución, etc)

# Programa anterior, reescrito con una bandera

mensaje = ""
activo = True

while activo: # La bandera activo es la que determina si el programa se sigue ejecutando o no
    mensaje = input("Decime algo y te lo repito. Si querés salir, digitá 'salir'") 
    if mensaje != 'salir':
            print(mensaje)
    else:
            activo = False 
            print("Saliendo...")

# Es posible crear bucles que se ejecuten indefinidamente

# while True:
      # print("Esto nunca para")

