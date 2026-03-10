def calcular_total(precio,  cantidad):
    return precio * cantidad
    




def registrar_producto():
    nombre = input("Ingresa el nombre del producto: ")
    
    precio = 0.0
    cantidad = 0
    
    while True:
        try:
            precio = float(input("Precio del unitario del producto: "))
            break
        except ValueError:
            print(" ❌ Ingresa un valor valido ❌")

    while True:
        try:
            cantidad = int(input("Ingresa la cantidad del producto: "))
            break
        except ValueError:
            print("❌ Ingresa un valor valido ❌")  

    total = precio * cantidad

    producto = {"nombre":nombre, "cantidad":cantidad, "precio":precio, "total":total}
    return producto


producto = registrar_producto()
print(f"{producto['nombre']}, registrado con exito")




   