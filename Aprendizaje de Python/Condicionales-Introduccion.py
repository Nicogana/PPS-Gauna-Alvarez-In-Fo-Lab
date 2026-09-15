autos = ['audi', 'bmw', 'subaru', 'toyota']
for auto in autos:
    if auto == 'bmw':
        print(auto.upper())
    else:
        print(auto.title())
#Esto lo que hace es que si el auto es BMW lo ponga en mayúscula completamente
#Pero si es cualquier otro sólo ponga la primera letra en mayúscula

#Ahora veamos cada condicional

auto = 'bmw'
print(auto == 'bmw') # Se verifica si son iguales con ==, y da True
print(auto == 'audi') # Da false


alumno = "José"
print(alumno == "josé") # false, case sensitive
print(alumno.lower()=="josé") #True!

if alumno!="Gauna": ## No debe ser igual a gauna para dar TRUE
    print("Ese no es Nicolás!")

edad = 18
print(edad==18)

# Se pueden utilizar < >= > <=
# Para ver mas de una condicion se usa and
materias_jose=6
materias_nico=7
print(materias_jose > 6 and materias_nico > 6) #FALSE 
print(materias_jose > 6 or materias_nico > 6) # True

# Para verificar si algo está en una lista, se utiliza in

catedras = ['SSOO', 'Gestion de Redes', 'PPS']
print("SSOO" in catedras) #TRUE
print("Programación A" in catedras) #FALSE

if "Etica" not in catedras:
    print(f"No se está cursando Ética en estos momentos")
