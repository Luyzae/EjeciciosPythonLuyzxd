DESCUENTODIRUNA = 0.10;
DESCUENTOVISPERTINA = 0.20;

SINCOLOR = 150;
COLOR= 300;
FOTOCOPIAS = 80;
ANILLADOS = 5000;



login = False;

while not login:

    print("-----------------------------------------")
    print("           Sistema de logeo")
    print("")
    print("Por favor ingrese sus datos correctos.")
    print("-----------------------------------------")

    nombre = str(input("ingrese su nombre de usuario: "))
    print("-----------------------------------------")
    contraseña = int(input("Ingrese su contraseña: "))
    print("-----------------------------------------")

    if nombre == "Luis" and contraseña == 12345:
        print("")
        print("Inicio de sesion exitoso.")
        print("")
        print("-----------------------------------------")
        print(f"Bienvenido al Sistema de Fotocopiado {nombre}")
        print("-----------------------------------------")
        print("")
        login = True;
    else:
        print("Error: nombre de usuario y contraseña incorrecto.");

rolFlag = False;

while not rolFlag:
    print("")
    print("")
    print("-----------------------------------------")
    print("           Sistema de rol")
    print("")
    print("Por favor ingrese si eres: ")
    print("Diurno, Vispertina o administrativo. Para su respectivo descuento")
    print("-----------------------------------------")

    rol = str(input("Ingrese su rol: "));

    if rol == "Diurno":
        rolFlag = True;
        menuFlagDiurno = True;
        while menuFlagDiurno:
            sistemaFlag = True;
            print("")
            print("-----------------------------------------")
            print("           Bienvido al Menú principal")
            print(f"Usuario: {nombre}")
            print(f"Rol: {rol}")
            print("Descuento: 10%")
            print("")
            print("¿Que quieres hacer?")
            print("1) Ingresar al  Sistema de fotocopiado.")
            print("2) Vaciar compras.")
            print("3) Generar la boleta.")
            print("4) Salir del sistema.")
            menuOP = int(input("Ingresa la opcion que prefieras: "))
            if menuOP == 1:
                while sistemaFlag:
                    print("");
                    print("¿Que quieres hacer?")
                    print("1) Imprimir")
                    print("2) Fotocopias")
                    print("3) Anillados")
                    print("4) Regresar al Menú principal")
                    print("")
                    menuOP = int(input("Ingresa la opcion que prefieras: "))
                    if menuOP == 1:
                        print("gracias por imprimir")
                    elif menuOP == 2:
                        print("Gracias por fotocopiar")
                    elif menuOP == 3:
                        print("Gracias por Anillados")
                    elif menuOP == 4:
                        sistemaFlag = False;
                        menuFlagDiurno = True;
                    else:
                        print("")
                        print("---------------------------")
                        print("Ingresa una opcion valida")
                        print("---------------------------")
                        print("")
    if rol == "Vispertina":
        rolFlag = True;
        menuFlagVispertina = True;
        while menuFlagVispertina:
            sistemaFlag = True;
            print("")
            print("-----------------------------------------")
            print("           Bienvido al Menú principal")
            print(f"Usuario: {nombre}")
            print(f"Rol: {rol}")
            print("Descuento: 20%")
            print("")
            print("¿Que quieres hacer?")
            print("1) Ingresar al  Sistema de fotocopiado.")
            print("2) Vaciar compras.")
            print("3) Generar la boleta.")
            print("4) Salir del sistema.")
            menuOP = int(input("Ingresa la opcion que prefieras: "))
    if rol == "Administrativo":
        rolFlag = True;
        menuFlagAdministrativo = True;
        while menuFlagAdministrativo:
            sistemaFlag = True;
            print("")
            print("-----------------------------------------")
            print("           Bienvido al Menú principal")
            print(f"Usuario: {nombre}")
            print(f"Rol: {rol}")
            print("Descuento: No aplica")
            print("")
            print("¿Que quieres hacer?")
            print("1) Ingresar al  Sistema de fotocopiado.")
            print("2) Vaciar compras.")
            print("3) Generar la boleta.")
            print("4) Salir del sistema.")
            menuOP = int(input("Ingresa la opcion que prefieras: "))
    else:
        print("")
        print("------------------------------------------------------------------------------")
        print("Por favor, ingrese tal cual las palabras: Diruno, Vispertuno o Administrativo");
        print("------------------------------------------------------------------------------")
        print("")