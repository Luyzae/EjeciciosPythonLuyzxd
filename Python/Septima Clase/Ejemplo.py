a = 4;
b = 2;

try:
    resultado = a / b;
except TypeError:
    print("Error: Estas tratando de dividir con una palabra");
except ZeroDivisionError:
    print("Erro: No se puede dividir por 0");
else:
    print(f"El resultado es {resultado}");