peliculas = []

def agregar_pelicula(title, year, genre):
    peliculas.append([title, year, genre])

def mostrar_peliculas():
    if len(peliculas) == 0:
        print("No hay películas registradas")
    else:
        print("Películas registradas")
        for movie in peliculas:
            print(f"Título: {movie[0]}, Año: {movie[1]}, Género: {movie[2]}")
        print()

def buscar_por_genero(genero):
    encontrados = []
    for movie in peliculas:
        if movie[2] == genero:
            encontrados.append(movie)
    if len(encontrados) > 0:
        print("¡Películas encontradas!")
        for movie in encontrados:
            print(f"Título: {movie[0]}, Año: {movie[1]}, Género: {movie[2]}")
    else:
        print("¡No se encontraron películas con ese género!")
    print()

def eliminar_por_titulo(titulo):
    for movie in peliculas:
        if movie[0] == titulo:
            peliculas.remove(movie)
            print("¡Tu película ha sido eliminada correctamente!")
            return
        print("No encontró tu película")

def estadísticas():
    print(f"\nTotal de películas: {len(peliculas)}")

    count = {}
    for movie in peliculas:
        genre = movie[2]
        if genre in count:
            count[genre] += 1
        else:
            count[genre] = 1

    print("Películas por género: ")
    for g in count:
        print(f" {g}: {count[g]}")

    if len(peliculas) > 0:
        mas_antigua = peliculas[0]
        for movie in peliculas:
            if movie[1] < mas_antigua[1]:
                mas_antigua = movie
        print(f"Película más antigua: {mas_antigua[0]} ({mas_antigua[1]})")
    print()

while True:
    print("MENÚ")

