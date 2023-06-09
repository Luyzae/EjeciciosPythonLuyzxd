"""Crear un arreglo de dos dimensiones de 3 x 3 con números ceros,
excepto la diagonal principal que debe contener en el mismo orden los
siguientes elementos 1, 2 y 3"""

import numpy as np


A = np.zeros((3, 3))


np.fill_diagonal(A, [1, 2, 3])

print(A)
