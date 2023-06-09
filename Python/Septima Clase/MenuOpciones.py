print("-------------------------")
print("    Menu de opciones")
print("-------------------------")

flag = True;

while flag:
    print("¿Que quieres elegir?")
    print("1) Opcion 1")
    print("2) Opcion 2")
    print("3) Salir")
    try:
        op = int(input("Ingresa una opcion: "));
        if op == 1:
            print("Haz elegido la opcion 1");
        elif op == 2:
            print("Haz elegido la opcion 2");
        elif op == 3:
            print("Gracias por usar le programa");
            flag = False
        else:
            print("Ingresa un numero del 1 al 3")
    except ValueError:
        print("ingresa un valor entero");
        flag = True;