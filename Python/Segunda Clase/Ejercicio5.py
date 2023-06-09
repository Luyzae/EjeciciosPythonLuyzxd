num1 = int(input("Ingresa un numero: "));
num2 = int(input("Ingresa un numero: "));
num3 = int(input("Ingresa un numero: "));

par = 0;
contarImpares = 0;
contarPares = 0;

if num1 and num2 and num3 > 0:
    if num1 % 2 == 0 and num2 % 2 == 0 and num3 % 2 == 0:
        par = 1;
        sumar = num1 + num2 + num3;
        print("-----------------------------------------------------");
        print (f"La suma de los numeros pares es {sumar}");
        print("-----------------------------------------------------");
    else:
        if num1 % 2 == 1:
            contarImpares = contarImpares+1;
        else:
            contarPares = contarPares+1;
        if num2 % 2 == 1:
            contarImpares = contarImpares+1;
        else:
            contarPares = contarPares+1;
        if num3 % 2 == 1:
            contarImpares = contarImpares+1;
        else:
            contarPares = contarPares+1;
        print("-----------------------------------------------------");
        print(f"La cantidad de numeros impares son: {contarImpares} y los pares son: {contarPares}");
        print("-----------------------------------------------------");
        print("Si quieres sumar los numeros, ingresa numeros pares");
        print("-----------------------------------------------------");

else:
    print("Ingresa numeros mayores a 0");