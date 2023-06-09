num = int(input("Ingresa un numero: "));

a = 1;
fact = 1;

while a <= num:
    fact = fact * a;
    a += 1;
print(f"El factorial de {num} es {fact}");

