def calculo(precio, descuento):

    return precio - (precio * descuento / 100)

datos = [10000, 10]

print(calculo(*datos))