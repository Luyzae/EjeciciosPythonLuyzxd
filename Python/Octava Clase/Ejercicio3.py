numeros = []

for i in range(10):
    num = int(input("Ingrese un número: "))
    numeros.append(num)

suma = sum(numeros)
promedio = suma / len(numeros)

print("Suma de los elementos:", suma)
print("Promedio de los elementos:", promedio)
