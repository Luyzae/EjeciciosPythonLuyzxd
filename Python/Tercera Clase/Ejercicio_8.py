precio_zapato = 20000
total_sin_envio = 0
contador_zapatos = 0

print("Ingrese la cantidad de zapatos que desea comprar, o presione enter para terminar.")
for i in range(1000):
    cantidad = input(f"Cantidad de zapatos {i+1}: ")
    if not cantidad:
        break
    cantidad = int(cantidad)
    contador_zapatos += cantidad
    total_sin_envio += precio_zapato * cantidad

    if total_sin_envio >= 40000:
        total_con_envio = total_sin_envio
        envio = "gratis"
    else:
        total_con_envio = total_sin_envio + 3000
        envio = "con costo adicional de $3000"

print(f"Usted ha comprado {contador_zapatos} zapatos, por un total de ${total_con_envio} ({envio})")