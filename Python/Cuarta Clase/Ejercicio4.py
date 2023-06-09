print("-------------------------------------------------------------");
print("Bienvenido al programa para saber si tu numero es perfecto")
print("-------------------------------------------------------------");

num_perfecto = 0

for n in range(1):
    num = int(input("Ingresa un numero: "));
    for i in range(1,num):
        if num % i == 0:
            num_perfecto = num_perfecto + i;
if num_perfecto == num:
    print(f"El numero {num} es perfecto");
else:
    print(f"El numero {num} no es perfecto");