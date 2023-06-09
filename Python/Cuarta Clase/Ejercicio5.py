print("-------------------------------------------------------------");
print("Bienvenido al programa que generará las tablas del 1 al 10")
print("-------------------------------------------------------------");


for i in range(1,11):
    print(f"Tabla de multiplicar del {i}");
    for t in range(1,11):
        tablas = i * t;
        print(f"{i} x {t} = {tablas}");