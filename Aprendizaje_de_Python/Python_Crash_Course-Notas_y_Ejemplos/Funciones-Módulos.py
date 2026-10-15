# Las funciones se pueden agrupar en archivos llamados modulos, que luego se pueden 
# importar a otros archivos usando la palabra clave import

import pizzas # esto nos da acceso a todas las funciones del modulo pizzas

pizzas.hacer_pizza('mediana', 'Jamon', 'Tomate', 'Queso')

pizzas.hacer_pizza('grande', 'piña')

pizzas.pedir_pizza

# tambien es posible importar solamente funciones especificas de un modulo, 
# usando el siguiente formato

# from modulo import funcion [, funcion_2] [, funcion_3]

# Puede pasar que una funcion que importamos tenga el mismo nombre 
# que alguna de las funciones de nuestro codigo. Para evitar conflictos, 
# podemos ponerle un alias al importarla 

# from modulo import funcion as alias

# por ejemplo 

from pizzas import hacer_pizza as hp

# Y si queremos importar todas las funciones del modulo, usamos el asterisco

from pizzas import * # trae todo el contenido del modulo