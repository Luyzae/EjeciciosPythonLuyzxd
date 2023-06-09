import numpy as np

matriz = np.random.randint(0, 101, size=(4, 5))

print("Matriz:")
print(matriz)

suma_filas = np.sum(matriz, axis=1)
print("\nSuma de los elementos de cada fila:")
print(suma_filas)

suma_columnas = np.sum(matriz, axis=0)
print("\nSuma de los elementos de cada columna:")
print(suma_columnas)

suma_diagonal = np.trace(matriz)
print("\nSuma de los elementos de la diagonal principal:")
print(suma_diagonal)

cantidad_impares = np.sum(matriz % 2 != 0)
print("\nCantidad de elementos impares:")
print(cantidad_impares)
