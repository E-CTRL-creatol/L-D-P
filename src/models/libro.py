"""Anotaciones de tipo del libro en la lista de libros"""
from typing import TypedDict

class Libro(TypedDict):
    titulo: str
    autor: str
    paginas: int
    disponible: bool
