import numpy as np

matriz1 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
matriz2 = np.array([[10, 11, 12], [13, 14, 15], [16, 17, 18]])

print("Matriz 1:")
print(matriz1)

print("Matriz 2:")
print(matriz2)

resultado = np.matmul(matriz1, matriz2)

print("Resultado de la multiplicación de matriz 1 y matriz 2:")
print(resultado)
