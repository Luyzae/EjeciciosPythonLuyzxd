"""Crear una copia del arreglo y muestre:
° Elemento mayor
° Elemento menor
° Suma de los elementos
° Promedio de los elementos
° Mostrar todos los elementos"""

import numpy as np

elementos = input("Ingrese los números: ")
elementos_lista = elementos.split()
A = np.array(elementos_lista, dtype=int)

A_copia = A.copy()

mayor = np.max(A_copia)
print("Elemento mayor:", mayor)

menor = np.min(A_copia)
print("Elemento menor:", menor)

suma = np.sum(A_copia)
print("Suma:", suma)

promedio = np.mean(A_copia)
print("Promedio:", promedio)

print("Elementos:")
print(A_copia)

