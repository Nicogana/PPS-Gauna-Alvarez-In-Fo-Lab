# Tuplas

dimensiones = (200,50)

# A diferencia de las listas, las tuplas son inmutables: una vez asignados, no podemos modificar uno de esos valores

# dimensiones[0]=250 --> ERROR!

for dimension in dimensiones:
    print(dimension)

# para redefinirla, se debe copiar encima de ella

dimensiones=(400,100)
for dimension in dimensiones:
    print(dimension)