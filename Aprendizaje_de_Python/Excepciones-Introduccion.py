# Las Excepciones son objetos especiales que gestionan errores
# Si se produce un error que Python no sabe gestionar, 
# crea una excepcion. 
# Nosotros podemos escribir codigo que maneje la excepcion 
# y permita al programa seguir ejecutandose

# Empecemos con un error típico: la división por 0

print(5/0)

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

print("Digita s oara salir")

while True:
    n1 = input("\n Primer número")
    if n1 == 's':
        break
    n2 = input("Segundo número")
    if n2 == 's':
        break
    r = int(n1)/int(n2)
    print(r)

# Si le pedimos que divida por cero, crashea y levanta un traceback

# Esta nueva calculadora si puede lidiar con una division por cero

while True:
    n1 = input("\n Primer número")
    if n1 == 's':
        break
    n2 = input("Segundo número")
    if n2 == 's':
        break
    try: 
        r = int(n1)/int(n2)
    except ZeroDivisionError:
        print("¡No se puede dividir por cero!")
    else:
        print(r)
