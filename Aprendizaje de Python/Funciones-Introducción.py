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

def describir_cuadro_de_futbol(nombre, descripcion):
    print(f"Soy de {nombre}")
    print(f"{descripcion}")

describir_cuadro_de_futbol('San Lorenzo', 'Cuervo')
describir_cuadro_de_futbol('Boca', 'Xeneize')

