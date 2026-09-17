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
print(actor) # Imprime {'nombre': 'Federico', 'apellido': "D'Elia", 
             #          'edad': 59, 'altura': 180}

# Podemos ejecutar funciones dentro de un bucle

while True:
    print("\n Digite su nombre: ")
    print("(Presione s para salir)")

    nombre = input("Nombre: ")
    if nombre == 's':
            break
    apellido = input("Apellido: ")
    if apellido == 's':
            break

    nombre_completo = formatear_nombre(nombre, apellido)

    print(f"Hola {nombre_completo}")

# Tambien podemos pasarle listas a las funciones

def saludar_usuarios(usuarios):
     for usuario in usuarios:
          msj =  f"Hola {usuario.title()}"
          print(msj)

usuarios = ['Nico', 'Ivo', 'Santi', 'Jose']

saludar_usuarios(usuarios)

# Y estas pueden modificar los contenidos de la lista si lo deseamos

def pagar_sueldos(sueldos_pendientes, sueldos_pagos):
     while sueldos_pendientes:
          sueldo = sueldos_pendientes.pop()
          print(f"Pagando el sueldo a: {sueldo}")
          sueldos_pagos.append(sueldo)

def listar_sueldos_pagos(sueldos_pagos):
     print("\n Los siguientes sueldos ya han sido pagos: ")
     for sueldo in sueldos_pagos:
          print(sueldo)

# Podríamos mover la definición de las funciones a otro archivo 
# y que en el cuerpo nos quede solo esto, que es muy facil de leer

pendientes = ['Jose', 'Maria', 'Evelyn', 'Ramiro']
pagos = []

pagar_sueldos(pendientes, pagos)
listar_sueldos_pagos(pagos)

# Por supuesto, esto presenta un inconveniente. 
# La lista original (pendientes)ahora está vacía. 

print(pendientes) # Imprime []

# En los casos en los que queremos preservar la lista original, 
# podemos pasar una copia como argumento de la funcion

pendientes = ['Jose', 'Maria', 'Evelyn', 'Ramiro']
pagos = []

pagar_sueldos(pendientes[:], pagos) # paso una copia de pendientes y la lista pagos

print(pagos) # pagos se modifica 
print(pendientes) # pendientes se preserva

# Salvo que sea absolutamente necesario preservar la lista original, 
# conviene pasar las listas originales como parametro
# La copia preserva la lista original, pero es mucho mas lenta, 
# porque debe copiar todo el contenido de la lista antes de arrancar la ejecución

# Hay situaciones en las cuales no sabemos antes de tiempo 
# cuantos argumentos tiene la función. 
# Afortunadamente, podemos indicarle a la funcion 
# que acepte tantos argumentos como le de el usuario
# estos argumentos se denominan "Argumentos Arbitrários"

def hacer_pizza(*ingredientes):  
     if 'ananá' in ingredientes or 'piña' in ingredientes:
        print("no.")
     else:
        print("Preparando una pizza con: ")
        for ingrediente in ingredientes:
            print(f"- {ingrediente}")
          
hacer_pizza('Tomate', 'Queso') 
hacer_pizza('Tomate', 'Aceitunas', 'Jamón', 'Queso') 

# Podemos mezclar args. arbit. y args. posicionales
# Primero debemos poner los argumentos posicionales y a lo último los arbitrarios

def hacer_pizza(tamaño, *ingredientes):  
     if 'ananá' in ingredientes or 'piña' in ingredientes:
        print("no.")
     else:
        print(f"Preparando una pizza {tamaño.lower()} con: ")
        for ingrediente in ingredientes:
            print(f"- {ingrediente.title()}")

hacer_pizza("mediana", "Jamón", "Queso")

# El orden importa: 
# El valor mediana se utiliza para llenar el primer parámetro (tamaño)
# Todos los valores adicionales se juntan dentro del argumento arbitrario *ingredientes
# En general, a estos argumentos arbitrarios se los junta en el parámetro genérico *args

# Ahora vamos con un concepto muy interesante. 
# Podemos pasar tantos argumentos arbitrarios explicitos como querramos
# Esto suena un poco raro, pero básicamente significa que podemos definir argumentos
# Que no están especificados dentro de la funcion y pasarles valores. 
# Esto se entiende mejor con un ejemplo:

def crear_perfil(nombre, apellido, **datos):
    datos['nombre'] = nombre
    datos['apellido'] = apellido
    return datos

fisico = crear_perfil('Juan Martín', 'Maldacena', edad=58, educado_en='Balseiro')
print(fisico) # Imprime {'edad': 58, 'educado_en': 'Balseiro', 
              #          'nombre': 'Juan Martín', 'apellido': 'Maldacena'}

# Como vemos, agregamos campos nuevos al diccionario, que no estaban originalmente,
# utilizando los argumentos arbitrarios explicitos
# estos se suelen agrupar bajo el nombre genérico de **kwargs