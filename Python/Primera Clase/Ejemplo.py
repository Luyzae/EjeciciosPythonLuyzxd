usd = 790.88;
ars = 3.63;

while True:
    print("\nMenú de opciones:");
    print("1. Convertir dólares a pesos chilenos.");
    print("2. Convertir pesos chilenos a dólares.");
    print("3. Convertir pesos argentinos a pesos chilenos.");
    print("4. Salir del programa.");
    option = input("Ingrese la opción deseada: ");

    if option == "1":
        while True:
            try:
                dollar_amount = float(input("Ingrese la cantidad de dólares a convertir: "));
                break;
            except ValueError:
                print("Ingrese un valor numérico válido.");
        peso_amount = dollar_amount * usd;
        print(f"{dollar_amount:.2f} dólares son {peso_amount:.2f} pesos chilenos.");

    elif option == "2":
        while True:
            try:
                peso_amount = float(input("Ingrese la cantidad de pesos chilenos a convertir: "));
                break;
            except ValueError:
                print("Ingrese un valor numérico válido.");
        dollar_amount = peso_amount / usd;
        print(f"{peso_amount:.2f} pesos chilenos son {dollar_amount:.2f} dólares.");

    elif option == "3":
        while True:
            try:
                ars_amount = float(input("Ingrese la cantidad de pesos argentinos a convertir: "));
                break;
            except ValueError:
                print("Ingresa un valor numérico válido.");
        clp_amount = ars_amount * ars;
        print(f"{ars_amount:.2f} pesos argentinos son {clp_amount:.2f} pesos chilenos.");

    elif option == "4":
        print("Hasta luego");
        break;

    else:
        print("Error");
