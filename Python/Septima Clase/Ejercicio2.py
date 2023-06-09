print(" ");
print("-------------------------")
print("    Menu de opciones")
print("-------------------------")
print(" ");


Amasado = 1500;
Molde = 1000;
Baguette = 2000;
Integral = 3000;

acumular = 0;
acumular2 = 0;
acumular3 = 0;
acumular4 = 0;

contador = 0;
contador2 = 0;
contador3 = 0;
contador4 = 0;

flag2 = True;

while flag2:
    flag = True;
    print(" ");
    print("---------------------------");
    print("     Menú    ");
    print("1) Comprar Pan");
    print("2) Emitir Boleta");
    print("3) Salir");
    print("---------------------------");
    print(" ");
    try:
        op2 = int(input("Ingresa una opción: "));
        if op2 == 1:
            while flag:
                print
                print(" ");
                print("-------------------------------")
                print("¿Que quieres comprar?");
                print(f"1) Amasado = ${Amasado}");
                print(f"2) Molde = ${Molde}");
                print(f"3) Baguette = ${Baguette}");
                print(f"4) Integral = ${Integral}");
                print(f"5) Regresar al Menú");
                print("-------------------------------")
                print(" ");
                try:
                    op = int(input("Ingresa una opcion: "));
                    print(" ");
                    if op == 1:
                        acumular = acumular + Amasado;
                        contador = contador + 1;
                        print("-------------------------------")
                        print(f"Llevas un total de {acumular + acumular2 + acumular3 + acumular4}");
                        print("-------------------------------");
                    elif op == 2:
                        acumular2 = acumular2 + Molde;
                        contador2 = contador2 + 1;
                        print("-------------------------------");
                        print(f"LLevas un total de {acumular + acumular2 + acumular3 + acumular4}");
                        print("-------------------------------");
                    elif op == 3:
                        acumular3 = acumular3 + Baguette;
                        contador3 = contador3 + 1;
                        print("-------------------------------");
                        print(f"Llevas un total de {acumular + acumular2 + acumular3 + acumular4}");
                        print("-------------------------------");
                    elif op == 4:
                        acumular4 = acumular4 + Integral;
                        contador4 = contador4 + 1;
                        print("-------------------------------");
                        print(f"Llevas un total de {acumular + acumular2 + acumular3 + acumular4}");
                        print("-------------------------------");
                    elif op == 5:
                        flag = False;
                        flag2 = True;
                        if flag2 == True:
                            flag2 == False
                            if flag2 == False:
                                flag == True;
                except ValueError:
                    print("ingresa un valor entero");
                    flag = True;
        elif op2 == 2:
            total = acumular + acumular2 + acumular3 + acumular4;
            if total == 0:
                print(f"No comprado ningun pan, por lo cual estas pagando un total de {total}");
            elif total > 5000:
                print("------------------------------");
                print("     Boleta      ");
                print("------------------------------");
                print(" ");
                print(f"Total a pagar: {total} (Envio Gratis)");
                print(f"Pan Amasado comprados: {contador}");
                print(f"Pan Molde comprados: {contador2}");
                print(f"Pan Baguette comprados: {contador3}");
                print(f"Pan integral comprados: {contador4}");
                print(" ");
                print(f"Gracias por comprar en DuocYa!");
            elif total < 5000:
                adicional = total * 0.10;
                total_con_adicional = int(total + adicional);
                print("------------------------------");
                print("     Boleta      ");
                print("------------------------------");
                print(" ");
                print(f"Total a pagar: {total_con_adicional} (Envio no Gratis)");
                print(f"Pan Amasado: {contador}");
                print(f"Pan Molde: {contador2}");
                print(f"Pan Baguette: {contador3}");
                print(f"Pan integral: {contador4}");
                print(" ");
                print(f"Gracias por comprar en DuocYa!");
            flag = False
        elif op2 == 3:
            print("Gracias por comprar");
            flag2 = False;
    except ValueError:
        print("Ingresa un valor numero valido");
