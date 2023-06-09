
BN= 150;
COLOR=300;
FOTOCOPIA = 80;
ANILLADO = 5000;


acumular = 0;
acumular2 = 0;
acumular3 = 0;
acumular4 = 0;

contador = 0;
contador2 = 0;
contador3 = 0;
contador4 = 0;

flag = True;

login = False;

while not login:
    try:
        usuario = str(input("Ingresa tu nombre de usuario: "))
        contrasena = int(input("Ingresa tu contraseña: "))
    
        if usuario == "fcalfun" and contrasena == 1234 or usuario == "Luis" and contrasena == 12345:
            print("--------------------------")
            print("inicio de session exitoso")
            print("----------------------------")
            login = True;
        else:
            print("----------------------------")
            print("Datos incorrectos");
            print("----------------------------")
    except ValueError:
        print("Error: Ingresa datos validos");


while flag:
    flag3 = True;
    flag2 = True;
    print("------------------------------")
    print("Menu de inicio");
    print("")
    print("1) Servicio de fotocopiado");
    print("2) Boleta");
    print("3) Salir");
    op = int(input("Ingresa la opcion que prefieras: "))
    if op == 1:
        while flag2:
            flagtest = True;
            test2 = True;
            print("---------------")
            print("¿Que quieres hacer?");
            print("")
            print("1) Impresión");
            print("2) Fotocopias");
            print("3) anillados");
            print("4) Menú principal");
            op2 = int(input("Ingresa la opcion que prefieras: "));
            if op2 == 1:
                while flagtest:
                    print(" ");
                    print("-----------------")
                    print("     ¿Imprimir a:?")
                    print(f"1) Sin color ${BN}")
                    print(f"2) Con color ${COLOR}")
                    print(f"3) Regresar al menú anterior")
                    op3 = int(input("Ingresa la opcion que prefieras: "));
                    if op3 == 1:
                        acumular = acumular + BN;
                        contador = contador + 1;

                        totalImpresion = acumular + acumular2;
                        print(" ");
                        print("------------------------------");
                        print(f"Llevas un total de: {contador} hojas imprimidas sin color");
                        print(f"Llevas un total de: ${acumular}");
                        print("------------------------------");
                        print(" ");
                        print("--------------------------------");
                        print(f"En la seccion de Impresión, llevas un total de: {totalImpresion}")
                        print("--------------------------------");
                        print(" ");

                    elif op3 == 2:
                        acumular2= acumular2 + COLOR
                        contador2 = contador2 + 1;

                        totalImpresion = acumular + acumular2;
                        print(" ");
                        print("------------------------------")
                        print(f"Llevas un total de: {contador2} hojas imprimidas con color");
                        print(f"Llevas un total de: ${acumular2}")
                        print("------------------------------");
                        print(" ");
                        print("--------------------------------");
                        print(f"En la seccion de Impresión, llevas un total de: {totalImpresion}")
                        print("--------------------------------");
                        print(" ");
                    elif op3 == 3:
                        flagtest = False;
            elif op2 == 2:
                while test2:
                    print(" ");
                    print("---------------------------")
                    print(F"Fotocopias")
                    print(f"precio: {FOTOCOPIA}");
                    print("---------------------------")
                    print("¿Quieres continuar?")
                    print("1) Si")
                    print("2) No")
                    print(" ");
                    op4 = int(input("Ingresa la opcion que prefieras: "))
                    if op4 == 1:
                        acumular3 = acumular3 + FOTOCOPIA
                        contador3 = contador3 + 1;
                        print("------------------------------")
                        print(f"En esta seccion llevas un total de {acumular3}");
                        print("------------------------------");
                    elif op4 == 2:
                        test2 = False;
            elif op2 == 3:
                print(" ");
                print(F"Anillados \nEste servicio tiene un total de ${ANILLADO} \n¿Quieres continuar?");
                print("1) Si")
                print("2) No")
                op5 = int(input("Ingresa una opcion que prefieras: "));
                if op5 == 1:
                    acumular4 = acumular4 + ANILLADO;
                    contador4 = contador4 + 1;
                    print("------------------------------");
                    print(f"En esta seccion llevas un total de {acumular4}");
                    print("------------------------------");
                if op5 == 2:
                    flag2 = True;
            elif op2 == 4:
                flag2 = False;
    elif op == 2:
        if acumular or acumular2 or acumular3 or acumular4 > 1:
            while flag3:
                flag3 = True
                print(" ")
                print("Bienvenido al sistema de boleta");
                print(" ")
                print("1) Diurno");
                print("2) Vispertino");
                print("3) Administrativo")
                print("4) Vaciar compras")
                print("4) Menú principal");
                op6 = int(input("Ingresa un opcion que prefieras: "));
                if op6 == 1:
                    print("-------------------------------------------------------")
                    print("Felicidades, por ser diurno, tienes un descueto de 10%")
                    print("-------------------------------------------------------")
                    print(" ")
                    print("------------------------")
                    print("Servicio de fotocopiado")
                    print(" ")
                    print(f"Hojas imprimidas en b/n = {contador}")
                    print(f"Hojas imprimidas en color = {contador2}")
                    print(f"Hojas fotocopiadas {contador3}")
                    print(f"Hojas anilladas = {contador4}")
                    totalhojas = contador + contador2 + contador3 + contador4
                    print("")
                    print(f"Hojas totales {totalhojas}")
                    print("")
                    print(f"Valor Total imprimidas en b/n = {acumular}")
                    print(f"Valor Total imprimidas en color = {acumular2}")
                    print(f"Valor Total fotocopiadas {acumular3}")
                    print(f"Valor Total anilladas = {acumular4}")
                    totalacumulado= acumular + acumular2 + acumular3 + acumular4;
                    descuento = totalacumulado * 0.10
                    descuentototal = descuento + 1;
                    print("")
                    print(f"SubTotal: {totalacumulado}")
                    print(f"Descuento: {descuentototal}");
                    totalDiruno = totalacumulado - descuentototal;
                    print(f"Total a pagar {totalDiruno}");
                    print("")
                elif op6 == 2:
                    print("---------------------------------------------------------")
                    print("Felicidades, por ser vispertino, tienes un descueto de 20%")
                    print("---------------------------------------------------------")
                    print(" ")
                    print("------------------------")
                    print("Servicio de fotocopiado")
                    print(" ")
                    print(f"Hojas imprimidas en b/n = {contador}")
                    print(f"Hojas imprimidas en color = {contador2}")
                    print(f"Hojas fotocopiadas {contador3}")
                    print(f"Hojas anilladas = {contador4}")
                    totalhojas2 = contador + contador2 + contador3 + contador4
                    print("")
                    print(f"Hojas totales {totalhojas}")
                    print("")
                    print(f"Valor Total imprimidas en b/n = {acumular}")
                    print(f"Valor Total imprimidas en color = {acumular2}")
                    print(f"Valor Total fotocopiadas {acumular3}")
                    print(f"Valor Total anilladas = {acumular4}")
                    totalacumulado2= acumular + acumular2 + acumular3 + acumular4;
                    descuento2 = totalacumulado2 * 0.20
                    descuentototal2 = descuento2 + 1;
                    print("")
                    print(f"SubTotal: {totalacumulado2}")
                    print(f"Descuento: {descuentototal2}");
                    totalVispertino2 = totalacumulado2 - descuentototal2;
                    print(f"Total a pagar {totalVispertino2}");
                    print("")
                elif op6 == 3:
                    print("---------------------------------------------------------")
                    print("No se te aplica ningun descuento")
                    print("---------------------------------------------------------")
                    print(" ")
                    print("------------------------")
                    print("Servicio de fotocopiado")
                    print(" ")
                    print(f"Hojas imprimidas en b/n = {contador}")
                    print(f"Hojas imprimidas en color = {contador2}")
                    print(f"Hojas fotocopiadas {contador3}")
                    print(f"Hojas anilladas = {contador4}")
                    totalhojas3 = contador + contador2 + contador3 + contador4
                    print("")
                    print(f"Hojas totales {totalhojas3}")
                    print("")
                    print(f"Valor Total imprimidas en b/n = {acumular}")
                    print(f"Valor Total imprimidas en color = {acumular2}")
                    print(f"Valor Total fotocopiadas {acumular3}")
                    print(f"Valor Total anilladas = {acumular4}")
                    totalacumulado3= acumular + acumular2 + acumular3 + acumular4;
                    print("")
                    print(f"SubTotal: {totalacumulado3}")
                    print(f"Total a pagar {totalacumulado}");
                    print("")
                elif op6 == 4:
                    acumular = 0
                    acumular2 = 0
                    acumular3 = 0
                    acumular4 = 0;
                    contador = 0;
                    contador2 = 0;
                    contador3 = 0;
                    contador4 = 0;
                    flag3 = False;
        else:
            print("-------------------------")
            print("No has comprado nada");
            print("--------------------------")

    elif op == 3:
        print("---------------------------------------")
        print("Gracias por elegir nuestro sistema, vuelva pronto")
        print("---------------------------------------")
        flag = False;