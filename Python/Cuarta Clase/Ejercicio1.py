contarMayor = 0;
contarMenor = 0;
contarCeros = 0;
for n in range(5):
    num = int(input("Ingresa un numero: "));
    if num > 0:
        contarMayor=contarMayor+1;
    elif num < 0 :
        contarMenor = contarMenor +1;
    else:
        contarCeros=contarCeros+1;


print(f"La cantidad de numeros mayores a cero es: {contarMayor}");
print(f"La cantidad de numeros mayores a cero es: {contarMenor}");
print(f"La cantidad de numeros mayores a cero es: {contarCeros}");
