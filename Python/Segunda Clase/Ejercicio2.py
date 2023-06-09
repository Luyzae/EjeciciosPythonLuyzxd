num1 = int(input("Ingresa un numero: "));
num2 = int(input("Ingresa un numero: "));

if num1 and num2 > 1:
    suma = num1 + num2;
    print(f"La suma de {num1} + {num2} es {suma}");
if num1 or num2 <= -1:
    print("Ingresa solo numeros positivos");
    