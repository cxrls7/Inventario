

def calcular_total(precio,  cantidad):
    return precio * cantidad
    
def registrar_producto():

    
    nombre = input("-Ingresa el nombre del producto: ")
    
    

    precio = 0.0
    cantidad = 0
    
    while True:
        try:
            precio = float(input("-Precio del unitario del producto: "))
            break
        except ValueError:
            print("\n ❌ Ingresa un valor valido ❌")

    while True:
        try:
            cantidad = int(input("-Ingresa la cantidad del producto: "))
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
    valor_total_acumulado = 0
    cantidad_total_items = 0

    for producto in inventario:
        valor_total_acumulado += producto['total']
        cantidad_total_items += producto['cantidad']

    return valor_total_acumulado, cantidad_total_items
    
def actualizar_producto(inventario):

   nombre_buscar = input("Ingrese el nombre del producto a actualizar:").strip().lower()
   
   for producto in inventario:
            
            if producto['nombre'].lower() == nombre_buscar:
                    print(f"Producto encontrado {producto['nombre']}")
                    print(f"Parametros actuales {producto['nombre']} || {producto['cantidad']} || {producto['precio']} ")

            try:
            
            
              nueva_cantidad = int(input("Ingrese la nueva cantidad: "))
              nuevo_precio = float(input("Ingrese el nuevo precio: "))

              producto['cantidad'] = nueva_cantidad
              producto['precio'] = nuevo_precio
              producto['total'] = nueva_cantidad * nuevo_precio

              print("\nProducto actualizado con exito")
              return True
                
            except ValueError:
                    print("ERROR. INGRESA NUMEROS VALIDOS")
                    return False
                
   print(f"EL PRODUCTO {nombre_buscar} NO EXISTE")
   return False        




    