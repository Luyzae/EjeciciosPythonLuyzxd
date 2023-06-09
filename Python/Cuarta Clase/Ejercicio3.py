print("---------------------------------------------------------------");
print("Bienvenido al programa para saber si tu numero es primo o no")
print("---------------------------------------------------------------");

for n in range(1):
    num = int(input("Ingresa un numero: "));
    if num >= 2:
        validarPrimo = True;
        for a in range (2, num):
            if num % a == 0:
                validarPrimo = False;
        if validarPrimo:
            print(f"El numero {num} es primo");
        else:
            print(f"El numero {num} no es primo");
    else:
        print("El numero debe ser mayor a uno");