# Aquí se ve como se utilizan los distintos espacios, como TAB, espacio normal o salto de línea.
print("Python")
#Python
print("\tPython")
# Python 

print("Languages:\nPython\nC\nJavaScript")
#Languages:
#Python
#C
#JavaScript 
print("Languages:\n\tPython\n\tC\n\tJavaScript")
#Languages:
# Python
# C
# JavaScript 
# En este caso, se quita el espacio en blanco solo para el rstrip
favorite_language = 'python '
print(favorite_language)
print(favorite_language.rstrip())
print(favorite_language)

# En este caso, se utiliza el rstrip dentro de la variable
favorite_language = 'python '
favorite_language = favorite_language.rstrip()
print(favorite_language)

# En este caso, saco los espacios a derecha, luego a izquierda y luego todos
favorite_language = ' python '
print(favorite_language.rstrip())
#' python'
print(favorite_language.lstrip())
#'python '
print(favorite_language.strip())
#'python'
