num1 = int(input("Ingresa un numero: "))
num2 = int(input("Ingresa un numero: "))
num3 = int(input("Ingresa un numero: "))

menores = 0

if num1 < 0:
    menores += 1
if num2 < 0:
    menores += 1
if num3 < 0:
    menores += 1

print(f"Hay un total de {menores} numeros menores a cero.")
