print("-------------------------")
print("    Menu de opciones")
print("-------------------------")

flag = True;

fionaci = 0;

while flag:
    print("¿Que quieres elegir?")
    print("1) Indicar si un numero es par o no")
    print("2) Mostrar los primeros 10 números de la serie Fibonacci")
    print("3) Salir")
    try:
        op = int(input("Ingresa una opcion: "));
        if op == 1:
            n = int(input("Ingresa un numero: "));
            if n % 2 == 0:
                print("----------------------------");
                print(f"El numero {n} es par");
                print("----------------------------");
            else:
                print("----------------------------");
                print(f"El numero {n} no es par");
                print("----------------------------");
        elif op == 2:
            a, b = 0, 1
            for i in range(10):
                print(a);
                a, b = b, a + b;
        elif op == 3:
            print("Gracias por usar le programa");
            flag = False
        else:
            print("Ingresa un numero del 1 al 3")
    except ValueError:
        print("ingresa un valor entero");
        flag = True;