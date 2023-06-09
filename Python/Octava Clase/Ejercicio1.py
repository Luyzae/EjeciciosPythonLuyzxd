
n = int(input("Ingrese un numero: "))

numero = [n]

for multiplicacion in range(2, 11):

    resultado = n * multiplicacion
    numero.append(resultado)

print(numero)