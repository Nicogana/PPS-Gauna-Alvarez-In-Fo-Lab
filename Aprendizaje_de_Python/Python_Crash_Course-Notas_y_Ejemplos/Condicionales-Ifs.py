edad = 18

# La estructura básica del if es muy similar a la de otros lenguajes de programacion

if edad == 18:
    print("Felicidades, ya podés votar")
    print("Acordate de mirar si estás en el Padrón")    
else:
    print("No, todavía no podés votar")

# El else if se escribe elif

if edad == 18:
    print("Felicidades, ya podés votar")
    print("Acordate de mirar si estás en el Padrón")    
elif edad > 65:
    print("Felicidades, ya podés votar y jubilarte")
    print("Andá a pasar tiempo con tu nieto")

# A veces no conviene tener un else, porque puede llevar a resultados inválidos, 
# ya que captura todo lo que no coincida con las condiciones evaludas por el if y el elif

edad = 23

if edad == 18:
    print("Felicidades, ya podés votar")
    print("Acordate de mirar si estás en el Padrón")    
elif edad >= 65:
    print("Felicidades, ya podés votar y jubilarte")
    print("Andá a pasar tiempo con tu nieto")
else:
    print("No, todavía no podés votar") # Resultado ilógico, una persona de 23 claramente puede votar

# esto se puede solucionar sacando el else y poniendo un "elif edad > 18 and edad < 65" al final 
# o rediseñando la lógica de los condicionales (por ej. reemplazando if edad >= 18 por if edad == 18) 

# Podemos probar multiples condiciones

personas = ['Jose', 'Carolina', 'Juan', 'Sofía']

if 'Jose' in personas:
    print("Hola Jose")
if 'Carolina' in personas:
    print("Buenos dias Carolina")
if 'Juan' in personas:
    print("Que gusto verte Juan")

# Todas estas condiciones se evaluan a verdadero. Si lo pusieramos en un if con elifs abajo, solo la primera condicion se evaluaria a verdadero
# Y se imprimiria un solo mensaje en vez de 3

if 'Jose' in personas:
    print("Hola Jose") # solo se imprime este
elif 'Carolina' in personas:
    print("Buenos dias Carolina") # este no
elif 'Juan' in personas:
    print("Que gusto verte Juan") # Y este tampoco


# Los ifs tambien puede operar sobre listas. 
# Una de las funciones mas útiles es chequear si la lista está vacia

cosas = ['Lapiz', 'Acuamarina', 'Moto', 'Salamines']

if cosas:
    print("Lista no vacia")

lista_vacia = []

if lista_vacia:
    print("esto no se cumple, la lista esta vacia")
else:
    print("La lista no tiene nada")

# Podemos utilizarlos anidados dentro de bucles, para comparar los contenidos de multiples listas

VIP_aeropuerto = ['Camila', 'Guada', 'Lucia']
pasajeras = ['Camila', 'Guada', 'Lucia', 'Sofia']

for pasajera in pasajeras:
    if pasajera in VIP_aeropuerto:
        print(f"{pasajera} puede pasar al VIP") # Entran todas, menos Sofia
    else:
        print(f"{pasajera} no está en la lista. Debe esperar el vuelo en la zona comun") 
