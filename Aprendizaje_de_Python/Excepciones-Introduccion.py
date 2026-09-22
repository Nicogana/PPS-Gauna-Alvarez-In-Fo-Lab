# Las Excepciones son objetos especiales que gestionan errores
# Si se produce un error que Python no sabe gestionar, 
# crea una excepcion. 
# Nosotros podemos escribir codigo que maneje la excepcion 
# y permita al programa seguir ejecutandose

# Empecemos con un error típico: la división por 0

# print(5/0)

# Al ejecutarlo, imprime esto

# File "C:\Users\...", line 9, in <module>
#    print(5/0)
#          ~^~
# ZeroDivisionError: division by zero

# Lo anterior es un traceback: 
# un mensaje que Python envia cuando no puede hacer lo que le pedimos
# ZeroDivisionError es la excepcion que fue levantada.
# Ahora que la conocemos, podemos reescribir el código 
# para lidiar con ella

try: 
    print(5/0)
except ZeroDivisionError:
    print("¡No se puede dividir por cero!")

# Todo lo que pongamos en el bloque try, 
# Python va a intentar ejecutar. Si ocurre un error,
# Python va a buscar algun except que esté después del try 
# y cuyo error coincida con el error generado. Si lo encuentra,
# Ejecuta el código de ese except. Finalmente, si no encuentra 
# el except correspondiente, envia un traceback por pantalla

# El buen manejo de las excepciones permite que nuestro programa 
# pueda responder a situaciones inesperadas sin crashear

# Por ejemplo, está calculadora no puede lidiar 
# con la division por cero

print("Digita s para salir \n")

while True:
    n1 = input("\n Primer número: ")
    if n1 == 's':
        break
    n2 = input("Segundo número: ")
    if n2 == 's':
        break
    r = int(n1)/int(n2)
    print(r)

# Si le pedimos que divida por cero, crashea y levanta un traceback

# Esta nueva calculadora si puede lidiar con una division por cero

while True:
    n1 = input("\n Primer número: ")
    if n1 == 's':
        break
    n2 = input("Segundo número: ")
    if n2 == 's':
        break
    try: 
        r = int(n1)/int(n2)
    except ZeroDivisionError:
        print("¡No se puede dividir por cero!")
    else:
        print(r)

# Primero se intenta correr el código del bloque try (ahí va 
# el código que puede generar la excepcion) y si se ejecuta
# exitosamente, se continua con el bloque else. 
# El código en un bloque except se ejecuta solamente si durante
# la ejecución del try se levanta la excepción que corresponde 
# a ese bloque

# Otra excepción muy común es la de FileNotFoundError. Esta se 
# levanta cuando el programa ni encuentra el archivo solicitado

arch = 'no_existe.txt'

#with open(arch, encoding='utf-8') as a:
    #datos = a.read() # Devuelve FileNotFoundError: [Errno 2] No such file or directory: 'no_existe.txt'

# Para controlar esta situación, agregamos un try:

try:  
    with open(arch, encoding='utf-8') as a:
        datos = a.read()
except FileNotFoundError:
    print(f"El archivo {arch} no existe")

# Otro beneficio de los bloques try es que evitan que la ejecución
# del programa se corte al levantar una excepción. 
# por ej, tomemos un programa que cuenta la cantidad de palabras
# de varios libros

libros = ['mujercitas.txt', 'moby_dick.txt', 'el_aleph.txt', 'adios_a_las_armas.txt']

# En mi maquina tengo los archivos en texto plano de todos estos libros, salvo El Aleph
# si no utilizamos un try, al intentar contar las palabras de este libro, se va a levantar
# una excepción FileNotFoundError y el programa va a parar. Por tanto, 
# nunca vamos a llegar a contar las palabras de Adiós a las armas

def contar_palabras(arch):
    try:  
        with open(arch, encoding='utf-8') as a:
            datos = a.read()
    except FileNotFoundError:
        print(f"El archivo {arch} no existe")
    else:
        palabras = datos.split()
        cant_pal = len(palabras)
        print(f"El archivo {arch} tiene {cant_pal} palabras")

for libro in libros:
    contar_palabras(libro)

# Por supuesto, no necesitamos informar sobre cada una de las excepciones.
# Hay veces que queremos capturar una excepcion sin devolver nada. 
# En estos casos usamos la palabra clave pass


def contar_palabras(arch):
    try:  
        with open(arch, encoding='utf-8') as a:
            datos = a.read()
    except FileNotFoundError:
        pass # Funciona igual que la función anterior, pero no devuelve nada si se levanta la excepción
    else:
        palabras = datos.split()
        cant_pal = len(palabras)
        print(f"El archivo {arch} tiene {cant_pal} palabras")
