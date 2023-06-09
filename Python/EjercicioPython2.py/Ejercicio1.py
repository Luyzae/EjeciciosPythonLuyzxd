import numpy as np

arregloA = np.random.randint(0, 501, 100)

print("Valores en índices pares: ", arregloA[::2])

print("Elemento mayor: ", np.max(arregloA))

print("Índice del elemento mayor: ", np.argmax(arregloA))

print("Elemento menor: ", np.min(arregloA))

arregloB = arregloA.copy() * 3
print("Arreglo B (copia de A multiplicado por 3): ", arregloB)

print("Suma de los elementos de B: ", np.sum(arregloB))

print("Promedio de los elementos de B: ", np.mean(arregloB))
