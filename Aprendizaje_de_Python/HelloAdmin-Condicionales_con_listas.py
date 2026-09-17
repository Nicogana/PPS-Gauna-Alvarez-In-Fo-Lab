usuarios = ["José", "Nico", "admin", "Ivo", "Santi"]

for usuario in usuarios:
    if usuario == "admin":
        print (f"Hola {usuario.title()}, ¿quiere ver un reporte? ")
    else:
        print(f"Gracias por loguearse de nuevo, {usuario}")


usuarios=[]

if usuarios:
    for usuario in usuarios:
        if usuario == "admin":
            print (f"Hola {usuario.title()}, ¿quiere ver un reporte? ")
        else:
            print(f"Gracias por loguearse de nuevo, {usuario}")
else:
    print("Debemos encontrar más usuarios!")

usuarios_actuales = ['admin', 'juan', 'maria', 'carlos', 'sofia', 'lucas']
usuarios_nuevos = ['Juan', 'ana', 'MARTIN', 'sofia', 'pedro']

for usuario in usuarios_nuevos:
    if usuario.lower() in usuarios_actuales:
        print(f"{usuario} deberá ingresar un nuevo nombre de usuario.")
    else:
        print(f"{usuario} está disponible.")

numeros = list(range(1,10))
for numero in numeros:
    if numero == 1:
        print("1ro")
    elif numero == 2:
        print("2do")
    elif numero == 3:
        print("3ro")
    else:
        print(f"{numero}to")
