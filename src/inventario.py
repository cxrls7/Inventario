def calcular_total(precio,  cantidad):
    return precio * cantidad
    
def registrar_producto():

    
    nombre = input("-🖊️  Ingresa el nombre del producto: ")
    
    

    precio = 0.0
    cantidad = 0
    
    while True:
        try:
            precio = float(input("-💶 Precio del unitario del producto: "))
            break
        except ValueError:
            print("\n ❌ Ingresa un valor valido ❌")

    while True:
        try:
            cantidad = int(input("-📤 Ingresa la cantidad del producto: "))
            break
        except ValueError:
            print("\n❌ Ingresa un valor valido ❌")  

    total = precio * cantidad

    producto = {"nombre":nombre, "cantidad":cantidad, "precio":precio, "total":total}
    return producto


def buscar_producto(inventario, nombre_buscado  ):
    for producto in inventario :
       if producto['nombre'].strip().lower() == nombre_buscado.strip().lower():
          return producto
    return None 


def calcular_estadisticas(inventario):
    if not inventario:
        return None
    
    valor_total_acumulado = 0
    cantidad_total_items = 0
    mas_caro = inventario[0]
    mayor_stock = inventario[0]
    calcular_subtotal = lambda producto:producto["precio"] * producto["cantidad"]


    for producto in inventario:
        subtotal = calcular_subtotal(producto)
        valor_total_acumulado += subtotal
        cantidad_total_items += producto['cantidad']

        if producto['precio'] > mas_caro['precio']: 
            mas_caro = producto     

        if producto['cantidad'] > mayor_stock['cantidad']:
            mayor_stock = producto

    return {'unidades': cantidad_total_items, 'valor': valor_total_acumulado, 'mas_caro': mas_caro, 'mayor_stock': mayor_stock}



    

   