import numpy as np

matriz = np.array([
    ['a', 'b', 'c', 'd'],
    ['e', 'f', 'g', 'h'],
    ['i', 'j', 'k', 'l'],
    ['m', 'n', 'o', 'p']
])

print("Matriz:")
print(matriz)

a = matriz.flatten()

vocales = ['a', 'e', 'i', 'o', 'u']

contador = 0
for i in a:
    if i in vocales:
        contador += 1

print("\nNúmero de vocales en la matriz:")
print(contador)
