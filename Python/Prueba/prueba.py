def login():
    users = {"fcalfun": "1234", "usuario2": "contraseña2"}  # Usuarios registrados
    
    while True:
        user = input("Usuario: ")
        password = input("Contraseña: ")
        
        if user in users and password == users[user]:
            return user
        else:
            print("Usuario o contraseña incorrectos. Inténtelo nuevamente.")

def mostrar_menu():
    print("Menu de Servicios")
    print("1. Impresión B/N")
    print("2. Impresión Color")
    print("3. Fotocopias")
    print("4. Anillados")
    print("5. Anular pedido")
    print("6. Salir")

def calcular_descuento(total, tipo_alumno):
    if tipo_alumno == "diurna":
        descuento = total * 0.1
    elif tipo_alumno == "vespertina":
        descuento = total * 0.2
    else:
        descuento = 0
        
    return descuento

def calcular_total(opciones):
    precios = {"1": 150, "2": 300, "3": 80, "4": 5000}  # Precios de los servicios
    total = 0
    
    for opcion in opciones:
        total += precios[opcion]
    
    return total

def realizar_pedido(user):
    opciones = []
    tipo_alumno = input("Tipo de alumno (diurna/vespertina/administrativo): ")
    
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")
        
        if opcion == "5":  # Anular pedido
            return None
        
        if opcion == "6":  # Salir del programa
            return "salir"
        
        if opcion in ["1", "2", "3", "4"]:
            opciones.append(opcion)
        else:
            print("Opción inválida. Inténtelo nuevamente.")
        
        confirmacion = input("¿Desea agregar otro servicio? (s/n): ")
        
        if confirmacion.lower() != "s":
            break
    
    total = calcular_total(opciones)
    descuento = calcular_descuento(total, tipo_alumno)
    total_con_descuento = total - descuento
    
    print("Servicio de Fotocopiado")
    print("----------------------")
    
    for opcion in opciones:
        if opcion == "1":
            print("100 hojas B/N - $", 100 * 150)
        elif opcion == "2":
            print("150 hojas color - $", 150 * 300)
    
    print("----------------------")
    print("Subtotal - $", total)
    print("Descuento - $", descuento)
    print("----------------------")
    print("Total a pagar - $", total_con_descuento)
    print("Gracias por su compra")

# Programa principal
print("Bienvenido al Sistema de Fotocopiado de Duoc UC")

user = login()

while True:
    print("\nUsuario:", user)
    pedido = realizar_pedido(user)
    
    if pedido == None:  # Anular pedido
        continue
    elif pedido == "salir":  # Salir del programa
        break
