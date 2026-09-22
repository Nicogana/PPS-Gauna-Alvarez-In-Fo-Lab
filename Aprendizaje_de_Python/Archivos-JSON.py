# JSON (JavaScript Object Notation) es un formato de archivos
# que se caracteriza por su simpleza y portabilidad. 
# muchos lenguajes de programación (incluido Python)
# lo usan para transmitir información

import json

# arranquemos guardando datos sencillos 

numeros = [1,2,3,4,5]

arch = 'numeros.json'

with open(arch, 'w') as a:
    json.dump(numeros, a)

# Y ahora leamos los datos guardados

with open(arch) as a:
    datos = json.load(a)

print(datos) # Imprime [1,2,3,4,5]

# El uso más común de los JSON es guardar información provista por el usuario

usuario = input("¿Cómo te llamas?: ")

arch = 'usuario.json'

with open(arch, 'w') as a:
    json.dump(usuario, a)
    print(f"Nunca te olvidaremos {usuario}")

# Habiendo guardado el nombre del usuario, podemos escribir código para recuperarlo.
# Esto se ve mejor si el código se escribe en un archivo separado. Lo dejo todo junto
# para no crear archivos innecesarios, pero si alguien desea probar que funciona,
# puede copiar el siguiente código en un archivo que tenga solamente la linea 
# import json al principio

arch = 'usuario.json'

with open(arch) as a:
    usuario = json.load(a)
    print(f"¡has vuelto {usuario}!")

# Con esto y los bloques try, podemos construir funciones mas complejas.
# Acá tenemos una función que carga el nombre del usuario si ya existe
# (si no existe lo crea)

def usuario(arch):
    """Carga el nombre del usuario y lo saluda. 
    Si el usuario no existe, lo crea"""
    try: 
        arch = 'usuario.json'
        with open(arch) as a:
            datos = json.load(a)
    except FileNotFoundError:
        usuario = input("¿Cómo te llamas?: ")
        with open(arch, 'w') as a:
            json.dump(usuario, a)
        print(f"Nunca te olvidaremos {usuario}")
    else: 
        print(f"¡has vuelto {usuario}!")

# Modularizando la función, finalmente nos queda 

def cargar_usuario(usuario):
    """ si existe el usuario, lo carga """
    try: 
        with open(usuario) as a:
            datos = json.load(a)
    except FileNotFoundError: 
        pass
    else:
        return datos

def crear_usuario(usuario):
    """Crea un nuevo usuario"""
    nombre = input("¿cómo te llamas?: ")
    with open(usuario) as a:
        json.dump(usuario, a)
    return nombre

def saludar_al_usuario():
    """Saluda al usuario con su nombre"""
    usuario = cargar_usuario('usuario.txt')
    if usuario:
        print(f"Bienvenido, {usuario}")
    else:
        usuario = crear_usuario('usuario.txt')
        print(f"Nunca te olvidaremos {usuario}")

saludar_al_usuario()