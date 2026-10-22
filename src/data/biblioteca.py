"""Libros y categorías almacenadas"""
from models.libro import Libro

# Lista de libros (usa esta estructura)
libros: list[Libro] = [
    {"titulo": "Cien años de soledad", "autor": "García Márquez",
        "paginas": 471, "disponible": True},
    {"titulo": "Don Quijote", "autor": "Cervantes",
        "paginas": 863, "disponible": False},
    {"titulo": "El principito", "autor": "Saint-Exupéry",
        "paginas": 96, "disponible": True},
    {"titulo": "1984", "autor": "George Orwell", "paginas": 328, "disponible": True}
]

# SET con las categorías disponibles
categorias = {"Ficción", "Ciencia", "Historia", "Poesía"}
