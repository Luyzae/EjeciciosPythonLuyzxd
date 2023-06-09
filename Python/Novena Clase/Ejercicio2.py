"""Utilice las siguientes funciones en el arreglo creado en el punto 
• Promedio de los elementos.
• Suma de los elementos.
• Mostrar el elemento mayor.
• Mostrar el elemento menor.
• Mostrar sólo los elementos de la diagonal principal."""


import numpy as np

A = []
for i in range(3):
    fila = input("Ingrese los numeros ")
    elementos = fila.split()
    fila_convertida = [int(num) for num in elementos]
    A.append(fila_convertida)

A = np.array(A)

promedio = np.mean(A)
print("Promedio:", promedio)

suma = np.sum(A)
print("Suma:", suma)

mayor = np.max(A)
print("Elemento mayor:", mayor)

menor = np.min(A)
print("Elemento menor:", menor)

diagonal_principal = np.diag(A)
print("Elementos de la diagonal principal:", diagonal_principal)



