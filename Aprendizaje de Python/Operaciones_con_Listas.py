# Podemos usar bucles for para recorrer las listas y realizar operaciones con sus elementos. Por ej:

alumnos = ['Jose', 'Nico', 'Josefina', 'Rocio']

for alumno in alumnos:
    print(f"¡Buenas {alumno}!")  # Imprime cada nombre de la lista

print("Sigamos con el ejercicio")

# Tambien podemos iterar valores numéricos

for valor in range(1,5):
    print(valor)

# Notese que range arranca desde el primer valor indicado y para antes de llegar al ultimo. Por eso range(1,5) imprime 1 2 3 4 5
# Para imprimir 1 2 3 4 5 hay que usar range(1,6)

# Tambien podemos arrancar contando desde 0

for valor in range(6):
    print(valor) # imprime 0 1 2 3 4 5

# podemos variar el paso

for pares in range(0, 6, 2):
    print(pares) # imprime 0 2 4

# también podemos guardar los numeros iterados en una lista, usando la funcion list

numeros_pares = list(range(0,10, 2))

print(numeros_pares) # Imprime [0, 2, 4, 6, 8]

# o usando los propios bucles For

cubos = []

for valor in range(11):
    cubos.append(valor ** 3) 

print(cubos)  # Imprime [0, 1, 8, 27, 64, 125, 216, 343, 512, 729, 1000]

# Estas operaciones pueden escribirse en un formato mas breve
 
cubos = [valor ** 3 for valor in range(1,11)] # produce exactamente el mismo resultado que los anteriores, pero es mas legible

# Python incluye algunas funciones que nos permiten realizar operaciones básicas de estadística

maximo = max(cubos) # devuelve el maximo valor de la lista
minimo = min(cubos) # devuelve el minimo valor de la lista
total = sum(cubos) # devuelve la suma de todos los valores de la lista

# Tambien tenemos la opcion de trabajar con partes de la lista

jugadores = ['Messi', 'Kaka', 'El Trinche', 'Flores']

print(jugadores[0:3]) # imprime ['Messi', 'Kaka', 'El Trinche']
print(jugadores[2:3]) # imprime ['El Trinche']
print(jugadores[0:2]) # imprime ['Messi', 'Kaka']
print(jugadores[-3:]) # imprime ['Kaka', 'El Trinche', 'Flores']


print("estos son los mas cracks")

for crack in jugadores[0:3]:
    print(crack) 

# Podemos copiar una lista a otra

jugadoresv2 = jugadores[:] # copiamos los contenidos de jugadores a jugadoresv2

jugadoresv2.append('De Paul')

print(jugadores) # imprime ['Messi', 'Kaka', 'El Trinche', 'Flores']
print(jugadoresv2) # imprime ['Messi', 'Kaka', 'El Trinche', 'Flores', 'De Paul']


# Ojo, esto anda, pero el resultado es muy distinto 

jugadoresv2 = jugadores # esto copia LA REFERENCIA de jugadores a jugadoresv2. Ahora ambas variables apuntan a la misma lista 
                        # por lo que cualquier cambio realizado sobre jugadores se verá reflejado en jugadoresv2 (y viceversa)

jugadoresv2.append('De Paul')

print(jugadoresv2) # imprime ['Messi', 'Kaka', 'El Trinche', 'Flores', 'De Paul']

print(jugadores) # imprime lo mismo. Al modificar jugadoresv2, también se modifica jugadores

