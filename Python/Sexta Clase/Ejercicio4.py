num = int (input("Ingresa un numero entre 103 y 987: "));

a = 1;
resultado = 0;
if num < 103:
    print("Ingrsa un numero mayor o igual a 103");
elif num > 987:
    print("Ingrsa un numero menor o igual a 987");

while a <= 3:
    resto = num % 10;
    resultado=(resultado * 10) + resto;
    num = num//10;
    a+=1;
    print(f"El resultado es {resultado}");