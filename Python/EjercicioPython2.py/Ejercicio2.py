import numpy as np

# Crear un arreglo unidimensional con nombre arreglo_1 y de tamaño 10, con elementos aleatorios de números enteros del 0 al 1000
arreglo_1 = np.random.randint(0, 1001, 10)

# Mostrar por pantalla todos los elementos del arreglo.
print("Elementos del arreglo: ", arreglo_1)

# Contar los elementos pares.
num_pares = np.sum(arreglo_1 % 2 == 0)
print("Cantidad de elementos pares: ", num_pares)

# Sumar los elementos impares.
suma_impares = np.sum(arreglo_1[arreglo_1 % 2 != 0])
print("Suma de elementos impares: ", suma_impares)

# Emitir mensaje de cada elemento que sea primo.
for elemento in arreglo_1:
    if elemento > 1:  # Solo los números mayores a 1 pueden ser primos
        for i in range(2, int(np.sqrt(elemento)) + 1):
            if elemento % i == 0:  # Si el número tiene un divisor, no es primo
                break
        else:  # Este else se ejecuta si el for no se rompe, lo que significa que el número es primo
            print(f"El elemento {elemento} es primo.")
