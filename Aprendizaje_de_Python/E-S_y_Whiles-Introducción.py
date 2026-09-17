# Para pedirle informacion al usuario, se usa la función input

nombre = input("¿Cómo te llamás?: ")
print(f"Hola {nombre}")

# Nótese que input trata cualquier entrada del usuario como si fuera una cadena

edad = input("Decime tu edad por favor: ") # Por ejemplo, 35

# print(edad + 1) <-- Da error, porque edad es una cadena, no un número

edad = int(edad) # Para que ande hay que castearlo como entero

# esto también es válido

edad = int(input("decime tu edad, por favor: "))

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

# Podemos usar un break para salir del bucle

while True: 
      echo = input("Digite salir para salir: ")

      if echo == 'salir':
            break
      else: 
            print(f"digitaste: {echo}")

# Tambien existe el continue, que complementa al break
# Le indica a python que no debe debe regresar al 
# principio del bucle sin ejecutar el resto de su cuerpo

numero = 0

while numero < 10: 
      numero += 1
      if numero % 2 == 0:
            continue
      print(f"Este numero ({numero}) es impar")


usuarios_no_confirmados = ['Bruno', 'Ana', 'Luis']
usuarios_confirmados = []

# En general, los bucles while se utilizan cuando no sabemos 
# cuantas iteraciones se deben realizar

while usuarios_no_confirmados: 
      usuario = usuarios_no_confirmados.pop()

      print(f"Verificando usuario: {usuario.title()}")
      usuarios_confirmados.append(usuario)

      print("\n Lista de usuarios confirmados:  ")

# Y los bucles for se utilizan cuando si sabemos
# cuantas iteraciones se deben realizar 

for usuario_confirmado in usuarios_confirmados:
        print(usuario_confirmado.title())


# Tambien se usan para remover duplicados en una lista

mascotas = ['perro', 'gato', 'caballo', 'surubí', 'gato', 'conejo']
print(mascotas)

while 'gato' in mascotas:
      mascotas.remove('gato')

print(mascotas)

# Y para llenar diccionarios

encuesta_activa = True

respuestas_encuesta = {}

while encuesta_activa:
      nombre = input("¿Como te llamas?: ")
      montaña = input("¿que montaña te gustaría escalar?: ")

      respuestas_encuesta[nombre] = montaña

      repetir = input("¿Desea compartir la encuesta? (s/n)")
      if repetir == 'no':
            encuesta_activa = False

print("\n --- Resultados de la Encuesta ---")

for nombre, montaña in respuestas_encuesta.items():
      print(f"a {nombre} le gustaria escalar {montaña}")

