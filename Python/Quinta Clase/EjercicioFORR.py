import random

ancho = 80
alto = 20

fondo = []
for i in range(alto):
    fila = ''
    for j in range(ancho):
        fila += random.choice('*+ ')
    fondo.append(fila)
fondo[0] = fondo[0][:-1] + '*'

for fila in fondo:
    print(fila)