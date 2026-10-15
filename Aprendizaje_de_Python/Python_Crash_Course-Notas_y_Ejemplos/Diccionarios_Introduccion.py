# Los diccionarios funcionan de la manera KEY - VALUE (como maps en Java)
materia = {'nombre': 'PPS','nota': 10}

print(materia['nombre'])
print(materia['nota'])
print(f"Te sacaste un {materia['nota']} en {materia['nombre']}")


nota_juegos = {'BOTW': 97, 'TOTK': 96, 'Mario Galaxy 2': 98}
print(nota_juegos)
# Agrego duplas al diccionario
nota_juegos['Ocarina Of Time']=99
nota_juegos['Pokémon Escarlata']= 72

print(nota_juegos)
#Modificaciones
nota_juegos['Super Mario Odyssey']=90
print(nota_juegos)
nota_juegos['Super Mario Odyssey']=97
print(f"La nota de Mario Odyssey era {nota_juegos['Super Mario Odyssey']}!")
# Eliminaciones
del nota_juegos['Super Mario Odyssey']
print(nota_juegos)
# Catcheo errores con .get()
nota_juego=nota_juegos.get('Ocarina Remake', 'Aún no se ha lanzado!')
print(nota_juego)

# Try it yourself!
persona={'Nombre':'José', 'Apellido': 'Colantonio', 'edad':96, 'ciudad': '9 de julio'}
print(persona)

glosario = {
    "variable": "Es un espacio donde se guarda un valor que puede cambiar.",
    "lista": "Es una colección ordenada de elementos que puede modificarse.",
    "tupla": "Es una colección ordenada de elementos que no puede modificarse.",
    "diccionario": "Es una colección de pares clave-valor.",
    "bucle": "Es una estructura que permite repetir un bloque de código."
}

print("Variable:", glosario["variable"], "\n")
print("Lista:", glosario["lista"], "\n")
print("Tupla:", glosario["tupla"], "\n")
print("Diccionario:", glosario["diccionario"], "\n")
print("Bucle:", glosario["bucle"])

# Ahora veremos bucles con diccionarios

usuario= {
    'nombreuser': 'josealv',
    'nombre': 'José',
    'apellido': 'Álvarez'
}
for key, value in usuario.items():
    print(f"Key: {key.title()}, Valor: {value}")

for juego, nota in nota_juegos.items():
    print(f"\nLa nota de {juego} es {nota}.")

# si quiero solamente realizar un loop en los juegos (sin keys es igual):

for juego in nota_juegos.keys():
    print(f"{juego}")

if 'Pokémon Blanco' not in nota_juegos.keys():
    print('Falta rankear Pokémon Blanco!')

#También pueden ser ordenados!
for juego in sorted(nota_juegos.keys()):
    print(f"{juego}")
# También podemos ver solo los valores con values()
for nota in nota_juegos.values():
    print(f"{nota}")

# Si tuviera algun valor repetido las notas, con set(nota_juegos.values())
# se pueden quitar duplicados

# También existen los SETS que permiten que al ingresar valores repetidos, estos se unifiquen

materias = {'PPS', 'Programación A', 'PPS', 'Etica'}
print(materias) # PPS se escribe solo una vez!

# Ahora podemos ver Listas de Diccionarios:
juego_0 = {'nombre': 'The Legend of Zelda', 'puntos': 10}
juego_1 = {'nombre': 'Mario Kart 8 Deluxe', 'puntos': 8}
juego_2 = {'nombre': 'Pokémon Legends: Arceus', 'puntos': 9}

juegos = [juego_0, juego_1, juego_2]

for juego in juegos:
    print(juego)

juegos = []

for numero_juego in range(30):
    nuevo_juego = {
        'nombre': 'Juego',
        'genero': 'Aventura',
        'puntuacion': 8
    }
    juegos.append(nuevo_juego)

for juego in juegos[:3]:
    if juego['genero'] == 'Aventura':
        juego['genero'] = 'Acción'
        juego['puntuacion'] = 10

for juego in juegos[:5]:
    print(juego)

print("...")

print(f"Total de juegos: {len(juegos)}")

# Puedo hacer una lista en un rango de 30 diccionarios distintos
# y cambiarle a ciertos los atributos que yo considere necesario


# También podemos tener listas dentro de los diccionarios:

juego = {
    'nombre': 'Super Smash Bros. Ultimate',
    'personajes': ['Mario', 'Link', 'Kirby', 'Pikachu']
}

print(f"Elegiste {juego['nombre']}, con los siguientes personajes:")

for personaje in juego['personajes']:
    print(f"\t{personaje}")

# Y varias listas dentro un diccionario:
juegos_favoritos = {
    'Nicolas': ['Pokémon', 'The Legend of Zelda'],
    'Juan': ['Mario Kart'],
    'Pedro': ['Super Smash Bros.', 'Animal Crossing'],
    'Sofia': ['Pokémon', 'Mario']
}

for nombre, juegos in juegos_favoritos.items():
    print(f"\n{nombre} tiene como juegos favoritos:")

    for juego in juegos:
        print(f"\t{juego}")

# Además también podemos tener un diccionario dentro de otro diccionario

jugadores = {
    'nicolas': {
        'nombre': 'Nicolas',
        'juego_favorito': 'Pokémon',
        'consola': 'Nintendo Switch 2'
    },

    'juan': {
        'nombre': 'Juan',
        'juego_favorito': 'Mario Kart 8 Deluxe',
        'consola': 'Nintendo Switch'
    }
}
for usuario, informacion in jugadores.items():
    print(f"\nUsuario: {usuario}")

    nombre = informacion['nombre']
    juego = informacion['juego_favorito']
    consola = informacion['consola']

    print(f"\tNombre: {nombre}")
    print(f"\tJuego favorito: {juego}")
    print(f"\tConsola: {consola}")
    