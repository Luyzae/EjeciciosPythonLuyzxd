acumulador = 0;
contador = 0;

num_1 = int(input("Ingresa un numero: "));
num_2 = int(input("Ingresa un numero: "));
num_3 = int(input("Ingresa un numero: "));

if num_1 % 2 == 0 :
    acumulador = acumulador + num_1;
    contador = contador + 1;
if num_2 % 2 == 0 :
    acumulador = acumulador + num_2;
    contador = contador + 1;
if num_3 % 2 == 0 :
    acumulador = acumulador + num_3;
    contador = contador + 1;

print(f"Los numeros pares acumulados son: {acumulador}");
print(f"Los numeros pares contados son: {contador}");