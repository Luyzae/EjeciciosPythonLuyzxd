print("--------------------------------------------------------------------------------------");
print("Bienvenido al programa que generará las tablas del 1 al 10 solo de lo numeros pares")
print("--------------------------------------------------------------------------------------");


for i in range(2,11,2):
    print(f"Tabla de multiplicar del {i}");
    for t in range(1,11):
        tablas = i * t;
        print(f"{i} x {t} = {tablas}");