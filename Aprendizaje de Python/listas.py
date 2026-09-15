# Primero, generamos una lista de alumnos

alumnos = ['Gauna', 'Juric', 'Colantonio', 'Torti']
print(alumnos)
# ['Gauna', 'Juric', 'Colantonio', 'Torti']

# Si quiero elegir uno en específico:

print(alumnos[0])
# Gauna -> trae el primero
print(alumnos[0].upper())
# GAUNA
print(alumnos[0].lower())
# gauna

# Los índices empiezan en 0 y se pueden utilizar variables negativas para señalizar
# tomando desde el fin de la lista

print(alumnos[-1])
# Torti -> último de la lista
# También lo podemos utilizar en otras variables:

message = f"Mi alumno favorito es {alumnos[0].title()}"
print(message)

# Mi alumno favorito es Gauna

# Ahora veamos modificaciones, adiciones y sustracciones
# Se tiene la lista Profesores y se modifica uno por otro

profesores =['Ana', 'Bruno', 'Pedro']
print(profesores)
#['Ana', 'Bruno', 'Pedro']
profesores[0]='Roberto'
print(profesores)
#['Roberto', 'Bruno', 'Pedro'] -> se reemplazó primera posición 'Ana' por 'Roberto'

#Agregar a lista:
profesores.append('Sandra')
print(profesores)
#Así podemos generar listas con [] y luego ir agregando con append
#También se puede insertar en cualquier orden
profesores.insert(1, 'Fernando')
print(profesores)
del profesores[1]
print(profesores)
#Eliminé a Fernando
# Remover de lista
profesores.remove('Roberto')
print(profesores)
vicedecana = profesores.pop(2)
print(f"La vicedecana es {vicedecana.title()}.")
#Se puede remover una variable que contenga algún valor!
muybuenprofesor='Bruno'
profesores.remove(muybuenprofesor)
print(profesores)
print(f"\n{muybuenprofesor.title()} es muy buen profesor.")

#Ordenar por orden alfabético y viceversa
profesores.append('Luis')
profesores.sort()
print(profesores)
profesores.sort(reverse=True)
print(profesores)

#Se pueden ordenar temporalmente
facultades=['ingeniería', 'medicina', 'economicas']
print(facultades)
print(sorted(facultades))
print(facultades)
# Invierte el orden insertado
facultades.reverse()
print(facultades)

#Longitud
print(len(facultades))
