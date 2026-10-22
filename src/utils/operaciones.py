from models.libro import Libro

def promedio_paginas(libros: list[Libro]):
    """Calcula el promedio de páginas de todos los libros"""
    total_paginas = 0

    for libro in libros:
        total_paginas += libro["paginas"]

    return total_paginas / len(libros)

def contar_libros(libros: list[Libro]):
    """Retorna la cantidad total de libros"""
    return len(libros)

def mostrar_disponibles(lista_libros: list[Libro]):
    """Muestra solo los libros que están disponibles"""
    for libro in lista_libros:
        if libro["disponible"]:
            print(f'Título: {libro["titulo"]}')
            print(f'Autor: {libro["autor"]}')
            print(f'Páginas: {libro["paginas"]}')


def buscar_por_paginas(lista_libros: list[Libro], max_paginas: int):
    """Muestra libros con menos páginas que max_paginas"""
    for libro in lista_libros:
        if libro["paginas"] < max_paginas:
            print(f'Título: {libro["titulo"]}')
            print(f'Autor: {libro["autor"]}')
            print(f'Páginas: {libro["paginas"]}')


def agregar_categoria(set_categorias: set[str], nueva_categoria: str):
    """Agrega una nueva categoría al set"""
    set_categorias.add(nueva_categoria)
    print("Categoría agregada correctamente.")