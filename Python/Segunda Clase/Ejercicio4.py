par = 0;

num = int(input("Ingresa un numero: "));

if num > 0 and num < 101:
    if num % 2 == 0:
        par = 1;
        print(f"Es par");
    else:
        print("Es impar");
else:
    print("Ingresa un numero entre el 1 y el 101");1