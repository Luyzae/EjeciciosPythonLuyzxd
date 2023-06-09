"""Crear un arreglo de dos dimensiones de tamaño 3 x 3, 
con elementosaleatorios de números enteros del 0 al 100"""

import numpy as np


A = np.random.randint(0, 101, size=(3, 3))

print(A)

