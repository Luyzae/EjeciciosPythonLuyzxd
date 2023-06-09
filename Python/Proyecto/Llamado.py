from Funcionaes import *


flag = True;

while flag:
    menu();
    op = int(input("Ingresa una opcion: "))
    if op == 1:
        Calcular_Iva();
    elif op == 2 :
        Descuento();
    elif op == 3:
        Calcular_IMC();
    elif op == 4:
        break;