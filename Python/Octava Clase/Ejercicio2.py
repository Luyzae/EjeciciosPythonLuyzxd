num = []


while True:
    try:
        n = int(input("Ingrese un número entero: "))
        if n == 0:
            break
        num.append(n)
    except ValueError:
        print("Error: Ingresa un numero")
num.sort()

print("Numeros ordenados en forma ascendente: ")
print(num)
