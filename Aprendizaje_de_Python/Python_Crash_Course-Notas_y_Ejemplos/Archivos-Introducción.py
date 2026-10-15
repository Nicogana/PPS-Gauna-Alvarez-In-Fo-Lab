# Los archivos son estructuras de datos
# que permiten persistir la información

# with open('pi.txt') as f:
#   datos = f.read()

# Imprime los datos del archivo
#print(datos)
# Esto le saca el caracter de nueva linea que tiene al final 
#print(datos.rstrip())

# Nótese que esto solo funciona si el archivo 
# que abrimos está en el mismo directorio 
# que el archivo donde está nuestro código
# Si se encuentra en otro directorio, debemos agregar su camino (o path)

path = 'C:/Users/alvar/OneDrive/Escritorio/Prueba_archivos/pi.txt'

with open(path) as f:
    datos = f.read()

print(datos)

# Tambien podemos leer el archivo linea por linea con un bucle for 

with open(path) as f:      
   for linea in f:       
    print(linea)


# Esto imprime: 
# 3.1415926535 

#  8979323846 

#  2643383279

# o usando la funcion readlines()

with open(path) as f:      
    lineas = f.readlines()

# Para sacar los caracteres en blanco, basta con poner rstrip()

# Por supuesto, 
# podemos trabajar con conjuntos de datos mucho mas grandes

# Por ejemplo, acá tenemos el primer millon de digitos de PI

path = 'C:/Users/alvar/OneDrive/Escritorio/Prueba_archivos/piM.txt'

with open(path) as f:
   lineas = f.readlines()     

pi_cad = ''

for linea in lineas:
   pi_cad += linea.strip()

print(f"{pi_cad[:52]}...")
print(len(pi_cad))

# Para trabajarlos un poco, busquemos la fecha de cumpleaños dentro de PI

cumple = input("Digité su fecha de cumpleaños: dd/mm/aa: ")

if cumple in pi_cad:
   print("Tu cumple está en el 1er millón de dígitos de PI")
else:
   print("Tu cumple NO está en el 1er millón de dígitos de PI")

# Todo lo previo es unicamente lectura. Vamos ahora con la escritura

arch = 'escritura.txt'

with open(arch, 'w') as f:
   f.write("Aguante el Info-Lab")
   f.write("muy lindo lugar")

# Esto escribe las lineas así: Aguante el Info-Labmuy lindo lugar

# Si queremos que se escriba separado, hay que agregar saltos de linea 

with open(arch, 'w') as f:
   f.write("Aguante el Info-Lab \n")
   f.write("muy lindo lugar \n")

# La funcion open permite abrir un archivo de diferentes modos. 
# Ya vimos el de lectura y el de escritura
# Tambien existe el a que permite agregar contenido al final de un archivo preexistente
# (a diferencia de la escritura, que pisa el contenido original)

with open(arch, 'a') as f:
   f.write("muy copada la gente \n")
   f.write("muy linda la oficina \n")
