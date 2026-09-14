# Otro tipo de variable muy importante en Python son los tipos de datos numéricos, que nos permiten realizar operaciones matemáticas y cálculos. 
# En Python, los números pueden ser enteros (int) o decimales (float).

2+3 # 5

3-1 # 1

2 * 3 # 6

6 / 2 # 3

# ademas de las operaciones básicas, Python permite realizar operaciones más avanzadas, cómo la potenciación o la división decimal 

2 ** 3 # 8

3 ** 3 # 27

10 ** 6 # 1000000

10 / 3 # 3.3333333333333335

# Los paréntesis permiten cambiar el orden de las operaciones.

2 + 3*4 # 14
(2 + 3) * 4 # 20

# los decimales se representan mediante el punto decimal

0.1 + 0.1 # 0.2

2 * 0.5 # 1.0

# En algúnos casos, algunas operaciones pueden dar resultados raros. 
# Esto es normal, tiene que ver con la forma en que los números decimales se representan en la memoria de computadora. 

0.2 + 0.1 # 0.30000000000000004

3 * 0.1 # 0.30000000000000004

# La division en Python es inherentemente decimal, aunque los operadores sean enteros

4/2 # 2.0

# Si uno de los operadores es decimal, el resultado será decimal

2 * 3.0 # 6.0

3.0 ** 2 # 9.0

# Podemos usar guiónes bajos para separar los dígitos de un número, volviendolo más legible.

edad_del_universo = 13_800_000_000 # 13.8 mil millones de años

print(edad_del_universo) # imprime 13800000000

# Podemos utilizar asignar multiples variables en una sola línea, basta con separarlas con comas

x,y,z = 1,2,3

# Por último, vamos a mencionar la existencia de las constantes. Son variables cuyo valor no cambia durante la ejecución del programa.
# No existe cómo tal un tipo "Constante" pero por convención, se escriben en mayúsculas. 

PI = 3.14159 
CONSTANTE_DE_PLANCK = 6.62607015e-34