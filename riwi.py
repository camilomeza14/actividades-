pelicula = 0 
accion = 0 
comedia = 0
for i in range(5): # Registrar 5 clientes
    genero = input("Elija género (pelicula, accion, comedia): ").lower()
    if genero == "pelicula": pelicula += 1
    elif genero == "accion": accion += 1
    elif genero == "comedia": comedia += 1

print(f"Películas: {pelicula}")
print(f"Acción: {accion}")
print(f"Comedia: {comedia}") 
