ANCHO = 80
ALTURA = 20

seed = 1

cant_simbolos = int(input("Ingrese la cantidad de símbolos que desea utilizar: "))

simbolos = []
for i in range(cant_simbolos):
    simbolo = input(f"Ingrese el símbolo {i+1}: ")
    simbolos += simbolo;

for i in range(ALTURA):
    fila = ""
    for j in range(ANCHO):
        seed = (1103515245 * seed + 12345) % (2**31);
        num = seed % cant_simbolos;
        char = simbolos[num];
        fila = char + fila;
    print(fila);
