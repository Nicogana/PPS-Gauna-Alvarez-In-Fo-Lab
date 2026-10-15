# En cuanto a los apóstrofos, primero se observa que si intercambiamos los ' entre "" se muestra el mensaje normal
message = "One of Python's strengths is its diverse community."
print(message)

# Pero si se utiliza entre ' ', ocurre un error pues luego del apóstrofo intermedio, no reconoce que siga la cadena.

message = 'One of Python's strengths is its diverse community.'
print(message)
