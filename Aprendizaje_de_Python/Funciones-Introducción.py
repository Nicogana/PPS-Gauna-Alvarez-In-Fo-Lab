import sys
sys.stdout.reconfigure(encoding='utf-8')

# las funciones son bloques de código 
# que están diseñados para realizar una tarea sencilla

def saludar_al_usuario():
    print("¡Hola Pibe!")

saludar_al_usuario()

# Es posible pasarle datos a una funcion mediante parámetros

def saludar_al_usuario(nombre):
    print(f"¡Hola {nombre.title()}!")

saludar_al_usuario('José')

# Existen varias formas de pasar argumentos a la función 

# Pueden pasarse posicionalmente: 
# Python coincide los argumentos en función al orden

def describir_cuadro_de_futbol(nombre, apodo):
    print(f"Soy de {nombre} ({apodo})")

describir_cuadro_de_futbol('San Lorenzo', 'Cuervo') # Imprime Soy de San Lorenzo (Cuervo)
describir_cuadro_de_futbol('Boca', 'Xeneize') # Imprime Soy de Boca (Xeneize)

# Esto puede traer problemas si nos equivocamos en el orden

describir_cuadro_de_futbol("Canalla", "Rosario Central") # Imprime Soy Canalla (Rosario Central)

# Para evitar esto, se pueden asignar explicitamente

describir_cuadro_de_futbol(nombre = 'Rosario Central', apodo = 'Canalla') 

# Ahora si se imprime bien 

# Tambien podemos asignar valores por defecto a los parámetros. 

def describir_cuadro_de_futbol(nombre='Sheffield F.C', apodo='The Club'):
    print(f"Soy de {nombre} ({apodo})")

# Si en la llamada de la funcion no se especifican los valores, 
# se usaran los asignados por defecto

describir_cuadro_de_futbol() # Imprime Soy de Sheffield F.C (The Club)

# Es buena práctica realizar asignaciones explicitas en funciones que tienen parámetros
# por defecto

describir_cuadro_de_futbol("Cuervo") 

# Imprime Soy de Cuervo (The Club) porque toma Cuervo cómo el 1er parámetro (nombre) 
# Si queremos que lo tome como apodo, necesitamos asignarlo explicitamente:

describir_cuadro_de_futbol(apodo="Cuervo") # Imprime Soy de Sheffield F.C (Cuervo)

# Las funciones pueden devolver un valor mediante la palabra clave return

def formatear_nombre(nombre, apellido):
    nombre_completo= f"{nombre} {apellido}"
    return nombre_completo.title()

boxeador = formatear_nombre("ringo", "bonavena")
print(boxeador)

# Y acomodando un poco los argumentos, podemos hacer que algunos de estos sean opcionales

def formatear_nombre(nombre, apellido, segundo_nombre=''):
    if segundo_nombre:
            nombre_completo= f"{nombre} {segundo_nombre} {apellido}"
    else:
         nombre_completo= f"{nombre} {apellido}"
    return nombre_completo.title()

# El argumento segundo_nombre es opcional. Por defecto, es una cadena vacía. 
# Y funciona con personas que no tienen segundo nombre

boxeador = formatear_nombre("ringo", "bonavena")
print(boxeador)

# Y también con personas que si

corredor_de_F1 = formatear_nombre("franco", "alejandro", "colapinto")
print(corredor_de_F1)

# No es necesario limitarse a tipos de datos simples, como cadenas o enteros
# Las funciones tambien pueden devolver 
# tipos de datos estructurados, como diccionarios o listas

def crear_persona(nombre, apellido):
     persona = {'nombre': nombre, 'apellido':apellido}
     return persona

basquetbolista = crear_persona("Manu", "Ginóbili")
print(basquetbolista) # Imprime {'nombre': 'Manu', 'apellido': 'Ginóbili'}

# Podemos aprovechar esto junto a los parámetros opcionales para construir 
# estructuras mucho más sofisticadas. 
# Por ejemplo, esta funcion permite crear un diccionario con el nombre y apellido
# y opcionalmente la edad y/o la altura

def crear_persona(nombre, apellido, edad=None, altura=None):
    persona = {'nombre': nombre, 'apellido':apellido}
    if edad:
        persona['edad'] = edad
    if altura:
        persona['altura'] = altura
    return persona

modelo = crear_persona("Hernán", "Drago", altura = 193) 
print(modelo) # Imprime {'nombre': 'Hernan', 'apellido': 'Drago', 'altura': 193}

actor = crear_persona("Federico", "D'Elía", 59, 180)
print(actor) # Imprime {'nombre': 'Federico', 'apellido': "D'Elia", 'edad': 59, 'altura': 180}

# Podemos ejecutar funciones dentro de un bucle

while True:
    print("\n Digite su nombre: ")
    print("(Presione s para salir)")

    nombre = input("Nombre: ")
    if nombre == 'q':
            break
    apellido = input("Apellido: ")
    if apellido == 'q':
            break

    nombre_completo = formatear_nombre(nombre, apellido)

    print(f"Hola {nombre_completo}")

    