import numpy as np

# Crear dos arreglos unidimensionales con nombre A y B y de tamaño 10, 
# con elementos aleatorios de números enteros del 0 al 300
A = np.random.randint(0, 301, 10)
B = np.random.randint(0, 301, 10)

# Mostrar por pantalla la suma de los elementos de cada arreglo.
print("Suma de los elementos del arreglo A: ", np.sum(A))
print("Suma de los elementos del arreglo B: ", np.sum(B))

# Mostrar por pantalla la suma de los elementos de ambos arreglos.
print("Suma de los elementos de ambos arreglos: ", np.sum(A) + np.sum(B))

# Mostrar por pantalla la tabla de multiplicar de los elementos impares del arreglo B
B_impares = B[B % 2 != 0]
for i in B_impares:
    print(f"Tabla de multiplicar del {i}:")
    for j in range(1, 11):
        print(f"{i} x {j} = {i*j}")
