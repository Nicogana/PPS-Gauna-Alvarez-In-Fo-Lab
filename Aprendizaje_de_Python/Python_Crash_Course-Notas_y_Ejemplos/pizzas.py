def hacer_pizza(tamaño, *ingredientes):                                       
     if 'ananá' in ingredientes or 'piña' in ingredientes:
        print("no.")
     else:
        print(f"Preparando una pizza {tamaño.lower()} con: ")
        for ingrediente in ingredientes:
            print(f"- {ingrediente.title()}")

def pedir_pizza():  
     print("pizza pedida")