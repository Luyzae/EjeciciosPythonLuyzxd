def menu():
    print("¿Que quieres hacer?")
    print("1) Calcular Iva de un prodcuto")
    print("2) Descuento de un producto")
    print("3) Calcular IMC")
    print("4) Salir del programa")


def Calcular_Iva():

    producto = int(input("Ingresa el valor del producto: "))

    iva = producto * 0.19;

    total = producto + iva;

    print(f"El total del producto con iva es de: {iva}")


def Descuento():

    pro = int(input("Ingresa el valor del producto: "))
    des = int(input("Ingresa tu descuento: "))

    total = pro - des

    print(f"El total del producto: {total}")


def Calcular_IMC():

    peso = float(input("Ingrese su peso: "))
    altura = float(input("Ingrese su altura: "))

    total = float((peso / altura**2));

    if total < 18.5:
        print("Bajo de peso");
    elif total >= 18.5 and total < 24.9:
        print("Peso adecuado");
    elif total >= 25.0 and total < 29.9:
        print("Obesidad grado 1");
    elif total >= 35.0 and total < 39.9:
        print("Obesidad grado 2")
    elif total > 40:
        print("Obesidad grado 3");